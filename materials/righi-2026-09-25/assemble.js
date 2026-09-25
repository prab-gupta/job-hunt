(async () => {
  const el = document.querySelector('#inCVfile0');
  if (!el) return 'NO_INPUT';
  if (!window.__b64 || window.__b64.length < 1000) return 'NO_B64_'+String(window.__b64&&window.__b64.length);
  const bin = atob(window.__b64);
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  const file = new File([bytes], 'Prabhavit_CV_Righi.pdf', { type: 'application/pdf' });
  const dt = new DataTransfer();
  dt.items.add(file);
  el.files = dt.files;
  el.dispatchEvent(new Event('input', { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
  // Telerik/RadUpload often listens to these
  if (window.$find) { try { /* noop */ } catch(e) {} }
  return JSON.stringify({ n: el.files.length, name: el.files[0] && el.files[0].name, size: el.files[0] && el.files[0].size });
})()