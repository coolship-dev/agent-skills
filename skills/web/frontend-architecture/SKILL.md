---
name: frontend-architecture
description: Design, implement and refactor maintainable production React and TypeScript frontends. Use when selecting UI libraries, defining component boundaries, organizing state or replacing unnecessary custom infrastructure.
---

# Frontend architecture

## Inspect first

1. Read the project's AGENTS.md, package manifests, framework version, UI components, API clients and relevant tests.
2. Trace the feature's user journey, data ownership and state transitions before designing changes.
3. Search for existing components and installed dependencies that already provide the required functionality.
4. Honor the project's current design system, framework and routing. Do not introduce competing libraries without a documented deficiency.
5. Consult [the library reference](references/stack.md) only when selecting or comparing dependencies.

## Build clear boundaries

- Keep feature logic, remote data access and visual components separate where it improves comprehension.
- Avoid giant application coordinators, duplicated effects and single-purpose abstraction layers.
- Prefer component composition to extensive boolean props and deeply configurable monoliths.
- Keep render logic pure; derive display values rather than duplicating state.
- Use URL state for navigable selections, a server-state layer for API data, form tooling for form lifecycles and local state for ephemeral interactions.
- Add a shared client store only when state genuinely crosses independent component boundaries. Never mirror server cache into it without a demonstrated need.
- Prefer typed request/response contracts; use OpenAPI code generation when the backend offers a stable schema, and runtime validation where inputs are untrusted.
- Reuse established accessible UI primitives. Do not handcraft dialogs, dropdowns, focus management or advanced tables when an approved dependency fits.

## Evaluate libraries

For each new dependency, consider existing in-project alternatives, maintenance, documentation, licensing, accessibility, security, bundle cost, version compatibility, and the cost of replacing it. Prefer proven packages when they reduce long-term maintenance, but do not add them for trivial functionality.

## Verify

Run applicable type checks, targeted unit/integration tests and browser checks of important workflows. Cover loading, empty, failure, unauthorized and success states where relevant. Verify keyboard/focus behavior and responsive layouts. State which checks were actually run, and distinguish observations from hypotheses.

## Deliver

Describe the existing components reused, new dependencies (if any), state and component boundaries, migration risks and validation results. If the request was for planning or review only, do not edit code.
