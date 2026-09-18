import hashlib
import os
import tempfile
import unittest
from pathlib import Path

import browser_runner as br


class FakeLocator:
    def __init__(self, page, selector, present=False, text=""):
        self.page, self.selector, self.present, self.text = page, selector, present, text
        self.first = self

    def count(self): return int(self.present)
    def is_visible(self): return self.present
    def fill(self, value): self.page.filled[self.selector] = value
    def set_input_files(self, value): self.page.uploaded = value
    def click(self):
        self.page.clicked = True
        if self.page.click_error: raise RuntimeError(self.page.click_error)
    def inner_text(self): return self.text


class FakePage:
    def __init__(self, fields, success=True, goto_error="", click_error="", redirect_url="",
                 success_before="", success_after="Application received"):
        self.fields, self.success = fields, success
        self.goto_error, self.click_error = goto_error, click_error
        self.redirect_url = redirect_url
        self.success_before, self.success_after = success_before, success_after
        self.url = ""
        self.filled, self.uploaded, self.clicked, self.screenshot_path = {}, "", False, ""

    def goto(self, url, **_kwargs):
        if self.goto_error: raise RuntimeError(self.goto_error)
        self.url = self.redirect_url or url

    def evaluate(self, _script): return self.fields

    def locator(self, selector):
        captcha = "captcha" in selector
        if captcha: return FakeLocator(self, selector, False)
        present = selector in {
            "input[name='first_name']", "input[name='last_name']", "input[type='email']",
            "input[type='file'][name*='resume' i]", "button[type='submit']",
        }
        text = ""
        if self.success and selector == "[data-qa='application-success']":
            text = self.success_after if self.clicked else self.success_before
        present = present or bool(text)
        return FakeLocator(self, selector, present, text)

    def screenshot(self, path, **_kwargs):
        self.screenshot_path = path
        Path(path).write_bytes(b"png")
    def wait_for_timeout(self, _milliseconds): pass


class BrowserRunnerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cv = self.root / "Prabhavit_CV.pdf"
        self.cv.write_bytes(b"unchanged-cv")
        checksum = hashlib.sha256(self.cv.read_bytes()).hexdigest()
        self.manifest = {
            "opportunity_id": 42, "batch_id": "batch-1", "company": "Exact Co",
            "role": "Engineer", "direct_url": "https://jobs.example.test/42",
            "cv_checksum": checksum, "released": True, "state": "CONFIRMED",
            "confirmed_item": {"company": "Exact Co", "role": "Engineer"},
        }
        self.profile = {"first_name": "Prabhavit", "last_name": "Example", "email": "p@example.test"}
        self.fields = [
            {"label": "first name", "required": True, "type": "text"},
            {"label": "last name", "required": True, "type": "text"},
            {"label": "email", "required": True, "type": "email"},
            {"label": "resume", "required": True, "type": "file"},
            {"label": "gender", "required": False, "type": "select"},
        ]

    def tearDown(self): self.tmp.cleanup()

    def test_release_requires_exact_identity_https_and_checksum(self):
        br.validate_release(self.manifest, self.cv)
        for key, value in (("company", "Approx Co"), ("role", "Other Role")):
            bad = dict(self.manifest)
            bad["confirmed_item"] = dict(self.manifest["confirmed_item"], **{key: value})
            with self.assertRaises(br.RunnerRejected): br.validate_release(bad, self.cv)
        bad = dict(self.manifest, direct_url="http://jobs.example.test/42")
        with self.assertRaises(br.RunnerRejected): br.validate_release(bad, self.cv)
        local = dict(self.manifest, direct_url="https://host.containers.internal:8443/form.html")
        br.validate_release(local, self.cv, local_test=True)
        with self.assertRaises(br.RunnerRejected): br.validate_release(self.manifest, self.cv, local_test=True)
        bad = dict(self.manifest, cv_checksum="0" * 64)
        with self.assertRaises(br.RunnerRejected): br.validate_release(bad, self.cv)

    def test_dry_run_fills_and_uploads_without_clicking(self):
        page = FakePage(self.fields)
        out = br.execute_page(page, self.manifest, self.profile, self.cv, self.root, dry_run=True)
        self.assertEqual("DRY_RUN", out.state)
        self.assertFalse(page.clicked)
        self.assertEqual(str(self.cv), page.uploaded)
        self.assertEqual("Prabhavit", page.filled["input[name='first_name']"])

    def test_success_requires_evidence_and_screenshot(self):
        page = FakePage(self.fields)
        out = br.execute_page(page, self.manifest, self.profile, self.cv, self.root)
        self.assertEqual("SUBMITTED", out.state)
        self.assertEqual("Application received", out.evidence)
        self.assertTrue(page.clicked)
        self.assertTrue(out.evidence_path.endswith("42-submitted.png"))
        self.assertEqual(0o700, os.stat(self.root).st_mode & 0o777)
        self.assertEqual(0o600, os.stat(out.evidence_path).st_mode & 0o777)

    def test_rejects_cross_origin_and_private_redirects(self):
        for redirect in (
            "https://evil.example.test/form",
            "https://user:secret@jobs.example.test/42",
            "https://127.0.0.1/form",
        ):
            with self.subTest(redirect=redirect), self.assertRaises(br.RunnerRejected):
                br.execute_page(
                    FakePage(self.fields, redirect_url=redirect), self.manifest,
                    self.profile, self.cv, self.root,
                )

    def test_local_test_allows_only_same_local_origin(self):
        local = dict(self.manifest, direct_url="https://host.containers.internal:8443/form.html")
        page = FakePage(self.fields)
        out = br.execute_page(page, local, self.profile, self.cv, self.root, dry_run=True, local_test=True)
        self.assertEqual("DRY_RUN", out.state)

    def test_preexisting_success_text_is_not_submission_evidence(self):
        page = FakePage(
            self.fields, success_before="Application received",
            success_after="Application received",
        )
        out = br.execute_page(page, self.manifest, self.profile, self.cv, self.root)
        self.assertEqual("NEEDS_REVIEW", out.state)

    def test_unsafe_or_unknown_required_fields_are_rejected(self):
        for label in ("Cover letter", "Why do you want this role?", "Portfolio", "Unknown certification"):
            with self.assertRaises(br.RunnerRejected):
                br.classify_fields([{"label": label, "required": True, "type": "text"}])
        with self.assertRaises(br.RunnerRejected):
            br.classify_fields([{"label": "gender", "required": True, "type": "select"}])

    def test_crash_classification_pre_and_post_click(self):
        before = br.execute_page(FakePage(self.fields, goto_error="offline"), self.manifest, self.profile, self.cv, self.root)
        self.assertEqual("RETRYABLE", before.state)
        after = br.execute_page(FakePage(self.fields, click_error="connection lost"), self.manifest, self.profile, self.cv, self.root)
        self.assertEqual("NEEDS_REVIEW", after.state)
        absent = br.execute_page(FakePage(self.fields, success=False), self.manifest, self.profile, self.cv, self.root)
        self.assertEqual("NEEDS_REVIEW", absent.state)


if __name__ == "__main__":
    unittest.main()
