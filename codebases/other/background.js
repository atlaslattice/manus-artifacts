/**
 * Apple Bridge - Background Service Worker
 * Manages WebSocket connection to relay server, clipboard sync,
 * tab sharing, and notification mirroring.
 */

// ─── Configuration ───────────────────────────────────────────────
const DEFAULT_RELAY_URL = 'ws://localhost:3000';
const RECONNECT_INTERVAL = 5000;
const CLIPBOARD_POLL_INTERVAL = 2000;
const HEARTBEAT_INTERVAL = 30000;

let ws = null;
let deviceId = null;
let pairingToken = null;
let lastClipboardContent = '';
let reconnectTimer = null;
let heartbeatTimer = null;
let clipboardPollTimer = null;
let isConnected = false;

// ─── Initialization ──────────────────────────────────────────────
chrome.runtime.onInstalled.addListener(async () => {
  deviceId = await getOrCreateDeviceId();
  await initContextMenus();
  console.log('[AppleBridge] Extension installed. Device ID:', deviceId);
  connectToRelay();
});

chrome.runtime.onStartup.addListener(async () => {
  deviceId = await getOrCreateDeviceId();
  console.log('[AppleBridge] Extension started. Device ID:', deviceId);
  connectToRelay();
});

// ─── Device Identity ─────────────────────────────────────────────
async function getOrCreateDeviceId() {
  const result = await chrome.storage.local.get('deviceId');
  if (result.deviceId) return result.deviceId;
  const id = 'chrome-' + crypto.randomUUID();
  await chrome.storage.local.set({ deviceId: id });
  return id;
}

// ─── WebSocket Connection ────────────────────────────────────────
async function connectToRelay() {
  if (ws && (ws.readyState === WebSocket.OPEN || ws.readyState === WebSocket.CONNECTING)) {
    return;
  }

  const config = await chrome.storage.sync.get({ relayUrl: DEFAULT_RELAY_URL });
  const relayUrl = config.relayUrl;

  try {
    ws = new WebSocket(relayUrl);

    ws.onopen = () => {
      console.log('[AppleBridge] Connected to relay server');
      isConnected = true;
      clearTimeout(reconnectTimer);
      broadcastStatus('connected');

      // Authenticate
      const authPayload = { deviceId, deviceType: 'chrome-extension', name: 'Chrome Browser' };
      const stored = chrome.storage.local.get('pairingToken');
      stored.then(result => {
        if (result.pairingToken) {
          authPayload.token = result.pairingToken;
        }
        sendMessage('auth_request', authPayload);
      });

      // Start heartbeat
      heartbeatTimer = setInterval(() => {
        if (ws && ws.readyState === WebSocket.OPEN) {
          sendMessage('heartbeat', {});
        }
      }, HEARTBEAT_INTERVAL);

      // Start clipboard polling
      startClipboardPolling();
    };

    ws.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        handleMessage(message);
      } catch (err) {
        console.error('[AppleBridge] Failed to parse message:', err);
      }
    };

    ws.onclose = (event) => {
      console.log('[AppleBridge] Disconnected from relay. Code:', event.code);
      isConnected = false;
      cleanup();
      broadcastStatus('disconnected');
      scheduleReconnect();
    };

    ws.onerror = (error) => {
      console.error('[AppleBridge] WebSocket error:', error);
      isConnected = false;
      broadcastStatus('error');
    };
  } catch (err) {
    console.error('[AppleBridge] Connection failed:', err);
    scheduleReconnect();
  }
}

function cleanup() {
  clearInterval(heartbeatTimer);
  clearInterval(clipboardPollTimer);
  heartbeatTimer = null;
  clipboardPollTimer = null;
}

function scheduleReconnect() {
  clearTimeout(reconnectTimer);
  reconnectTimer = setTimeout(() => {
    console.log('[AppleBridge] Attempting reconnection...');
    connectToRelay();
  }, RECONNECT_INTERVAL);
}

function sendMessage(type, payload) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({
      type,
      payload,
      sourceDeviceId: deviceId,
      timestamp: new Date().toISOString()
    }));
  }
}

// ─── Message Handler ─────────────────────────────────────────────
function handleMessage(message) {
  const { type, payload, sourceDeviceId } = message;

  // Ignore messages from self
  if (sourceDeviceId === deviceId) return;

  switch (type) {
    case 'auth_success':
      console.log('[AppleBridge] Authenticated. User:', payload.userId);
      chrome.storage.local.set({ userId: payload.userId, pairingToken: payload.token });
      pairingToken = payload.token;
      broadcastStatus('authenticated');
      break;

    case 'auth_failure':
      console.error('[AppleBridge] Authentication failed:', payload.error);
      broadcastStatus('auth_failed');
      break;

    case 'clipboard_update':
      handleClipboardUpdate(payload);
      break;

    case 'share_tab':
      handleShareTab(payload);
      break;

    case 'push_notification':
      handlePushNotification(payload);
      break;

    case 'device_connected':
      console.log('[AppleBridge] Device connected:', payload.deviceName);
      chrome.notifications.create({
        type: 'basic',
        iconUrl: 'icons/icon128.png',
        title: 'Apple Bridge',
        message: `${payload.deviceName || 'A device'} has connected.`
      });
      broadcastDevices(payload.devices);
      break;

    case 'device_disconnected':
      console.log('[AppleBridge] Device disconnected:', payload.deviceName);
      broadcastDevices(payload.devices);
      break;

    case 'pairing_success':
      console.log('[AppleBridge] Pairing successful!');
      chrome.storage.local.set({ pairingToken: payload.token });
      pairingToken = payload.token;
      chrome.notifications.create({
        type: 'basic',
        iconUrl: 'icons/icon128.png',
        title: 'Apple Bridge',
        message: 'Device paired successfully! Your devices are now linked.'
      });
      break;

    default:
      console.log('[AppleBridge] Unknown message type:', type);
  }
}

