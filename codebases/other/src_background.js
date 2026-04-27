// Background Service Worker for Project Symbiote
// Handles message routing, API calls, and state management

// State management
let currentContext = null;
let claudeApiKey = null;
let googleAuthToken = null;

// Initialize on install
chrome.runtime.onInstalled.addListener(() => {
  console.log('[Symbiote] Extension installed');
  
  // Load saved settings
  chrome.storage.local.get(['claudeApiKey', 'googleAuthToken'], (result) => {
    claudeApiKey = result.claudeApiKey;
    googleAuthToken = result.googleAuthToken;
  });

  // Set up side panel behavior
  chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true });
});

// Listen for storage changes
chrome.storage.onChanged.addListener((changes, namespace) => {
  if (namespace === 'local') {
    if (changes.claudeApiKey) {
      claudeApiKey = changes.claudeApiKey.newValue;
    }
    if (changes.googleAuthToken) {
      googleAuthToken = changes.googleAuthToken.newValue;
    }
  }
});

// Message handler
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log('[Symbiote] Received message:', message.type);

  switch (message.type) {
    case 'GRAB_CONTEXT':
      handleGrabContext(message, sender, sendResponse);
      return true;

    case 'SEND_COMMAND':
      handleSendCommand(message, sender, sendResponse);
      return true;

    case 'AUTHORIZE_GOOGLE_DRIVE':
      handleGoogleAuth(message, sender, sendResponse);
      return true;

    case 'EXECUTE_ACTION':
      handleExecuteAction(message, sender, sendResponse);
      return true;

    case 'REQUEST_APPROVAL':
      handleRequestApproval(message, sender, sendResponse);
      return true;

    default:
      sendResponse({ success: false, error: 'Unknown message type' });
  }
});

// Handle context grabbing from content script
async function handleGrabContext(message, sender, sendResponse) {
  try {
    currentContext = {
      url: message.url,
      title: message.title,
      text: message.text,
      timestamp: Date.now()
    };

    chrome.runtime.sendMessage({
      type: 'CONTEXT_GRABBED',
      data: currentContext
    });

    sendResponse({ success: true });
  } catch (error) {
    console.error('[Symbiote] Error grabbing context:', error);
    sendResponse({ success: false, error: error.message });
  }
}

// Handle command from side panel
async function handleSendCommand(message, sender, sendResponse) {
  try {
    if (!claudeApiKey) {
      throw new Error('Claude API key not configured. Please set it in Settings.');
    }

    logAction({
      action: 'command',
      detail: message.command,
      classification: 'safe'
    });

    const result = await sendToClaude(message.command, message.context);

    if (result.actions && result.actions.length > 0) {
      for (const action of result.actions) {
        await processAction(action);
      }
    }

    sendResponse({ success: true, result: result });
  } catch (error) {
    console.error('[Symbiote] Error sending command:', error);
    
    chrome.runtime.sendMessage({
      type: 'ERROR',
      error: error.message
    });

    sendResponse({ success: false, error: error.message });
  }
}

// Send command to Claude API
async function sendToClaude(command, context) {
  const systemPrompt = `You are Symbiote, an AI assistant that helps users automate browser tasks and manage files.

You can execute actions by returning JSON in this format:
{
  "actions": [
    {
      "action": "click",
      "selector": "button.submit-btn",
      "confirm": false
    }
  ],
  "message": "Human-readable response"
}

Available actions:
- click: Click an element (requires selector)
- input: Type into an element (requires selector, text)
- scroll: Scroll the page (requires direction: up/down)
- navigate: Navigate to URL (requires url)
- drive_list: List Google Drive files (requires folderId, optional)
- drive_read: Read file contents (requires fileId)
- drive_create: Create new file (requires name, content, mimeType)

For safe actions (reading, listing), set confirm: false.
For sensitive actions (clicking, creating, deleting), set confirm: true.

Current context: ${context || 'No context provided'}

User command: ${command}`;

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': claudeApiKey,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: 'claude-3-5-sonnet-20241022',
      max_tokens: 4096,
      messages: [
        {
          role: 'user',
          content: systemPrompt
        }
      ]
    })
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(`Claude API error: ${error.error?.message || response.statusText}`);
  }

  const data = await response.json();
  const content = data.content[0].text;

  try {
    const jsonMatch = content.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
  } catch (e) {
    // If not JSON, return as plain message
  }

  return {
    message: content,
    actions: []
  };
}

// Process action through constitutional layer
async function processAction(action) {
  const classification = classifyAction(action);

  logAction({
    action: action.action,
    detail: JSON.stringify(action),
    classification: classification
  });

  if (classification === 'blocked') {
    throw new Error(`Action blocked: ${action.action}`);
  }

  if (classification === 'requires-approval' || action.confirm) {
    const approved = await requestApproval(action);
    if (!approved) {
      throw new Error('Action rejected by user');
    }
  }

  await executeAction(action);
}

// Classify action safety
function classifyAction(action) {
  const safeActions = ['drive_list', 'drive_read', 'scroll'];
  const sensitiveActions = ['click', 'input', 'navigate', 'drive_create'];
  const blockedActions = ['drive_delete', 'execute_script'];

  if (blockedActions.includes(action.action)) {
    return 'blocked';
  }

  if (sensitiveActions.includes(action.action)) {
    return 'requires-approval';
  }

  if (safeActions.includes(action.action)) {
    return 'safe';
  }

  return 'requires-approval';
}

