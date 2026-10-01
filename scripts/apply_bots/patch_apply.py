import sys

with open('apply-bot/apply.mjs', 'r') as f:
    code = f.read()

old_func = """async function uploadCV(page) {
  const hidden = page.locator('input[type="file"]').first();
  if (await hidden.count() > 0) {
    await hidden.setInputFiles(P.cvPath);
    await page.waitForTimeout(1200);
    return;
  }
  const chooser = page.waitForEvent('filechooser', { timeout: 8000 });
  const hidden = page.locator('input[type=file]').first();
  await hidden.click({ force: true, timeout: 3000 }).catch(async () => {
    await page.getByRole('button', { name: /upload|choose file|add file|allega/i }).first().click();
  });
  const fc = await chooser;
  await fc.setFiles(P.cvPath);
  await page.waitForTimeout(1200);
}"""

new_func = """async function uploadCV(page) {
  try {
    const fileInput = page.locator('input[type="file"]').first();
    if (await fileInput.count() > 0) {
      await fileInput.setInputFiles(P.cvPath);
      await page.waitForTimeout(1200);
      return;
    }
  } catch (e) {}

  const chooser = page.waitForEvent('filechooser', { timeout: 8000 });
  const trigger = page.getByRole('button', { name: /upload|choose file|add file|allega|attach/i }).first();
  await trigger.click({ force: true, timeout: 3000 });
  const fc = await chooser;
  await fc.setFiles(P.cvPath);
  await page.waitForTimeout(1200);
}"""

code = code.replace(old_func, new_func)

with open('apply-bot/apply.mjs', 'w') as f:
    f.write(code)
