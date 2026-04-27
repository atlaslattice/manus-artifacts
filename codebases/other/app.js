/**
 * Apple Bridge - Companion PWA
 * 
 * Progressive Web App for iOS/macOS that communicates with the
 * Chrome extension via the WebSocket relay server.
 */

// ─── Configuration ───────────────────────────────────────────────
const DEFAULT_RELAY_URL = 'ws://localhost:3000';
const RECONNECT_INTERVAL = 5000;
const HEARTBEAT_INTERVAL = 30000;

// ─── State ───────────────────────────────────────────────────────
let ws = null;
let deviceId = null;
let pairingToken = null;
let isConnected = false;
let reconnectTimer = null;
let heartbeatTimer = null;
let receivedTabs = [];
let activities = [];

// ─── DOM Elements ────────────────────────────────────────────────
const statusIndicator = document.getElementById('statusIndicator');
const setupScreen = document.getElementById('setupScreen');
const dashboardScreen = document.getElementById('dashboardScreen');
const pairingInput = document.getElementById('pairingInput');
const pairBtn = document.getElementById('pairBtn');
const scanQrBtn = document.getElementById('scanQrBtn');
const devicesList = document.getElementById('devicesList');
const clipboardText = document.getElementById('clipboardText');
const sendClipboardBtn = document.getElementById('sendClipboardBtn');
const pasteLocalBtn = document.getElementById('pasteLocalBtn');
const receivedClipboard = document.getElementById('receivedClipboard');
const receivedTextEl = document.getElementById('receivedText');
const copyReceivedBtn = document.getElementById('copyReceivedBtn');
const tabUrlInput = document.getElementById('tabUrlInput');
const sendTabBtn = document.getElementById('sendTabBtn');
const receivedTabsEl = document.getElementById('receivedTabs');
const activityLogEl = document.getElementById('activityLog');
const disconnectBtn = document.getElementById('disconnectBtn');
const tabbar = document.getElementById('tabbar');

// ─── Initialization ──────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  deviceId = getOrCreateDeviceId();

  // Check if already paired
  pairingToken = localStorage.getItem('pairingToken');
  if (pairingToken) {
    showDashboard();
    connectToRelay();
  }

  // Load saved data
  loadSavedData();

  // Register service worker for push notifications
  registerServiceWorker();
});

// ─── Device Identity ─────────────────────────────────────────────
function getOrCreateDeviceId() {
  let id = localStorage.getItem('deviceId');
  if (!id) {
    const platform = /iPhone|iPad/.test(navigator.userAgent) ? 'ios' : 'mac';
    id = `${platform}-${crypto.randomUUID()}`;
    localStorage.setItem('deviceId', id);
  }
  return id;
}

function getDeviceName() {
  const ua = navigator.userAgent;
  if (/iPhone/.test(ua)) return 'iPhone';
  if (/iPad/.test(ua)) return 'iPad';
  if (/Mac/.test(ua)) return 'Mac';
  return 'Apple Device';
}

// ─── WebSocket Connection ────────────────────────────────────────
function connectToRelay() {
  if (ws && (ws.readyState === WebSocket.OPEN || ws.readyState === WebSocket.CONNECTING)) {
    return;
  }

  const relayUrl = localStorage.getItem('relayUrl') || DEFAULT_RELAY_URL;

  try {
    ws = new WebSocket(relayUrl);

    ws.onopen = () => {
      console.log('[AppleBridge] Connected to relay');
      isConnected = true;
      updateStatusUI('connected');
      clearTimeout(reconnectTimer);

      // Authenticate or pair
      if (pairingToken) {
        sendMessage('auth_request', {
          deviceId,
          deviceType: getDeviceName().toLowerCase(),
          name: getDeviceName(),
          token: pairingToken
        });
      }

      // Start heartbeat
      heartbeatTimer = setInterval(() => {
        if (ws && ws.readyState === WebSocket.OPEN) {
          sendMessage('heartbeat', {});
        }
      }, HEARTBEAT_INTERVAL);
    };

    ws.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        handleMessage(message);
      } catch (err) {
        console.error('[AppleBridge] Parse error:', err);
      }
    };

    ws.onclose = () => {
      isConnected = false;
      updateStatusUI('disconnected');
      clearInterval(heartbeatTimer);
      scheduleReconnect();
    };

    ws.onerror = () => {
      isConnected = false;
      updateStatusUI('error');
    };
  } catch (err) {
    console.error('[AppleBridge] Connection failed:', err);
    scheduleReconnect();
  }
}

