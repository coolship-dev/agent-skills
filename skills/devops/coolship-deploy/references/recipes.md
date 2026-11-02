# Deployment recipes and design decisions

Inspect actual files before choosing; don't replace an existing correct project setup with these generic recipes.

| App style | Typical approach | Main risk |
| --- | --- | --- |
| Dockerfile present | Dockerfile build pack, matching port | Entry point not binding `0.0.0.0`, no readiness check |
| Compose file present | Compose deployment, named service domains | Accidentally publishing DB or altering named volumes |
| Next.js SSR | Existing Dockerfile / Railpack | Confusing static export with server-side rendering |
| Vite / React SPA | Static site output (`dist`) served by nginx/Coolify static path | Wrong output directory, missing SPA fallback |
| FastAPI / Flask | Railpack or Dockerfile | Binding to `localhost` instead of `0.0.0.0` |
| Worker/queue consumer | Non-HTTP process/Compose worker | Fake HTTP health checks, secrets or private queues exposed |

## Example: Python FastAPI Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Adapt import path, dependencies, Python version, nonroot runtime policy and image security to the project. This command fixes port 8000; set the matching Coolify exposed port. A health endpoint (`/healthz`) should return HTTP 200 only when the application is ready.

## Example: Compose

See [example Compose asset](../assets/compose.example.yaml). Expose app internally and let Coolify route its domain; normally do not use `ports:` on publicly accessible interfaces. A database should be private and its persistence/backups explicit. Avoid fixed `container_name` and host ports if preview deployments or multiple environments might coexist. Health checks and correct data mounts are more important than Compose `depends_on` alone.

```bash
coolship init --compose-domain web=https://app.example.com
# or after binding: coolship domain set web=https://app.example.com
coolship deploy
coolship logs --service web --lines 100
```

Check installed Coolify version supports service-specific logs. Replace example domain and service names with actual names.

## Runtime, network and Cloudflare

For a public hostname verify separately: (1) server listens internally on correct port, (2) Coolify maps domain to right service and port, (3) DNS/Cloudflare Tunnel reaches intended proxy, (4) HTTPS and access controls are correct. `domain set` does not manage all four.

For private services intentionally bound to LAN/Tailscale, do not expose a public hostname just to satisfy health checks. Use an appropriately networked test runner and document unreachable checks.

## Environment variables and state

Keep variables in Coolify; document names and ownership but not values. Distinguish build-time values, runtime secrets, shared Coolify variable references and preview scopes. Ensure `.env` ignored and never pasted to an AI model.

For persistent services, verify volumes/backup restore. A changed Compose service/project name can change volume naming and make existing data appear missing. Coordinate schema migrations with rolling updates; don't assume image rollback restores database state.

## External smoke test

```bash
curl --fail --show-error --silent --max-time 10 "https://YOUR_REAL_DOMAIN/healthz"
```

Do not execute this against the placeholder URL. If practical expose a safe `/version` returning build SHA to confirm deployed revision; otherwise use Coolify's deployment commit reference and read-only status checks.
