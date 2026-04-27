/**
 * Apple Bridge - Popup Script
 * Handles UI interactions and communicates with the background service worker.
 */

// ─── DOM Elements ────────────────────────────────────────────────
const statusDot = document.getElementById('statusDot');
const statusText = document.getElementById('statusText');
const devicesList = document.getElementById('devicesList');
const activityLog = document.getElementById('activityLog');
const shareTabBtn = document.getElementById('shareTabBtn');
const syncClipboardBtn = document.getElementById('syncClipboardBtn');
const qrCodeBtn = document.getElementById('qrCodeBtn');
const pairDeviceBtn = document.getElementById('pairDeviceBtn');
const qrSection = document.getElementById('qrSection');
const closeQrBtn = document.getElementById('closeQrBtn');
const pairingSection = document.getElementById('pairingSection');
const closePairingBtn = document.getElementById('closePairingBtn');
const pairingCodeEl = document.getElementById('pairingCode');
const qrCanvas = document.getElementById('qrCanvas');
const pairingQrCanvas = document.getElementById('pairingQrCanvas');

// ─── State ───────────────────────────────────────────────────────
let activities = [];

// ─── Initialize ──────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  // Get current status from background
  chrome.runtime.sendMessage({ action: 'getStatus' }, (response) => {
    if (response) {
      updateStatus(response.connected ? 'connected' : 'disconnected');
    }
  });

  // Request device list
  chrome.runtime.sendMessage({ action: 'getDevices' });

  // Load activity log from storage
  const stored = await chrome.storage.local.get('activityLog');
  if (stored.activityLog) {
    activities = stored.activityLog;
    renderActivityLog();
  }
});

// ─── Status Updates ──────────────────────────────────────────────
function updateStatus(status) {
  statusDot.className = 'status-dot';

  switch (status) {
    case 'connected':
    case 'authenticated':
      statusDot.classList.add('connected');
      statusText.textContent = 'Connected';
      break;
    case 'disconnected':
      statusText.textContent = 'Disconnected';
      break;
    case 'error':
    case 'auth_failed':
      statusDot.classList.add('error');
      statusText.textContent = 'Error';
      break;
    default:
      statusText.textContent = 'Connecting...';
  }
}

// ─── Listen for Background Messages ──────────────────────────────
chrome.runtime.onMessage.addListener((message) => {
  switch (message.action) {
    case 'statusUpdate':
      updateStatus(message.status);
      break;
    case 'devicesUpdate':
      renderDevices(message.devices || []);
      break;
  }
});

// ─── Device Rendering ────────────────────────────────────────────
function renderDevices(devices) {
  if (!devices || devices.length === 0) {
    devicesList.innerHTML = '<p class="empty-state">No devices paired yet.</p>';
    return;
  }

  devicesList.innerHTML = devices.map(device => {
    const icon = getDeviceIcon(device.deviceType);
    const statusClass = device.online ? 'Online' : 'Offline';
    return `
      <div class="device-item">
        <div class="device-icon">${icon}</div>
        <div class="device-info">
          <div class="device-name">${escapeHtml(device.name || device.deviceType)}</div>
          <div class="device-status">${statusClass}</div>
        </div>
      </div>
    `;
  }).join('');
}

function getDeviceIcon(type) {
  if (!type) return '💻';
  if (type.includes('iphone') || type.includes('ios')) return '📱';
  if (type.includes('ipad')) return '📱';
  if (type.includes('mac')) return '💻';
  if (type.includes('chrome')) return '🌐';
  return '📱';
}

// ─── Action Handlers ─────────────────────────────────────────────

// Share Current Tab
shareTabBtn.addEventListener('click', () => {
  chrome.runtime.sendMessage({ action: 'shareCurrentTab' }, (response) => {
    if (response?.success) {
      addActivity('share', 'Sent current tab to Apple devices');
      showButtonFeedback(shareTabBtn, 'Sent!');
    }
  });
});