function scheduleReconnect() {
  clearTimeout(reconnectTimer);
  reconnectTimer = setTimeout(() => connectToRelay(), RECONNECT_INTERVAL);
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

  if (sourceDeviceId === deviceId) return;

  switch (type) {
    case 'auth_success':
      pairingToken = payload.token;
      localStorage.setItem('pairingToken', payload.token);
      showDashboard();
      addActivity('auth', 'Connected to relay server');
      break;

    case 'auth_failure':
      alert('Authentication failed: ' + (payload.error || 'Unknown error'));
      updateStatusUI('error');
      break;

    case 'pairing_success':
      pairingToken = payload.token;
      localStorage.setItem('pairingToken', payload.token);
      showDashboard();
      addActivity('pair', 'Successfully paired with Chrome');
      if (payload.devices) renderDevices(payload.devices);
      break;

    case 'clipboard_update':
      handleClipboardReceived(payload);
      break;

    case 'share_tab':
      handleTabReceived(payload);
      break;

    case 'push_notification':
      handleNotification(payload);
      break;

    case 'device_connected':
      addActivity('device', `${payload.deviceName || 'Device'} connected`);
      if (payload.devices) renderDevices(payload.devices);
      break;

    case 'device_disconnected':
      addActivity('device', `${payload.deviceName || 'Device'} disconnected`);
      if (payload.devices) renderDevices(payload.devices);
      break;

    case 'devicesUpdate':
      if (payload.devices) renderDevices(payload.devices);
      break;
  }
}

// ─── Clipboard ───────────────────────────────────────────────────
function handleClipboardReceived(payload) {
  const { content } = payload;
  if (!content) return;

  receivedClipboard.classList.remove('hidden');
  receivedTextEl.textContent = content;
  addActivity('clipboard', `Received: "${content.substring(0, 50)}..."`);

  // Show notification if available
  if ('Notification' in window && Notification.permission === 'granted') {
    new Notification('Clipboard Synced', {
      body: content.substring(0, 100),
      icon: 'icons/icon-192.png'
    });
  }
}

// ─── Tab Sharing ─────────────────────────────────────────────────
function handleTabReceived(payload) {
  const { url, title } = payload;
  if (!url) return;

  receivedTabs.unshift({
    url,
    title: title || url,
    time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  });
  receivedTabs = receivedTabs.slice(0, 20);
  localStorage.setItem('receivedTabs', JSON.stringify(receivedTabs));
  renderReceivedTabs();

  addActivity('tab', `Tab received: ${title || url}`);

  // Show notification
  if ('Notification' in window && Notification.permission === 'granted') {
    new Notification('Tab Received', {
      body: title || url,
      icon: 'icons/icon-192.png',
      data: { url }
    });
  }
}

function handleNotification(payload) {
  if ('Notification' in window && Notification.permission === 'granted') {
    new Notification(payload.title || 'Apple Bridge', {
      body: payload.body || '',
      icon: 'icons/icon-192.png'
    });
  }
  addActivity('notification', payload.title || 'Notification received');
}

// ─── UI Rendering ────────────────────────────────────────────────
function showDashboard() {
  setupScreen.classList.add('hidden');
  dashboardScreen.classList.remove('hidden');
  tabbar.style.display = 'flex';
}

function showSetup() {
  setupScreen.classList.remove('hidden');
  dashboardScreen.classList.add('hidden');
  tabbar.style.display = 'none';
}

function updateStatusUI(status) {
  statusIndicator.className = 'status-indicator';
  if (status === 'connected') statusIndicator.classList.add('connected');
  else if (status === 'error') statusIndicator.classList.add('error');
}

function renderDevices(devices) {
  if (!devices || devices.length === 0) {
    devicesList.innerHTML = '<p class="empty">No devices connected</p>';
    return;
  }

  devicesList.innerHTML = devices.map(d => {
    const icon = d.deviceType?.includes('chrome') ? '🌐' :
                 d.deviceType?.includes('iphone') || d.deviceType?.includes('ios') ? '📱' :
                 d.deviceType?.includes('mac') ? '💻' : '📱';
    const status = d.online ? 'Online' : `Last seen ${d.lastSeen ? new Date(d.lastSeen).toLocaleTimeString() : 'unknown'}`;
    return `
      <div class="device-item">
        <div class="device-icon-circle">${icon}</div>
        <div class="device-info">
          <div class="device-name">${escapeHtml(d.name || d.deviceType || 'Unknown')}</div>
          <div class="device-meta">${status}</div>
        </div>
      </div>
    `;
  }).join('');
}

function renderReceivedTabs() {
  if (receivedTabs.length === 0) {
    receivedTabsEl.innerHTML = '<p class="empty">No tabs received yet</p>';
    return;
  }

  receivedTabsEl.innerHTML = receivedTabs.map(t => `
    <div class="tab-item">
      <a href="${escapeHtml(t.url)}" target="_blank" rel="noopener">${escapeHtml(t.title)}</a>
      <span class="tab-time">${t.time}</span>
    </div>
  `).join('');
}

function addActivity(type, text) {
  const icons = {
    auth: '🔐', pair: '🔑', clipboard: '📋', tab: '🔗',
    device: '📱', notification: '🔔', send: '📤'
  };

  activities.unshift({
    icon: icons[type] || '📌',
    text,
    time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  });
  activities = activities.slice(0, 30);
  localStorage.setItem('activities', JSON.stringify(activities));
  renderActivityLog();
}

