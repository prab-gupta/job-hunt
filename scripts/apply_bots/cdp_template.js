import http from 'http';
import WebSocket from 'ws';

function getWebSocketUrl() {
  return new Promise((resolve, reject) => {
    http.get('http://127.0.0.1:9222/json', (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const targets = JSON.parse(data);
          const page = targets.find(t => t.type === 'page' && !t.url.startsWith('devtools://'));
          if (page) resolve(page.webSocketDebuggerUrl);
          else reject(new Error("No page found"));
        } catch(e) { reject(e); }
      });
    }).on('error', reject);
  });
}

async function run() {
  try {
    const wsUrl = await getWebSocketUrl();
    const ws = new WebSocket(wsUrl);
    
    let msgId = 1;
    const callbacks = new Map();
    
    ws.on('message', data => {
      const msg = JSON.parse(data);
      if (msg.id && callbacks.has(msg.id)) {
        callbacks.get(msg.id)(msg.result);
        callbacks.delete(msg.id);
      }
      if (msg.method === 'Runtime.consoleAPICalled') {
        const text = msg.params.args.map(a => a.value).join(' ');
        console.log('BROWSER CONSOLE:', text);
      }
    });

    const send = (method, params = {}) => new Promise(resolve => {
      const id = msgId++;
      callbacks.set(id, resolve);
      ws.send(JSON.stringify({ id, method, params }));
    });

    ws.on('open', async () => {
      await send('Runtime.enable');
      await send('Page.enable');
      
      console.log('Navigating...');
      await send('Page.navigate', { url: process.argv[2] });
      
      // Wait a bit for load
      await new Promise(r => setTimeout(r, 5000));
      
      const res = await send('Runtime.evaluate', {
        expression: `document.title`,
        returnByValue: true
      });
      console.log('Title:', res.result?.value);
      
      ws.close();
    });
  } catch (err) {
    console.error(err);
  }
}
run();
