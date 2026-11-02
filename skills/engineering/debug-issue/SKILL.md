---
name: debug-issue
description: Reproduce and fix software defects using evidence. Use for errors, regressions, unexpected behavior, or failing tests; container infrastructure diagnosis belongs to docker-debug.
---

# Debug issue

Collect the expected and actual behavior, failing input, relevant revision and environment. Inspect logs without exposing credentials. Reproduce the failure with the smallest practical case; if reproduction is unavailable, state the evidence and uncertainty.

Trace the failure across boundaries. Form a specific hypothesis and choose a check that distinguishes it from alternatives. Change one causal factor at a time; avoid speculative fixes, blanket retries and disabled validation.

Fix the root cause while preserving unrelated behavior and user work. Add a regression check when it captures the failure meaningfully. Run the reproduction and appropriate nearby tests; inspect the diff.

Report root cause, fix and verification. If blocked, give the exact missing evidence and next diagnostic step. Do not call a plausible patch verified without executing a check.
