# Curated frontend skills

This catalog offers two original frontend architecture skills and an opt-in installer for selected upstream skills. Upstream content is not duplicated.

## Local Coolship skills

- [frontend-architecture](../skills/web/frontend-architecture/SKILL.md): component design, library selection, state boundaries and incremental refactoring.
- [frontend-review](../skills/web/frontend-review/SKILL.md): evidence-based maintainability and dependency-reuse audits.

Existing skills [react-best-practices](../skills/web/react-best-practices/SKILL.md) and [web-ui-review](../skills/web/web-ui-review/SKILL.md) remain available. Use the appropriate scope rather than requesting all skills on every task.

## Maintainer-owned upstream skills

| Skill | Official source | Focus |
| --- | --- | --- |
| `vercel-react-best-practices` | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) | React data fetching and performance |
| `vercel-composition-patterns` | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns) | React composition and state APIs |
| `web-design-guidelines` | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Web usability/accessibility review |
| `frontend-design` | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Visual layout and typography |
| `playwright-cli` | [Microsoft](https://github.com/microsoft/playwright-cli) | Browser-driven inspections and interactions |

Upstream licenses, compatibility requirements, and updates are maintained by their publishers. Some skills may fetch their latest guidance at execution time, so review external sources before trusting them.

## Install from an application's root

The [Skills CLI](https://github.com/vercel-labs/skills) currently requires Node.js 22.20 or newer.

Install only the Coolship originals:

```sh
npx skills add coolship-dev/agent-skills --skill frontend-architecture --skill frontend-review -a codex -a claude-code -y
```

To install the curated collection, clone this catalog and run the helper **from the consuming project's root**:

```sh
sh /path/to/agent-skills/scripts/install-frontend.sh
# Or choose specific agents:
sh /path/to/agent-skills/scripts/install-frontend.sh codex claude-code
```

Default agents are Codex, Claude Code, Cursor and OpenCode. All installs are project-scoped. The helper invokes the Skills CLI and does not change the application's npm dependencies or add global tools.

The Playwright browser skill is optional. If `playwright-cli` is on the PATH, the helper invokes `playwright-cli install --skills`. Otherwise install it separately using the [official CLI](https://github.com/microsoft/playwright-cli):

```sh
npm install -g @playwright/cli@latest
playwright-cli install --skills
```

Playwright CLI requires an appropriate browser/runtime to execute. Installation of a skill alone does not provide browser access.

For Skills CLI updates:

```sh
npx skills list
npx skills check
npx skills update
```

## Application-owned stack policy

This catalog does not mandate a specific component system. Put concrete choices in the consuming repository's `AGENTS.md`. For example:

```md
Use frontend-architecture for frontend implementation and frontend-review for architecture audits. Check existing packages and reuse established components before writing custom UI primitives.

Approved for this app: React + TypeScript + Vite, Material UI, React Router, TanStack Query/Table, React Hook Form + Zod, Vitest and Playwright.

Require justification for a second UI component system or a new global state manager. Verify type checks and browser workflows before closing UI work.
```

For another app, keep its existing framework (e.g. Next.js) and UI system (e.g. shadcn/ui).

## Validation

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-skills.py
python3 -m unittest discover -s tests
sh -n scripts/install-frontend.sh
```

Installer unit tests use mocked commands and never download packages. A live upstream installation and browser session are separate checks.
