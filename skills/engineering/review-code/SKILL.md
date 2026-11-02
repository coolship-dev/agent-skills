---
name: review-code
description: Review a code change for actionable correctness, security and regression risks. Use for pull requests, diffs, or requested code reviews.
---

# Review code

Establish the base/head and requested scope. Read project instructions, the diff, callers, contracts and relevant tests. Evaluate changed behavior, including failure paths, permissions, data integrity and compatibility.

Report concrete defects introduced or exposed by the change. For each finding, include severity, a precise file/line location, the triggering conditions, impact and supporting reasoning. Prefer a few substantiated findings over speculative lists. Separate questions from confirmed defects. Avoid style preferences unless they violate an explicit project requirement or obscure a real problem.

Use targeted checks when they help establish a defect; state what was actually run. Do not edit code unless requested. Lead with findings ordered by impact. If none are found, say so and identify material coverage gaps; do not claim the change is risk-free.
