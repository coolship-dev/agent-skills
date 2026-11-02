---
name: coolship-deploy
description: Deploy, redeploy, verify, troubleshoot, and prepare CI for applications on self-hosted Coolify using the project-local Coolship CLI. Use when shipping a web app, API, Dockerfile, Docker Compose service, monorepo target, or preview; configuring coolship.toml, domains, environment variables or health checks; or diagnosing deployment failures. Verify the intended Coolify target, pushed Git revision, authorization and health before claiming success.
---

# Coolship deployment skill

Use this skill to deploy an **application repository** to **self-hosted Coolify** through the **Coolship CLI**, then prove the expected revision is running. It is model-independent: agents with shell access can execute the workflow; an agent without execution tools can propose commands but **must not claim to have deployed**.

Read supporting material as needed:
- [Infrastructure profile](references/infrastructure.md) — target discovery and routing boundaries.
- [CLI reference](references/commands.md) — verified syntax and behavioral limits.
- [Deployment recipes](references/recipes.md) — Dockerfile, Compose, Node, Python, ports, state, routing.
- [CI/CD](references/ci.md) — GitHub Actions and triggering policy.
- [Troubleshooting](references/troubleshooting.md) — diagnostics, retries, recovery.

## Hard rules

1. **Scope:** Use Coolship for app-local operations, not server/team administration. Coolship is not a replacement for the Coolify dashboard or `coolify-cli` administration. Do not SSH into Proxmox or modify host networking as a shortcut to deploy an app.
2. **Source of deployed code:** `coolship deploy` deploys the Git branch **already configured in Coolify**. It does **not** upload the working tree, commit changes, or push Git. A successful deployment can still contain old code: compare local, upstream and server revision.
3. **Authorization:** Before any mutation, identify exact context, project, environment, application/target, server, domain and expected Git commit. Deploy only when requested or explicitly allowed by an existing approved CI workflow. Never autonomously execute `delete`, `stop`, `unlink`, `env push --prune`, `env push --force`, forced domain reassignment or destructive data actions.
4. **Secrets:** Never print, commit, upload into prompts, or log real tokens or production `.env` contents. Do not use `env diff --show-values` or `COOLSHIP_DEBUG_UNREDACTED=1`. Do not enable shell tracing around credentials. Withheld secrets are unknown, not blank.
5. **Uncertain writes:** A timeout may mean the remote deployment is continuing. Inspect history before retrying; do not blindly replay deployment requests.
6. **No server assumptions:** Multiple instances and destinations may exist, with changing availability. Historical account context is only a hint. Use read-only discovery and never silently change context or server.
7. **State:** Protect volumes and databases. Verify mounts/backups before state-affecting changes, and review migrations separately. A container image rollback does not roll back a schema/data migration.
8. **Version check:** Coolship is pre-1.0. Its `main` README may document commands newer than the installed release. Check `coolship --version` and `coolship COMMAND --help` before use.

## Deploy workflow

### Step 0 — inspect the repository (read-only)

```bash
pwd
git status --short
git branch --show-current
git rev-parse HEAD
git remote -v
command -v coolship
coolship --version
coolship --help
```

Read `AGENTS.md`, relevant docs, `coolship.toml`, `.gitignore`, Dockerfile/Compose, package manifests, app port and health endpoint, env **names**, test commands and existing CI. Do not display secret values. Optional read-only helper: `scripts/preflight.sh` in this skill folder.

If no terminal/network authorization is available, stop at a reproducible procedure with explicit unverified items.

### Step 1 — resolve the exact Coolify target

Find `coolship.toml` in the Git repository, or establish one. `[project]` binds a single app; `[apps.NAME]` binds monorepo targets. Resolve:

| Fact | Must verify |
| --- | --- |
| Context | Correct authenticated self-hosted instance, not an accidental default |
| Target | Project, environment and application/monorepo target |
| Server | Actual deployment destination and current health/capacity |
| Source | Repo, Git provider access and configured branch in Coolify |
| Runtime | Build strategy, exposed port/Compose service, persistent mounts and health check |
| Routing | Coolify domain, DNS/tunnel and access policy |
| Permissions | User authorization and least-privilege credentials |

When already linked, inspect:

```bash
coolship config show
coolship doctor
coolship status
coolship domain
coolship deployments -n 5
```

`doctor` can return a failing app-running check before its first deployment; inspect its findings rather than assuming the binding is wrong.

When credentials are missing: run `coolship login` **interactively**, or inject **both** `COOLSHIP_URL` and `COOLSHIP_TOKEN` from a trusted CI secret store. Never hard-code a token in `coolship.toml`, code or example. Select a known context with `--context NAME` when appropriate, but do not combine `--context` with a `COOLSHIP_URL` / `COOLSHIP_TOKEN` pair.

