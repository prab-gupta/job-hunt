import http from 'http';
import WebSocket from 'ws';

async function run() {
  const wsUrl = "ws://127.0.0.1:9222/devtools/page/0C823CCD8BEC63694B4249C005278D4D";
  const ws = new WebSocket(wsUrl);
  let msgId = 1;
  const callbacks = new Map();
  ws.on('message', data => {
    const msg = JSON.parse(data);
    if (msg.id && callbacks.has(msg.id)) { callbacks.get(msg.id)(msg.result); callbacks.delete(msg.id); }
  });
  const send = (method, params = {}) => new Promise(resolve => {
    const id = msgId++; callbacks.set(id, resolve); ws.send(JSON.stringify({ id, method, params }));
  });
  ws.on('open', async () => {
    await send('Runtime.enable');
    await send('Page.enable');
    // Navigate to Google without signing in
    await send('Page.navigate', { url: "https://html.duckduckgo.com/html/?q=site:msd.wd5.myworkdayjobs.com+R416895" });
    await new Promise(r => setTimeout(r, 3000));
    const res = await send('Runtime.evaluate', {
      expression: `
        Array.from(document.querySelectorAll('a.result__url')).map(a => a.href)[0]
      `,
      returnByValue: true
    });
    console.log("Found URL:", res.result?.value);
    ws.close();
  });
}
run();
