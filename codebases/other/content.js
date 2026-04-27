/**
 * Apple Bridge - Content Script
 * Listens for clipboard copy events on web pages and forwards them
 * to the background service worker for cross-device sync.
 */

document.addEventListener('copy', () => {
  setTimeout(async () => {
    try {
      const text = await navigator.clipboard.readText();
      if (text) {
        chrome.runtime.sendMessage({
          action: 'sendClipboard',
          text: text
        });
      }
    } catch (err) {
      // Clipboard access may be denied on some pages — fail silently
    }
  }, 100);
});

// Listen for incoming clipboard writes from the extension
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'pasteFromDevice') {
    navigator.clipboard.writeText(request.text).then(() => {
      sendResponse({ success: true });
    }).catch(() => {
      sendResponse({ success: false });
    });
    return true;
  }
});
