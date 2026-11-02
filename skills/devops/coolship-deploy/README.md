# Coolship deployment — portable AI Agent Skill

A [model-independent Agent Skill](https://agentskills.io/specification) for deploying applications through self-hosted [Coolify](https://coolify.io/docs/) with [Coolship CLI](https://github.com/joaomnuno/coolship). Contains no tokens, passwords or private IP addresses.

## Install in an application repository

Copy the **entire** `coolship-deploy/` folder into `.agents/skills/coolship-deploy/` within the app repo. Clients implementing Agent Skills can discover its YAML-frontmatter `SKILL.md` automatically. Other models can read `SKILL.md` directly as Markdown and load referenced files on demand.

To help generic agents that don't auto-discover skills, add to the app's `AGENTS.md` (or equivalent persistent project instructions):

```markdown
## Deployment
For Coolify deployment, CI, environment configuration, domain routing and
production diagnostics, follow `.agents/skills/coolship-deploy/SKILL.md` and
its linked references. Verify intended target and pushed Git revision before
`coolship deploy`; never claim an unexecuted deployment succeeded.
```

For a one-off request to any model: “Read `.agents/skills/coolship-deploy/SKILL.md` and follow it to prepare/deploy this repository to my Coolify.” The agent still needs shell access, network connectivity and explicitly authorized credentials to actually deploy.

## Package contents

- `SKILL.md` — concise safe procedure, verification and required result reporting.
- `references/infrastructure.md` — environment discovery and server-selection cautions.
- `references/commands.md` — Coolship usage and release/version limitations.
- `references/recipes.md` — Dockerfile, Compose, Node/Python, ports, data, networking.
- `references/ci.md` — CI trigger policy and GitHub Actions guidance.
- `references/troubleshooting.md` — diagnostics, recovery, rollback and failure policy.
- `assets/` — project binding, Compose and manual CI examples.
- `scripts/preflight.sh` — read-only Git/CLI remote diagnostics, run from app repo.

Prepared 2026-11-02. The latest tagged Coolship release observed is `v0.4.0`, and upstream `main` also contains unreleased features. Actual CLI help, current Coolify and Git state always override this historical profile.
