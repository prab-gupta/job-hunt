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
    await send('Page.navigate', { url: "https://www.google.com/search?q=site:msd.wd5.myworkdayjobs.com+R416895" });
    await new Promise(r => setTimeout(r, 3000));
    const res = await send('Runtime.evaluate', {
      expression: `
        const links = Array.from(document.querySelectorAll('a'));
        links.map(l => l.href).find(h => h.includes('myworkdayjobs.com'))
      `,
      returnByValue: true
    });
    console.log("Workday URL:", res.result?.value);
    ws.close();
  });
}
run();
