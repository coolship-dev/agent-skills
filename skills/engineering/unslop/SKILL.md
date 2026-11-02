---
name: unslop
description: Remove unnecessary complexity and generic filler from code or prose. Use when asked to simplify, clean up generated output, or make writing more direct while preserving meaning.
---

# Unslop

Determine whether the request concerns code, prose or both, and identify the intended behavior, audience and scope.

For code, inspect callers and tests before removing abstractions. Look for single-use indirection, duplicated logic, dead branches, redundant comments, unnecessary dependencies and error handling that hides failures. Simplify only when behavior and contracts remain clear; keep complexity required by actual use cases. Run relevant checks after behavioral edits.

For prose, preserve facts, uncertainty, citations and the author's intent. Replace vague claims with available specifics, remove repeated conclusions and stock transitions, and use direct sentences. Do not invent details or flatten necessary nuance.

Keep edits scoped and reviewable. Report substantive changes and any checks; avoid broad rewrites when a small correction meets the request.
