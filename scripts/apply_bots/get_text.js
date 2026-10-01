import WebSocket from 'ws';

async function run() {
  const wsUrl = "ws://127.0.0.1:9222/devtools/page/B1DD4BDB53288B25F5B08FFC6F911D9A";
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
    const res = await send('Runtime.evaluate', {
      expression: `document.body.innerText`,
      returnByValue: true
    });
    console.log(res.result?.value);
    ws.close();
  });
}
run();
