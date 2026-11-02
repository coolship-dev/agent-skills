# Initial validation — 2026-11-02

The initial catalog contains 14 packages matching the skills named in `PROMPT.md`. Original input documents are preserved at the repository root. Deployment resources were moved from the supplied package into `skills/devops/coolship-deploy/`; account-specific infrastructure and an unsupported historical incident were removed from the portable instructions.

Validation performed:

- Repository validator: metadata, unique names/category layout, package-local Markdown links, shell syntax/executable permissions, YAML/TOML templates and evaluation case structure.
- Eleven automated tests: validator rejection cases plus preflight behavior in temporary Git repositories with a fake Coolship executable. Remote diagnosis failures return nonzero; an unborn repository never contacts Coolship.
- Official `skills-ref validate` checks for the catalog.
- `npx skills add . --list`: all 14 nested packages discovered.
- Isolated installation with `--skill coolship-deploy -a cursor -a claude-code -a codex --yes --copy`: installed entrypoints and references, assets, preflight and evaluation cases were present in the generated agent directories.

CLI examples were checked against the [Coolship README](https://github.com/joaomnuno/coolship/blob/main/README.md); the pinned v0.4.0 module declares Go 1.26. Installed help remains authoritative because main can contain unreleased behavior. Format and installation guidance follow the [Agent Skills specification](https://agentskills.io/specification) and [skills CLI](https://github.com/vercel-labs/skills).

Limits: no live Coolify deployment, real credentials, Cursor/Claude interactive agent session or firmware/hypervisor operation was exercised. Scenario files describe expected agent behavior and have structural validation; they are not automated model evaluations. The deployment CI asset deliberately requires application-owned check/source/release verification hooks before it can deploy.