When no binding exists:
- **App already in Coolify:** `coolship link`; choose exact project, environment and application; review `coolship.toml` before commit.
- **New app:** `coolship init`; review detected Git remote, branch, build pack, port, project and server, and ensure creation is within the requested scope. A private repo must have a configured GitHub App or read-only deploy key.
- **Monorepo:** Use named targets and `--target NAME` to eliminate ambiguity.

See [commands](references/commands.md) for supported flags and templates.

### Step 2 — prepare an actual deployable revision

1. Choose a fitting build method: static, Railpack/Nixpacks, Dockerfile or Compose. Ensure reproducible dependencies, container startup, `0.0.0.0` binding and matching internal port.
2. Run project-specific unit/build/lint checks and identify tests not run.
3. Set a useful readiness/health signal, not just an HTTP endpoint that returns a random success. For non-HTTP workers use a process/container or workload-specific check.
4. Document runtime vs build-time environment **variable names**; verify data dependencies, resource limits and backups. Use private storage for app secrets.
5. Ensure the intended Git changes have been **committed and pushed, with authorization**, to the branch Coolify will build. Check local `HEAD`, upstream, repo origin and configured branch. Existing explicit commit/push authorization is sufficient; otherwise ask before publishing.
6. Check whether Coolify auto-deploy on Git push is enabled; do not trigger the exact same revision a second time without need.

### Step 3 — configure remote app carefully

```bash
coolship env diff       # remote comparison, values masked
coolship domain         # read domains
```

Within the user’s authorized configuration scope: `coolship env push` or `coolship domain set ...`. Review **key names** and changes first; `env push --prune` deletes remote-only variables, and `--force` can overwrite withheld secrets. `.env` is local-sensitive material: `env pull` writes it, so use only if necessary and ensure it is ignored by Git. Environment changes generally take effect on the next deployment.

`coolship domain set` changes the **Coolify** domain configuration, **not** DNS, Cloudflare Tunnel, certificates, access policy, or an app's listening port. For stateful changes confirm mounts, backup and restoration plan.

### Step 4 — submit exactly one deployment

After authorization and preflight:

```bash
coolship deploy --timeout 20m
# monorepo example:
coolship deploy --target api --timeout 20m
```

Default waits and watches this deployment UUID. `--no-wait` means only queued, not successfully deployed. `--force` is not the default: use it only to address a specific stale build/cache issue. If submission outcome is uncertain, **inspect `deployments` first**, then the Coolify dashboard; a second POST may duplicate the operation.

### Step 5 — prove deployment + runtime health

```bash
coolship status
coolship deployments -n 5
coolship logs --lines 100
coolship open --print
```

If supported, `coolship logs --service web --lines 100` selects a Compose service (Coolify >=4.4.0 as documented). Independently check the real health endpoint/functional flow from a network that can reach it; verify TLS/domain as appropriate. Confirm:

- Deployment **finished** (not only queued, in progress or timed out).
- App status is actually healthy/running, without relevant startup errors.
- Domain resolves/routes to the intended application; private apps need not have a public URL.
- **Deployed Git SHA/branch** matches the requested revision; use release/version marker when available. A Cloudflare `200` alone does not prove the right commit.
- Runtime dependencies, migrations and persisted data are sound, where relevant.

If a check cannot be performed, mark it as **unverified**. If deployment fails, read [troubleshooting](references/troubleshooting.md) and do not hide uncertainty.

### Step 6 — report concrete evidence

Use this concise output format after an actual deployment:

```text
Target: <context> / <project> / <environment> / <application or target>
Server/domain: <verified destination and address>
Source: <repository> @ <branch> / <expected SHA>
Deployment: <UUID> — <finished|failed|queued|timed out|unknown>
Checks: <tests, health endpoint, logs, TLS, deployed-SHA check>
Data/migrations: <none|checked|unverified>
Changes made: <code, config, env key names, domains>
Risks/next action: <specific, actionable>
```

If only files or commands were prepared, say **Not deployed**.

## Quick commands

```bash
coolship login                    # interactive self-hosted context setup
coolship link                     # bind existing Coolify app
coolship init                     # create and bind new app, asks confirmation
coolship status
coolship deploy
coolship deployments -n 5
coolship logs --lines 100
coolship logs --follow
coolship domain
coolship env diff
coolship open --print
```

Read-only examples above: `status`, `doctor`, `config show`, `deployments`, `logs`, `domain`, `open --print`. `init`, `deploy`, `env push`, `domain set`, `start`, `restart`, `stop`, `cancel`, `delete` are remote mutations. `link` and `unlink` change local binding files.

## Sources, portability and precedence

Source review **2026-11-02**: [Coolship repository](https://github.com/joaomnuno/coolship), [Coolify docs](https://coolify.io/docs/), and [Agent Skills specification](https://agentskills.io/specification). The installed binary's help, repository config, current server state and actual Git revision have priority over any sample or historical account context. This skill requires no ChatGPT memory, hidden tools, model-specific prompt syntax, hard-coded token or private IP. A model unable to execute the workflow must output a runbook and honest verification gaps, never a fabricated deployment result.
