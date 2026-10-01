#!/usr/bin/env node
/**
 * Utility to fetch latest verification codes or application confirmations via Gmail API / Gmail MCP credentials.
 * Usage:
 *   node scripts/check_gmail.js --code
 *   node scripts/check_gmail.js --search "Nebius"
 *   node scripts/check_gmail.js --latest 5
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

// Resolve googleapis from npx cache or local
let google;
try {
  google = require('googleapis').google;
} catch (e) {
  try {
    const npxDir = '/Users/prab/.npm/_npx/148524a34044d269/node_modules/googleapis';
    google = require(npxDir).google;
  } catch (err) {
    console.error('Failed to load googleapis:', err.message);
    process.exit(1);
  }
}

async function getGmailClient() {
  const keysPath = path.join(os.homedir(), '.gmail-mcp', 'gcp-oauth.keys.json');
  const credsPath = path.join(os.homedir(), '.gmail-mcp', 'credentials.json');
  if (!fs.existsSync(keysPath) || !fs.existsSync(credsPath)) {
    throw new Error('Gmail MCP credentials not found in ~/.gmail-mcp/');
  }
  const keys = JSON.parse(fs.readFileSync(keysPath));
  const creds = JSON.parse(fs.readFileSync(credsPath));
  const key = keys.installed || keys.web;
  const oauth2Client = new google.auth.OAuth2(key.client_id, key.client_secret, key.redirect_uris[0]);
  oauth2Client.setCredentials(creds);
  return google.gmail({ version: 'v1', auth: oauth2Client });
}

async function main() {
  const args = process.argv.slice(2);
  const gmail = await getGmailClient();

  if (args.includes('--code')) {
    const res = await gmail.users.messages.list({ userId: 'me', maxResults: 3, q: 'security code OR verification code OR confirmation code' });
    if (!res.data.messages || res.data.messages.length === 0) {
      console.log(JSON.stringify({ found: false, code: null }));
      return;
    }
    const msg = await gmail.users.messages.get({ userId: 'me', id: res.data.messages[0].id });
    const snippet = msg.data.snippet || '';
    let code = null;
    const colonMatch = snippet.match(/:\s*([A-Za-z0-9]{6,8})\b/);
    if (colonMatch) {
      code = colonMatch[1];
    } else {
      const match = snippet.match(/\b([A-Za-z0-9]{6,8})\b/);
      code = match ? match[1] : null;
    }
    console.log(JSON.stringify({
      found: true,
      snippet,
      code,
      messageId: msg.data.id,
      date: msg.data.payload.headers.find(h => h.name === 'Date')?.value
    }, null, 2));
    return;
  }

  const queryIndex = args.indexOf('--search');
  const q = queryIndex !== -1 ? args[queryIndex + 1] : '';
  const limitIndex = args.indexOf('--latest');
  const maxResults = limitIndex !== -1 ? parseInt(args[limitIndex + 1], 10) : 5;

  const res = await gmail.users.messages.list({ userId: 'me', maxResults, q });
  const messages = [];
  for (const m of res.data.messages || []) {
    const msg = await gmail.users.messages.get({ userId: 'me', id: m.id });
    const headers = msg.data.payload.headers;
    messages.push({
      id: msg.data.id,
      from: headers.find(h => h.name === 'From')?.value,
      subject: headers.find(h => h.name === 'Subject')?.value,
      date: headers.find(h => h.name === 'Date')?.value,
      snippet: msg.data.snippet
    });
  }
  console.log(JSON.stringify(messages, null, 2));
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
