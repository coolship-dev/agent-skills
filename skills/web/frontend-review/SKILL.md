---
name: frontend-review
description: Review frontend architecture for duplicated UI primitives, confused state ownership, unnecessary custom code and maintainability risks. Use when assessing React/TypeScript codebase structure, feature boundaries or dependency reuse.
---

# Frontend architecture review

This skill examines architectural maintainability, not a visual design audit. Use the existing `web-ui-review` for UX/accessibility review and `review-code` for correctness/regression findings in a diff, avoiding duplicate reports.

## Gather evidence

1. Read repository instructions, package manifests, component trees, application entry points, routing, API clients, feature modules and tests.
2. Trace representative user journeys and identify owners of data, mutations and UI state.
3. Locate concrete examples with files and lines. Do not infer defects from file length or a framework choice alone.
4. Determine whether an existing component, library or shared utility can replace a custom implementation.

## Examine

- Repeated handcrafted dialogs, dropdowns, tables, form validation and keyboard/focus logic.
- Oversized coordinators and components mixing remote requests, domain rules and presentation.
- Duplicated API state or state synchronization effects and unnecessary global stores.
- Duplicate component families, conflicting UI libraries and dependency bloat.
- Unsafe API boundaries, hand-maintained contract types and unvalidated untrusted data.
- Poor feature boundaries, leaky abstractions and needless indirection.
- Missing tests for important loading, mutation, failure and navigation behavior.

## Recommend proportionate fixes

Prioritize by observed user impact, risk and future maintenance cost. For each finding provide precise locations, supporting evidence, smallest safe remediation, relevant established library/reuse option, trade-offs and a verification plan. A popular dependency is not always better than small local code: justify its benefit.

Clearly distinguish confirmed issues, hypotheses and untested runtime behavior. Preserve what already works. Do not modify code or install packages for a review-only request.

## Output

Provide a focused ordered shortlist with severity, locations, evidence, proposed change and validation criteria. State the tests and browser checks actually performed; don't claim production readiness from static analysis.
