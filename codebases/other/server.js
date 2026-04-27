/**
 * Apple Bridge - WebSocket Relay Server
 * 
 * A lightweight relay server that brokers real-time communication
 * between Chrome extensions and companion PWAs on Apple devices.
 * 
 * Features:
 * - Device pairing via short codes
 * - Message relay between paired devices
 * - Presence tracking (online/offline)
 * - Automatic cleanup of stale connections
 */

import { WebSocketServer, WebSocket } from 'ws';
import { randomUUID } from 'crypto';
import http from 'http';

// ─── Configuration ───────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
const HEARTBEAT_TIMEOUT = 45000;     // 45 seconds
const PAIRING_CODE_TTL = 300000;     // 5 minutes
const CLEANUP_INTERVAL = 60000;      // 1 minute

// ─── In-Memory Data Store ────────────────────────────────────────
// In production, replace with Redis or a database.
const users = new Map();          // userId -> { token, devices: Map<deviceId, deviceInfo> }
const connections = new Map();    // ws -> { userId, deviceId, deviceType, name, alive }
const pairingCodes = new Map();   // code -> { userId, createdAt }

// ─── HTTP Server (for health checks and PWA serving) ─────────────
const httpServer = http.createServer((req, res) => {
  // CORS headers for PWA
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'ok',
      connections: connections.size,
      users: users.size,
      uptime: process.uptime()
    }));
    return;
  }

  if (req.url === '/api/pair/validate' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      try {
        const { code } = JSON.parse(body);
        const pairing = pairingCodes.get(code);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ valid: !!pairing }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid request' }));
      }
    });
    return;
  }

  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Apple Bridge Relay Server v1.0.0');
});

// ─── WebSocket Server ────────────────────────────────────────────
const wss = new WebSocketServer({ server: httpServer });

wss.on('connection', (ws, req) => {
  const clientIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
  console.log(`[Connect] New client from ${clientIp}`);

  // Initialize connection metadata
  connections.set(ws, { userId: null, deviceId: null, deviceType: null, name: null, alive: true });

  ws.on('message', (data) => {
    try {
      const message = JSON.parse(data.toString());
      handleMessage(ws, message);
    } catch (err) {
      console.error('[Error] Failed to parse message:', err.message);
      sendToClient(ws, 'error', { error: 'Invalid message format' });
    }
  });

  ws.on('close', () => {
    handleDisconnect(ws);
  });

  ws.on('pong', () => {
    const conn = connections.get(ws);
    if (conn) conn.alive = true;
  });
});

// ─── Message Router ──────────────────────────────────────────────
function handleMessage(ws, message) {
  const { type, payload, sourceDeviceId, timestamp } = message;

  switch (type) {
    case 'auth_request':
      handleAuth(ws, payload);
      break;

    case 'create_pairing':
      handleCreatePairing(ws, payload);
      break;

    case 'join_pairing':
      handleJoinPairing(ws, payload);
      break;

    case 'clipboard_update':
    case 'share_tab':
    case 'push_notification':
      relayToUserDevices(ws, message);
      break;

    case 'get_devices':
      handleGetDevices(ws);
      break;

    case 'heartbeat':
      const conn = connections.get(ws);
      if (conn) conn.alive = true;
      break;

    default:
      console.log(`[Warn] Unknown message type: ${type}`);
  }
}

// ─── Authentication ──────────────────────────────────────────────
function handleAuth(ws, payload) {
  const { deviceId, deviceType, name, token } = payload;

  let userId;

  if (token) {
    // Returning user — find by token
    for (const [uid, user] of users) {
      if (user.token === token) {
        userId = uid;
        break;
      }
    }
  }

  if (!userId) {
    // New user — create account
    userId = randomUUID();
    const newToken = randomUUID();
    users.set(userId, {
      token: newToken,
      devices: new Map()
    });

    // Update connection
    const conn = connections.get(ws);
    conn.userId = userId;
    conn.deviceId = deviceId;
    conn.deviceType = deviceType;
    conn.name = name;

    // Register device
    users.get(userId).devices.set(deviceId, {
      deviceType,
      name,
      online: true,
      lastSeen: new Date().toISOString()
    });

    sendToClient(ws, 'auth_success', {
      userId,
      token: users.get(userId).token,
      isNew: true
    });

    console.log(`[Auth] New user ${userId} with device ${deviceId}`);
    return;
  }

  // Existing user
  const user = users.get(userId);
  const conn = connections.get(ws);
  conn.userId = userId;
  conn.deviceId = deviceId;
  conn.deviceType = deviceType;
  conn.name = name;

  // Register/update device
  user.devices.set(deviceId, {
    deviceType,
    name,
    online: true,
    lastSeen: new Date().toISOString()
  });

  sendToClient(ws, 'auth_success', {
    userId,
    token: user.token,
    isNew: false
  });

  // Notify other devices
  broadcastToUser(userId, 'device_connected', {
    deviceId,
    deviceName: name || deviceType,
    devices: getDeviceList(userId)
  }, deviceId);

  console.log(`[Auth] Returning user ${userId}, device ${deviceId}`);
}

// ─── Device Pairing ──────────────────────────────────────────────
function handleCreatePairing(ws, payload) {
  const { code } = payload;
  const conn = connections.get(ws);

  if (!conn || !conn.userId) {
    sendToClient(ws, 'error', { error: 'Not authenticated' });
    return;
  }

  // Store pairing code
  pairingCodes.set(code, {
    userId: conn.userId,
    createdAt: Date.now()
  });

  console.log(`[Pairing] Code ${code} created for user ${conn.userId}`);
  sendToClient(ws, 'pairing_created', { code, expiresIn: PAIRING_CODE_TTL / 1000 });
}

