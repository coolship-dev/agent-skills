# React/TypeScript library selection

These are widely used options to evaluate, **not mandatory dependencies**. Before proposing a package inspect the app's established stack and ask whether existing code already solves the requirement.

| Concern | Candidate | When appropriate | Avoid |
| --- | --- | --- | --- |
| UI component package | Material UI | Complete, actively maintained component suite | Combining with another full UI system |
| Source-owned UI components | shadcn/ui + Radix UI | High customization with maintainable accessible primitives | Treating copied components as maintenance-free |
| Styling | Tailwind CSS | Already used or intentionally selected for a new app | Mixing unnecessary styling paradigms |
| Routing | React Router | Standalone client React apps | Replacing framework-native routing |
| Server data | TanStack Query | Caching, invalidation, mutations, stale/request states | Mirroring cached data into global state |
| Tables | TanStack Table | Complex sorting, filtering and selection | Adding it for a static simple table |
| Virtualization | TanStack Virtual | Proven high row/column count or measured performance problem | Premature optimization |
| Forms | React Hook Form + Zod | Field lifecycle and typed user-facing validation | Treating client validation as a security boundary |
| Shared client state | Zustand | Shared ephemeral UI state that cannot stay local | Using it as a second server cache |
| Icons | Lucide | No established icon system yet | Introducing competing icon packages |
| Component examples | Storybook | Shared component library, visual review or design system | Mandatory setup for a tiny UI |
| Unit tests | Vitest | Vite/TypeScript-based frontend tests | Replacing existing suitable test tooling |
| Browser tests | Playwright | Critical user journeys, interactions and regressions | Asserting production readiness from isolated tests |
| OpenAPI types | openapi-typescript or Hey API | Backend publishes a supported OpenAPI schema | Multiple conflicting handwritten client contracts |
| Interactive nodes | React Flow | Actual graph/node editing UX | Diagram library for ordinary forms/layouts |
| Canvas annotation | react-konva | High interaction demands on image overlays | Ignoring simpler SVG/DOM alternatives |

## Decision procedure

1. Reuse an approved, suitable dependency already installed.
2. Otherwise compare maintained options, including a no-new-dependency approach.
3. Prefer one component system (for example **Material UI OR shadcn/ui**, not both by default).
4. Match state ownership to what it represents: server, URL, form, local or genuinely shared client state.
5. Verify current upstream APIs and compatibility before importing code patterns.
6. Include accessibility, type checking and browser behavior in completion criteria.

## Project-level policy example

The consuming project's own `AGENTS.md` can specify an actual stack:

> Follow frontend-architecture when adding or refactoring React features. Reuse approved components and check the dependency manifest before creating custom primitives. Keep server data, URL state, form state and UI state distinct. Document any new framework or overlapping library. Verify type checks and critical browser flows.

This central skill must never impose a specific stack on unrelated projects.