// Request approval from user
async function requestApproval(action) {
  return new Promise((resolve) => {
    const confirmed = confirm(
      `Symbiote wants to perform this action:\n\n` +
      `Action: ${action.action}\n` +
      `Details: ${JSON.stringify(action, null, 2)}\n\n` +
      `Allow this action?`
    );
    resolve(confirmed);
  });
}

// Execute action
async function executeAction(action) {
  switch (action.action) {
    case 'click':
    case 'input':
    case 'scroll':
    case 'navigate':
      await executeContentScriptAction(action);
      break;

    case 'drive_list':
      return await listDriveFiles(action.folderId);

    case 'drive_read':
      return await readDriveFile(action.fileId);

    case 'drive_create':
      return await createDriveFile(action.name, action.content, action.mimeType);

    default:
      throw new Error(`Unknown action: ${action.action}`);
  }
}

// Execute action via content script
async function executeContentScriptAction(action) {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  
  const response = await chrome.tabs.sendMessage(tab.id, {
    type: 'EXECUTE_ACTION',
    action: action
  });

  if (!response.success) {
    throw new Error(response.error);
  }

  return response.result;
}

// Google Drive OAuth
async function handleGoogleAuth(message, sender, sendResponse) {
  try {
    const token = await chrome.identity.getAuthToken({
      interactive: true,
      scopes: [
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/drive.file'
      ]
    });

    googleAuthToken = token.token;
    await chrome.storage.local.set({ googleAuthToken: token.token });

    logAction({
      action: 'auth',
      detail: 'Google Drive authorized',
      classification: 'safe'
    });

    sendResponse({ success: true });
  } catch (error) {
    console.error('[Symbiote] Google auth error:', error);
    sendResponse({ success: false, error: error.message });
  }
}

// Google Drive API: List files
async function listDriveFiles(folderId = 'root') {
  if (!googleAuthToken) {
    throw new Error('Google Drive not authorized');
  }

  const query = folderId === 'root' 
    ? "'root' in parents and trashed=false"
    : `'${folderId}' in parents and trashed=false`;

  const response = await fetch(
    `https://www.googleapis.com/drive/v3/files?q=${encodeURIComponent(query)}&fields=files(id,name,mimeType,modifiedTime)`,
    {
      headers: {
        'Authorization': `Bearer ${googleAuthToken}`
      }
    }
  );

  if (!response.ok) {
    throw new Error(`Drive API error: ${response.statusText}`);
  }

  const data = await response.json();
  
  chrome.runtime.sendMessage({
    type: 'COMMAND_RESULT',
    data: {
      action: 'drive_list',
      content: JSON.stringify(data.files, null, 2)
    }
  });

  return data.files;
}

// Google Drive API: Read file
async function readDriveFile(fileId) {
  if (!googleAuthToken) {
    throw new Error('Google Drive not authorized');
  }

  const response = await fetch(
    `https://www.googleapis.com/drive/v3/files/${fileId}?alt=media`,
    {
      headers: {
        'Authorization': `Bearer ${googleAuthToken}`
      }
    }
  );

  if (!response.ok) {
    throw new Error(`Drive API error: ${response.statusText}`);
  }

  const content = await response.text();
  
  chrome.runtime.sendMessage({
    type: 'COMMAND_RESULT',
    data: {
      action: 'drive_read',
      content: content
    }
  });

  return content;
}

// Google Drive API: Create file
async function createDriveFile(name, content, mimeType = 'text/plain') {
  if (!googleAuthToken) {
    throw new Error('Google Drive not authorized');
  }

  const metadata = {
    name: name,
    mimeType: mimeType
  };

  const boundary = '-------314159265358979323846';
  const delimiter = "\r\n--" + boundary + "\r\n";
  const closeDelimiter = "\r\n--" + boundary + "--";

  const multipartRequestBody =
    delimiter +
    'Content-Type: application/json\r\n\r\n' +
    JSON.stringify(metadata) +
    delimiter +
    'Content-Type: ' + mimeType + '\r\n\r\n' +
    content +
    closeDelimiter;

  const response = await fetch(
    'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart',
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${googleAuthToken}`,
        'Content-Type': 'multipart/related; boundary=' + boundary
      },
      body: multipartRequestBody
    }
  );

  if (!response.ok) {
    throw new Error(`Drive API error: ${response.statusText}`);
  }

  const data = await response.json();
  
  chrome.runtime.sendMessage({
    type: 'COMMAND_RESULT',
    data: {
      action: 'drive_create',
      content: `File created: ${data.name} (ID: ${data.id})`
    }
  });

  return data;
}

// Log action
function logAction(entry) {
  console.log(`[Symbiote] Action: ${entry.action} [${entry.classification}] - ${entry.detail}`);
  
  chrome.runtime.sendMessage({
    type: 'ACTION_LOG',
    data: entry
  });
}

// Handle keyboard commands
chrome.commands.onCommand.addListener(async (command) => {
  if (command === 'grab-context') {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    
    chrome.tabs.sendMessage(tab.id, {
      type: 'GRAB_CONTEXT'
    });
  }
});

console.log('[Symbiote] Background service worker initialized');