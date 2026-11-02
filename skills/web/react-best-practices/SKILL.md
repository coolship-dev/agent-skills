---
name: react-best-practices
description: Improve React application behavior and performance. Use for React component state, rendering, effects, data loading or measured performance issues.
---

# React best practices

Inspect the framework/version, component boundaries, data flow and existing conventions. Use that version's official documentation when API behavior is uncertain. Do not introduce a framework migration as an optimization.

Keep render logic pure and state minimal. Derive values during render where practical; use effects for synchronization with external systems, with cleanup and correct dependencies. Avoid unstable list keys and state mutation. Check asynchronous races, loading/error states and accessible interaction.

For performance work, identify a measured bottleneck with profiling or representative evidence. Examine request waterfalls, bundle cost and repeated rendering before adding memoization. Keep server/client boundaries and hydration behavior consistent with the app's framework.

Verify relevant interactions, tests and build. Report evidence and distinguish measured improvements from hypotheses.
