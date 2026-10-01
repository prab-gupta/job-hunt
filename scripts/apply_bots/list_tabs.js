import http from 'http';
http.get('http://127.0.0.1:9222/json', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const targets = JSON.parse(data).filter(t => t.type === 'page');
    targets.forEach(t => console.log(`${t.id} | ${t.url} | ${t.title}`));
  });
});
