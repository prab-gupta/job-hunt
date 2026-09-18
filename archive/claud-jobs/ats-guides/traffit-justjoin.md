# Traffit and JustJoin runbook

Canonical mechanics: [`../apply-bot/PATTERNS.md`](../apply-bot/PATTERNS.md).

## Fast path

1. On JustJoin, inspect the employer's **Apply** destination before declaring reCAPTCHA blockage.
2. If Apply opens an external Traffit or other ATS form, switch to that ATS workflow.
3. On Traffit, upload the tailored CV and attach or enter the cover letter when offered.
4. For country and city, use the real searchable input: type a partial term, inspect results, click the truthful option.
5. Choose the nearest truthful availability option from the loaded list.
6. Verify all values, selections, consent, and uploaded filename.
7. If JustJoin's guest form raises reCAPTCHA, hand back. Never solve or bypass it.
8. Submit external ATS forms only when unblocked.
9. On Traffit, `/thankyou/` plus the green checkmark can be the only confirmation. Screenshot it even when body text is sparse.
10. Update the tracker with the exact confirmation evidence.

## Known traps

- JustJoin reCAPTCHA does not necessarily apply to an external employer ATS.
- Traffit's underlying `<select>` can be an empty proxy; use the visible autocomplete.
- Confirmation may be visual rather than textual.

