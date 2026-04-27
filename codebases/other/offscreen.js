/**
 * Apple Bridge - Offscreen Document
 * Handles clipboard read/write operations that require a DOM context.
 */

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'readClipboard') {
    readClipboard().then(text => sendResponse({ text })).catch(() => sendResponse({ text: '' }));
    return true;
  }

  if (request.action === 'writeClipboard') {
    writeClipboard(request.text).then(() => sendResponse({ success: true })).catch(() => sendResponse({ success: false }));
    return true;
  }
});

async function readClipboard() {
  try {
    const text = await navigator.clipboard.readText();
    return text;
  } catch (err) {
    // Fallback: use execCommand
    const textarea = document.getElementById('clipboard-area');
    textarea.focus();
    document.execCommand('paste');
    const text = textarea.value;
    textarea.value = '';
    return text;
  }
}

async function writeClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
  } catch (err) {
    // Fallback: use execCommand
    const textarea = document.getElementById('clipboard-area');
    textarea.value = text;
    textarea.select();
    document.execCommand('copy');
    textarea.value = '';
  }
}
