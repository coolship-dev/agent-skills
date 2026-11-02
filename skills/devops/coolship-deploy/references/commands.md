# Coolship CLI command reference

Sourced from [Coolship upstream README](https://github.com/joaomnuno/coolship/blob/main/README.md), reviewed 2026-11-02. **Version warning:** `main` may be ahead of the tagged `v0.4.0` release. Verify local `coolship --version` and `coolship COMMAND --help`.

## Credentials and context

```bash
coolship login                  # interactive selection: self-hosted/Cloud, URL, context, token
coolship config show           # read resolved binding and credential source without token
# CI ONLY, set through protected secret store:
# COOLSHIP_URL=https://coolify.example.com
# COOLSHIP_TOKEN=<secure value>
```

Coolship uses the official Coolify CLI credential file `~/.config/coolify/config.json` on Linux/macOS. `--coolify-config` overrides that path. The Coolify instance normally needs API Access enabled. Token abilities: `read`, `write` and `deploy` as needed; on newer Coolify, runtime/build logs and secret reads can need `read:sensitive` (actual privileges are server-specific). Never combine an env credential pair with `--context`, and never commit credential files.

## Create/link

```bash
coolship link
coolship link --project "Personal" --environment production --application "api"
coolship init
coolship init --project "Personal" --server "Master Ubuntu" --port 3000 --yes
coolship init --dockerfile deploy/Dockerfile --port 8000 --yes
coolship init --compose-domain web=https://app.example.com --yes
```

`link` changes only local `coolship.toml`. `init` creates and binds a remote application after showing a plan; absent `--deploy`, it does not automatically deploy unless the user accepts an interactive deploy prompt. For private repos, configure access deliberately via `--source github-app --github-app NAME` or `--source deploy-key --deploy-key NAME`. `--yes` skips confirmation, not the need for explicit external authorization.

## Binding schema

Single-app sample:

```toml
version = 1
[project]
context = "YOUR_SAVED_CONTEXT"
project = "YOUR_COOLIFY_PROJECT"
environment = "production"
application = "YOUR_APP"
root = "."
```

Monorepo sample:

```toml
version = 1
[apps.web]
context = "YOUR_SAVED_CONTEXT"
project = "YOUR_COOLIFY_PROJECT"
environment = "production"
application = "frontend"
root = "apps/web"

[apps.api]
context = "YOUR_SAVED_CONTEXT"
project = "YOUR_COOLIFY_PROJECT"
environment = "production"
application = "backend"
root = "apps/api"
```

Use either `[project]` **or** `[apps.*]`, not both. Link targets from their subdirectories (`coolship link --target web`). Commands can take `--target api` or a target name. Commit the credentials-free binding file. `link`/`init` also pin remote resource UUIDs; preserve them if present.

## Inspect / deploy

```bash
coolship doctor                   # inspect linked config, context/server/app; can fail if not running
coolship status
coolship deployments -n 5
coolship deploy --timeout 20m     # wait and watch deployment UUID
coolship deploy --target api --timeout 20m
coolship deploy --no-wait         # QUEUES ONLY; not completion
coolship deploy --force           # rebuild without cache, only for justified issues
coolship logs --lines 100
coolship logs --service web --lines 100  # Compose service; server compatibility needed
coolship open --print
coolship open --dashboard
```

`coolship deploy` uses source/branch configured in Coolify. It **does not** push local commits. Timeouts or Ctrl-C can end local observation without stopping the deployment on the server. Inspect `deployments` before retrying.

## Variables / domains / lifecycle

```bash
coolship env diff                 # safe by default: values masked
coolship env pull                 # writes local .env (sensitive)
coolship env push                 # changes server variables; authorization required
coolship domain                   # read domains
coolship domain set app.example.com  # changes Coolify config, not DNS
coolship preview --pr 42          # only after preview registered in Coolify
coolship restart --yes            # mutating
```

Avoid automatic execution of destructive or risky flags: `env push --prune`, `env push --force`, `domain set --force`, `delete`, `stop`, `unlink`. Coolify can hold separate normal vs preview variable scopes; `--preview` changes which set the env commands affect. Withheld values should remain unknown, not replaced with empty strings. Changes generally take effect at the next deployment.

## Build pack detection in upstream docs

- Compose file in root (`compose.yaml`, `compose.yml`, `docker-compose.yml`, `docker-compose.yaml`) → `dockercompose`, per-service domains; `--port` not used.
- `Dockerfile` → `dockerfile`; check port, health check and actual file path.
- Plain `index.html` without package manifest → `static`, commonly port 80.
- Other source → `railpack` default; Nixpacks also supported; check built-in default port 3000.
- `--static --publish-dir dist` can build and serve static output, if app's actual build matches.

## Output and compatibility

`--format json` is for machine-readable output; inspect fields in the installed CLI before building scripts. Exit codes documented: `0` success; `1` command failed (also env drift with `env diff --exit-code`); `2` invalid input/config; `130` interrupted. Runtime logs for Compose services need compatible Coolify (4.4.0+ per October 2026 upstream verification). A token may lack sensitive-read; withheld logs are **not** empty logs.
