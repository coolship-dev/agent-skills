# Troubleshooting and recovery

First inspect without mutation:

```bash
coolship --version
coolship config show
coolship doctor
coolship status
coolship deployments -n 10
coolship logs --lines 100
coolship open --dashboard
```

Preserve deployment UUID and timestamps. Never paste secrets into bug reports.

| Symptom | Possible cause | Safe response |
| --- | --- | --- |
| Unknown context / missing credentials | `~/.config/coolify/config.json`, env pair missing, wrong default | Select intended context or perform supervised login |
| API disabled, 401/403, IP denial | Coolify API access, token, team rights, allowlist | Correct permissions/access through operator; no privileged host SSH fallback |
| TLS/DNS/timeout | Wrong panel URL, inaccessible network/tunnel, host outage | Check network and certs; never disable TLS validation reflexively |
| Wrong app | Stale or ambiguous `coolship.toml`, wrong context/target | Read binding and IDs, explicitly relink only after review |
| Build failed | Wrong Git branch, Docker context, lockfile, build-time variables | Fix reproducible source, push authorized commit and deploy once |
| Deployed old revision | Local changes unpushed, wrong Coolify branch, auto-deploy race | Identify actual server SHA; do not force deploy blindly |
| Deployment timeout | Server may still be running operation | Check deployments and dashboard before any retry |
| Unhealthy app | Listener address/port, readiness check, dependencies, crashes | Inspect runtime logs and health config; deploy correction after tests |
| Logs unavailable | `read:sensitive` permission or stopped container | Obtain scoped access / read dashboard; lack of logs != success |
| Compose logs wrong | Wrong service name or unsupported Coolify | Select exact service on Coolify 4.4.0+ |
| 404/502 over domain | Proxy route, app port, DNS, Tunnel | Verify all routing layers independently |
| Database data appears missing | Volume name changed, mounts or migration | Halt destructive changes, verify backups and volumes |

## Rollback

The checked Coolship command reference documents `deployments`, `cancel`, `restart`, and `deploy`; do **not** invent `coolship rollback`. Coolify itself supports image rollback from retained images in its application operations UI. A safe rollback requires ensuring compatibility with current environment, volumes and schema. Alternatively use an approved known-good Git revision/branch as Coolify's source, and deploy.

A failed build often leaves the previous running application serving, but runtime replacement can still disrupt service. A restored image does not restore DB schema or external side effects. After any failure describe: target, requested SHA, deployment UUID, last known status, first failing stage, verified observations and smallest reversible next step.
