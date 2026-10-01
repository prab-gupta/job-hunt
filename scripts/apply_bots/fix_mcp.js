const http = require('http');
const fs = require('fs');

http.get('http://127.0.0.1:9222/json/version', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    try {
      const json = JSON.parse(data);
      const wsUrl = json.webSocketDebuggerUrl;
      if (!wsUrl) throw new Error("No webSocketDebuggerUrl found");
      
      const pathPart = wsUrl.replace('ws://127.0.0.1:9222', '');
      const content = `9222\n${pathPart}`;
      
      const path1 = '/Users/prab/Library/Application Support/Google/Chrome/DevToolsActivePort';
      const path2 = '/Users/prab/Library/Application Support/Google/Chrome/RemoteProfile/DevToolsActivePort';
      
      fs.writeFileSync(path1, content);
      fs.writeFileSync(path2, content);
      
      console.log("Fixed DevToolsActivePort!");
    } catch (e) {
      console.log("Error:", e.message);
    }
  });
}).on('error', (e) => {
  console.log("HTTP Error:", e.message);
});