// ─── Clipboard Sync ──────────────────────────────────────────────
function startClipboardPolling() {
  clearInterval(clipboardPollTimer);
  clipboardPollTimer = setInterval(async () => {
    try {
      // Use offscreen document to read clipboard
      const clipboardText = await readClipboardViaOffscreen();
      if (clipboardText && clipboardText !== lastClipboardContent) {
        lastClipboardContent = clipboardText;
        sendMessage('clipboard_update', { content: clipboardText });
        console.log('[AppleBridge] Clipboard sent:', clipboardText.substring(0, 50) + '...');
      }
    } catch (err) {
      // Clipboard read may fail silently — that's OK
    }
  }, CLIPBOARD_POLL_INTERVAL);
}

async function readClipboardViaOffscreen() {
  // Request the offscreen document to read clipboard
  try {
    await chrome.offscreen.createDocument({
      url: 'offscreen.html',
      reasons: ['CLIPBOARD'],
      justification: 'Read clipboard for cross-device sync'
    });
  } catch (e) {
    // Document may already exist
  }

  return new Promise((resolve) => {
    chrome.runtime.sendMessage({ action: 'readClipboard' }, (response) => {
      resolve(response?.text || '');
    });
  });
}

async function handleClipboardUpdate(payload) {
  const { content } = payload;
  if (!content || content === lastClipboardContent) return;

  lastClipboardContent = content;

  // Write to clipboard via offscreen document
  try {
    await chrome.offscreen.createDocument({
      url: 'offscreen.html',
      reasons: ['CLIPBOARD'],
      justification: 'Write clipboard for cross-device sync'
    });
  } catch (e) {
    // Document may already exist
  }

  chrome.runtime.sendMessage({ action: 'writeClipboard', text: content });

  // Show notification
  chrome.notifications.create({
    type: 'basic',
    iconUrl: 'icons/icon128.png',
    title: 'Clipboard Synced',
    message: `Received: "${content.substring(0, 80)}${content.length > 80 ? '...' : ''}"`
  });
}

// ─── Tab Sharing ─────────────────────────────────────────────────
function handleShareTab(payload) {
  const { url, title } = payload;
  if (!url) return;

  chrome.tabs.create({ url, active: true });

  chrome.notifications.create({
    type: 'basic',
    iconUrl: 'icons/icon128.png',
    title: 'Tab Received',
    message: `Opened: ${title || url}`
  });
}

// ─── Push Notifications ──────────────────────────────────────────
function handlePushNotification(payload) {
  chrome.notifications.create({
    type: 'basic',
    iconUrl: 'icons/icon128.png',
    title: payload.title || 'Apple Bridge',
    message: payload.body || ''
  });
}

// ─── Context Menu ────────────────────────────────────────────────
async function initContextMenus() {
  chrome.contextMenus.removeAll();

  chrome.contextMenus.create({
    id: 'sendTabToApple',
    title: 'Send this tab to iPhone/Mac',
    contexts: ['page']
  });

  chrome.contextMenus.create({
    id: 'sendLinkToApple',
    title: 'Send this link to iPhone/Mac',
    contexts: ['link']
  });

  chrome.contextMenus.create({
    id: 'sendTextToApple',
    title: 'Copy to iPhone/Mac clipboard',
    contexts: ['selection']
  });
}

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  switch (info.menuItemId) {
    case 'sendTabToApple':
      sendMessage('share_tab', { url: tab.url, title: tab.title });
      chrome.notifications.create({
        type: 'basic',
        iconUrl: 'icons/icon128.png',
        title: 'Tab Sent',
        message: `Sent "${tab.title}" to your Apple devices.`
      });
      break;

    case 'sendLinkToApple':
      sendMessage('share_tab', { url: info.linkUrl, title: info.linkUrl });
      break;

    case 'sendTextToApple':
      sendMessage('clipboard_update', { content: info.selectionText });
      chrome.notifications.create({
        type: 'basic',
        iconUrl: 'icons/icon128.png',
        title: 'Text Sent',
        message: `Sent selected text to your Apple devices.`
      });
      break;
  }
});

// ─── Communication with Popup ────────────────────────────────────
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  switch (request.action) {
    case 'getStatus':
      sendResponse({
        connected: isConnected,
        deviceId,
        pairingToken
      });
      return true;

    case 'shareCurrentTab':
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (tabs[0]) {
          sendMessage('share_tab', { url: tabs[0].url, title: tabs[0].title });
          sendResponse({ success: true });
        }
      });
      return true;

    case 'generatePairingCode':
      generatePairingCode().then(code => sendResponse({ code }));
      return true;

    case 'sendClipboard':
      sendMessage('clipboard_update', { content: request.text });
      sendResponse({ success: true });
      return true;

    case 'reconnect':
      if (ws) ws.close();
      connectToRelay();
      sendResponse({ success: true });
      return true;

    case 'getDevices':
      sendMessage('get_devices', {});
      sendResponse({ success: true });
      return true;
  }
});

async function generatePairingCode() {
  const code = Math.random().toString(36).substring(2, 8).toUpperCase();
  sendMessage('create_pairing', { code });
  return code;
}

// ─── Broadcast to Popup ──────────────────────────────────────────
function broadcastStatus(status) {
  chrome.runtime.sendMessage({ action: 'statusUpdate', status }).catch(() => {});
}

function broadcastDevices(devices) {
  chrome.runtime.sendMessage({ action: 'devicesUpdate', devices }).catch(() => {});
}
