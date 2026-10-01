const { chromium } = require('playwright');
(async () => {
  try {
    console.log("Connecting...");
    const browser = await chromium.connectOverCDP('http://127.0.0.1:9222', { timeout: 5000 });
    console.log("Connected!");
    await browser.disconnect();
    console.log("Disconnected.");
  } catch (e) {
    console.log("Error:", e.message);
  }
})();