function renderActivityLog() {
  if (activities.length === 0) {
    activityLogEl.innerHTML = '<p class="empty">No recent activity</p>';
    return;
  }

  activityLogEl.innerHTML = activities.slice(0, 10).map(a => `
    <div class="activity-item">
      <span class="icon">${a.icon}</span>
      <span class="text">${escapeHtml(a.text)}</span>
      <span class="time">${a.time}</span>
    </div>
  `).join('');
}

// ─── Event Handlers ──────────────────────────────────────────────

// Pairing
pairBtn.addEventListener('click', () => {
  const code = pairingInput.value.trim().toUpperCase();
  if (code.length < 4) {
    alert('Please enter a valid pairing code.');
    return;
  }

  connectToRelay();

  // Wait for connection, then send pairing request
  const waitForConnection = setInterval(() => {
    if (ws && ws.readyState === WebSocket.OPEN) {
      clearInterval(waitForConnection);
      sendMessage('join_pairing', {
        code,
        deviceId,
        deviceType: getDeviceName().toLowerCase(),
        name: getDeviceName()
      });
    }
  }, 200);

  // Timeout after 10 seconds
  setTimeout(() => clearInterval(waitForConnection), 10000);
});

pairingInput.addEventListener('input', (e) => {
  e.target.value = e.target.value.toUpperCase().replace(/[^A-Z0-9]/g, '');
});

// QR Scan (placeholder — would need native camera API or a library)
scanQrBtn.addEventListener('click', () => {
  alert('QR scanning requires camera access. On iOS, you can use the built-in Camera app to scan QR codes from the Chrome extension.');
});

// Send Clipboard
sendClipboardBtn.addEventListener('click', () => {
  const text = clipboardText.value.trim();
  if (!text) {
    alert('Please enter or paste some text first.');
    return;
  }
  sendMessage('clipboard_update', { content: text });
  addActivity('send', `Sent clipboard: "${text.substring(0, 40)}..."`);
  showFeedback(sendClipboardBtn, 'Sent!');
});

// Paste from local clipboard
pasteLocalBtn.addEventListener('click', async () => {
  try {
    const text = await navigator.clipboard.readText();
    clipboardText.value = text;
  } catch (err) {
    alert('Clipboard access requires a user gesture and HTTPS. Please paste manually.');
  }
});

// Copy received clipboard
copyReceivedBtn.addEventListener('click', async () => {
  const text = receivedTextEl.textContent;
  try {
    await navigator.clipboard.writeText(text);
    showFeedback(copyReceivedBtn, 'Copied!');
  } catch (err) {
    // Fallback
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    showFeedback(copyReceivedBtn, 'Copied!');
  }
});

// Send Tab
sendTabBtn.addEventListener('click', () => {
  const url = tabUrlInput.value.trim();
  if (!url) {
    alert('Please enter a URL.');
    return;
  }
  sendMessage('share_tab', { url, title: url });
  addActivity('send', `Sent tab: ${url}`);
  tabUrlInput.value = '';
  showFeedback(sendTabBtn, 'Sent!');
});

// Disconnect
disconnectBtn.addEventListener('click', () => {
  if (confirm('Disconnect from all devices? You will need to pair again.')) {
    localStorage.removeItem('pairingToken');
    localStorage.removeItem('receivedTabs');
    localStorage.removeItem('activities');
    pairingToken = null;
    if (ws) ws.close();
    showSetup();
  }
});

// Tab bar navigation (simplified — scrolls to sections)
tabbar.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    tabbar.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    // Could implement full tab switching here
  });
});

// ─── Service Worker Registration ─────────────────────────────────
async function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    try {
      const registration = await navigator.serviceWorker.register('sw.js');
      console.log('[SW] Registered:', registration.scope);

      // Request notification permission
      if ('Notification' in window && Notification.permission === 'default') {
        const permission = await Notification.requestPermission();
        console.log('[Notifications] Permission:', permission);
      }
    } catch (err) {
      console.error('[SW] Registration failed:', err);
    }
  }
}

// ─── Utilities ───────────────────────────────────────────────────
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

function showFeedback(btn, message) {
  const original = btn.textContent;
  btn.textContent = message;
  btn.style.background = '#34C759';
  setTimeout(() => {
    btn.textContent = original;
    btn.style.background = '';
  }, 1500);
}

function loadSavedData() {
  try {
    const savedTabs = JSON.parse(localStorage.getItem('receivedTabs') || '[]');
    receivedTabs = savedTabs;
    renderReceivedTabs();

    const savedActivities = JSON.parse(localStorage.getItem('activities') || '[]');
    activities = savedActivities;
    renderActivityLog();
  } catch (e) {
    console.error('Failed to load saved data:', e);
  }
}
