# Coolship agent skills

Portable, focused [Agent Skills](https://agentskills.io/specification) for engineering and infrastructure work. Each package is self-contained under `skills/<category>/<name>/`; supporting resources load only when needed. The original design inputs remain in `PROMPT.md` and `coolship-deploy-prompt-implementation.md`.

## Install

Use the [skills CLI](https://github.com/vercel-labs/skills) with Node.js 22.20 or later:

```sh
npx skills add coolship-dev/agent-skills --list
npx skills add coolship-dev/agent-skills --skill coolship-deploy -a cursor -a claude-code -a codex
# Add -g for a user-wide installation.
npx skills list
npx skills check
npx skills update
```

Install only the capabilities your project needs. For manual installation, copy an entire leaf package into your agent's skills directory (for example `.agents/skills/coolship-deploy/`). Agents without discovery can read its `SKILL.md` directly. Installation does not grant deployment credentials or authorization.

## Catalog

| Skill | Purpose |
| --- | --- |
| [coolship-deploy](skills/devops/coolship-deploy/SKILL.md) | Deploy and verify applications with Coolship and Coolify |
| [plan-feature](skills/engineering/plan-feature/SKILL.md) | Turn feature requirements into an implementable technical plan |
| [implement-feature](skills/engineering/implement-feature/SKILL.md) | Implement a scoped feature in an existing codebase |
| [debug-issue](skills/engineering/debug-issue/SKILL.md) | Reproduce and fix software defects using evidence |
| [review-code](skills/engineering/review-code/SKILL.md) | Review a code change for actionable correctness, security and regression risks |
| [unslop](skills/engineering/unslop/SKILL.md) | Remove unnecessary complexity and generic filler from code or prose |
| [react-best-practices](skills/web/react-best-practices/SKILL.md) | Improve React application behavior and performance |
| [web-ui-review](skills/web/web-ui-review/SKILL.md) | Review web interfaces for usability, accessibility and responsive behavior |
| [docker-debug](skills/devops/docker-debug/SKILL.md) | Diagnose Docker and Docker Compose failures |
| [proxmox-ops](skills/devops/proxmox-ops/SKILL.md) | Diagnose and maintain Proxmox virtual machines and containers |
| [cloudflare-routing](skills/devops/cloudflare-routing/SKILL.md) | Configure and diagnose Cloudflare DNS, proxy and Tunnel routing |
| [python-project-setup](skills/python/python-project-setup/SKILL.md) | Set up or repair Python project tooling |
| [opencv-development](skills/python/opencv-development/SKILL.md) | Develop and debug OpenCV image or video processing in Python |
| [platformio-workflow](skills/embedded/platformio-workflow/SKILL.md) | Build, test and troubleshoot PlatformIO firmware projects |

## Maintain and validate

See [contributing](docs/contributing.md) and [authoring guidelines](docs/authoring-guidelines.md). Root `AGENTS.md` governs this repository only. CI validates format, local links, templates, evaluation schemas and script syntax; scenario files are manual behavioral checks, not proof of a live deployment.

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-skills.py
python3 -m unittest discover -s tests
```

Deployment examples require an authorized Coolify instance and a compatible Coolship CLI. No live application is deployed by this repository's checks. Private topology belongs in permission-controlled operations configuration.

Licensed under [MIT](LICENSE).