function handleJoinPairing(ws, payload) {
  const { code, deviceId, deviceType, name } = payload;

  const pairing = pairingCodes.get(code);
  if (!pairing) {
    sendToClient(ws, 'auth_failure', { error: 'Invalid or expired pairing code' });
    return;
  }

  // Check expiry
  if (Date.now() - pairing.createdAt > PAIRING_CODE_TTL) {
    pairingCodes.delete(code);
    sendToClient(ws, 'auth_failure', { error: 'Pairing code has expired' });
    return;
  }

  const userId = pairing.userId;
  const user = users.get(userId);

  if (!user) {
    sendToClient(ws, 'auth_failure', { error: 'User not found' });
    return;
  }

  // Register the new device
  const conn = connections.get(ws);
  conn.userId = userId;
  conn.deviceId = deviceId;
  conn.deviceType = deviceType;
  conn.name = name;

  user.devices.set(deviceId, {
    deviceType,
    name,
    online: true,
    lastSeen: new Date().toISOString()
  });

  // Clean up pairing code
  pairingCodes.delete(code);

  // Send success to the new device
  sendToClient(ws, 'pairing_success', {
    userId,
    token: user.token,
    devices: getDeviceList(userId)
  });

  // Notify all other devices
  broadcastToUser(userId, 'device_connected', {
    deviceId,
    deviceName: name || deviceType,
    devices: getDeviceList(userId)
  }, deviceId);

  console.log(`[Pairing] Device ${deviceId} joined user ${userId} via code ${code}`);
}

// ─── Message Relay ───────────────────────────────────────────────
function relayToUserDevices(senderWs, message) {
  const conn = connections.get(senderWs);
  if (!conn || !conn.userId) {
    sendToClient(senderWs, 'error', { error: 'Not authenticated' });
    return;
  }

  const { type, payload, sourceDeviceId, timestamp } = message;

  // Forward to all other devices of this user
  for (const [clientWs, clientConn] of connections) {
    if (
      clientWs !== senderWs &&
      clientConn.userId === conn.userId &&
      clientWs.readyState === WebSocket.OPEN
    ) {
      clientWs.send(JSON.stringify({
        type,
        payload,
        sourceDeviceId: conn.deviceId,
        timestamp: timestamp || new Date().toISOString()
      }));
    }
  }

  console.log(`[Relay] ${type} from ${conn.deviceId} to user ${conn.userId}'s devices`);
}

// ─── Device List ─────────────────────────────────────────────────
function handleGetDevices(ws) {
  const conn = connections.get(ws);
  if (!conn || !conn.userId) return;

  sendToClient(ws, 'devicesUpdate', {
    devices: getDeviceList(conn.userId)
  });
}

function getDeviceList(userId) {
  const user = users.get(userId);
  if (!user) return [];

  return Array.from(user.devices.entries()).map(([id, info]) => ({
    deviceId: id,
    ...info
  }));
}

// ─── Disconnect Handling ─────────────────────────────────────────
function handleDisconnect(ws) {
  const conn = connections.get(ws);
  if (conn && conn.userId && conn.deviceId) {
    const user = users.get(conn.userId);
    if (user) {
      const device = user.devices.get(conn.deviceId);
      if (device) {
        device.online = false;
        device.lastSeen = new Date().toISOString();
      }

      // Notify other devices
      broadcastToUser(conn.userId, 'device_disconnected', {
        deviceId: conn.deviceId,
        deviceName: conn.name || conn.deviceType,
        devices: getDeviceList(conn.userId)
      }, conn.deviceId);
    }

    console.log(`[Disconnect] Device ${conn.deviceId} (user ${conn.userId})`);
  }

  connections.delete(ws);
}

// ─── Utility Functions ───────────────────────────────────────────
function sendToClient(ws, type, payload) {
  if (ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type, payload, timestamp: new Date().toISOString() }));
  }
}

function broadcastToUser(userId, type, payload, excludeDeviceId = null) {
  for (const [clientWs, clientConn] of connections) {
    if (
      clientConn.userId === userId &&
      clientConn.deviceId !== excludeDeviceId &&
      clientWs.readyState === WebSocket.OPEN
    ) {
      sendToClient(clientWs, type, payload);
    }
  }
}

// ─── Heartbeat & Cleanup ─────────────────────────────────────────
const heartbeatInterval = setInterval(() => {
  wss.clients.forEach((ws) => {
    const conn = connections.get(ws);
    if (conn && !conn.alive) {
      console.log(`[Heartbeat] Terminating stale connection: ${conn.deviceId}`);
      ws.terminate();
      return;
    }
    if (conn) conn.alive = false;
    ws.ping();
  });
}, HEARTBEAT_TIMEOUT);

// Clean up expired pairing codes
const cleanupInterval = setInterval(() => {
  const now = Date.now();
  for (const [code, pairing] of pairingCodes) {
    if (now - pairing.createdAt > PAIRING_CODE_TTL) {
      pairingCodes.delete(code);
      console.log(`[Cleanup] Expired pairing code: ${code}`);
    }
  }
}, CLEANUP_INTERVAL);

wss.on('close', () => {
  clearInterval(heartbeatInterval);
  clearInterval(cleanupInterval);
});

// ─── Start Server ────────────────────────────────────────────────
httpServer.listen(PORT, () => {
  console.log(`
╔══════════════════════════════════════════════════╗
║          Apple Bridge Relay Server v1.0          ║
╠══════════════════════════════════════════════════╣
║  HTTP:      http://localhost:${PORT}               ║
║  WebSocket: ws://localhost:${PORT}                 ║
║  Health:    http://localhost:${PORT}/health         ║
╚══════════════════════════════════════════════════╝
  `);
});