// Sync Clipboard
syncClipboardBtn.addEventListener('click', async () => {
  try {
    const text = await navigator.clipboard.readText();
    if (text) {
      chrome.runtime.sendMessage({ action: 'sendClipboard', text }, (response) => {
        if (response?.success) {
          addActivity('clipboard', `Synced clipboard: "${text.substring(0, 40)}..."`);
          showButtonFeedback(syncClipboardBtn, 'Synced!');
        }
      });
    } else {
      showButtonFeedback(syncClipboardBtn, 'Clipboard empty');
    }
  } catch (err) {
    showButtonFeedback(syncClipboardBtn, 'Access denied');
  }
});

// QR Code for Current Tab
qrCodeBtn.addEventListener('click', async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (tab?.url) {
    qrSection.classList.remove('hidden');
    generateQRCode(qrCanvas, tab.url, 200);
    addActivity('qr', `Generated QR code for: ${tab.title}`);
  }
});

closeQrBtn.addEventListener('click', () => {
  qrSection.classList.add('hidden');
});

// Pair Device
pairDeviceBtn.addEventListener('click', () => {
  chrome.runtime.sendMessage({ action: 'generatePairingCode' }, (response) => {
    if (response?.code) {
      pairingSection.classList.remove('hidden');
      pairingCodeEl.textContent = response.code;

      // Generate QR code with pairing URL
      const pairingUrl = `https://apple-bridge.app/pair?code=${response.code}`;
      generateQRCode(pairingQrCanvas, pairingUrl, 160);

      addActivity('pair', 'Generated pairing code');
    }
  });
});

closePairingBtn.addEventListener('click', () => {
  pairingSection.classList.add('hidden');
});

// ─── QR Code Generation ─────────────────────────────────────────
function generateQRCode(canvas, text, size) {
  // Simple QR code generation using canvas
  // This is a lightweight implementation — in production, use a library like qrcode.js
  const ctx = canvas.getContext('2d');
  canvas.width = size;
  canvas.height = size;

  // Clear canvas
  ctx.fillStyle = '#FFFFFF';
  ctx.fillRect(0, 0, size, size);

  // Use the QRCode library if available
  if (typeof QRCode !== 'undefined') {
    // QRCode library handles rendering
    new QRCode(canvas, {
      text: text,
      width: size,
      height: size,
      colorDark: '#1C1C1E',
      colorLight: '#FFFFFF',
      correctLevel: QRCode.CorrectLevel.M
    });
  } else {
    // Fallback: show URL as text
    ctx.fillStyle = '#F2F2F7';
    ctx.fillRect(0, 0, size, size);
    ctx.fillStyle = '#1C1C1E';
    ctx.font = '11px -apple-system, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // Word wrap
    const words = text.split('');
    const charsPerLine = Math.floor(size / 7);
    let y = size / 2 - 20;
    for (let i = 0; i < text.length; i += charsPerLine) {
      ctx.fillText(text.substring(i, i + charsPerLine), size / 2, y);
      y += 16;
    }
  }
}

// ─── Activity Log ────────────────────────────────────────────────
function addActivity(type, text) {
  const icons = {
    share: '🔗',
    clipboard: '📋',
    qr: '📷',
    pair: '🔑',
    notification: '🔔'
  };

  activities.unshift({
    icon: icons[type] || '📌',
    text,
    time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  });

  // Keep only last 20 items
  activities = activities.slice(0, 20);

  // Save to storage
  chrome.storage.local.set({ activityLog: activities });

  renderActivityLog();
}

function renderActivityLog() {
  if (activities.length === 0) {
    activityLog.innerHTML = '<p class="empty-state">No recent activity.</p>';
    return;
  }

  activityLog.innerHTML = activities.map(item => `
    <div class="activity-item">
      <span class="activity-icon">${item.icon}</span>
      <span class="activity-text">${escapeHtml(item.text)}</span>
      <span class="activity-time">${item.time}</span>
    </div>
  `).join('');
}

// ─── Utilities ───────────────────────────────────────────────────
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

function showButtonFeedback(btn, message) {
  const originalText = btn.querySelector('span').textContent;
  btn.querySelector('span').textContent = message;
  btn.style.color = '#34C759';
  setTimeout(() => {
    btn.querySelector('span').textContent = originalText;
    btn.style.color = '';
  }, 1500);
}
