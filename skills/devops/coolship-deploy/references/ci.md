# CI/CD strategy for Coolship + Coolify

`coolship deploy` deploys the Git source and branch **already configured in Coolify**, not the GitHub Actions checkout. Always verify the targeted revision.

## Pick one deployment trigger

1. **Coolify Git integration/webhook**: pushing to the configured branch auto-deploys; CI runs tests. Avoid adding a separate `coolship deploy` per push, which can duplicate deployments.
2. **CI-driven release**: disable overlapping Coolify auto-deploy; after tests succeed, CI calls `coolship deploy`, waits and checks the health endpoint.
3. **Manual promotion**: run a protected `workflow_dispatch` GitHub Actions job. The bundled [workflow asset](../assets/github-actions-deploy.yml) shows this path.

## Secrets and permission

Store `COOLSHIP_URL` and `COOLSHIP_TOKEN` in GitHub Actions environment secrets or an equivalent secret manager. Use a Coolify token scoped to operations actually needed; some runtime/build logs require `read:sensitive`. Never export secrets into logs, artifacts or AI prompts. Use a protected `production` GitHub environment, read-only repo checkout, serialized deployment concurrency and explicit branch/source verification.

## CI checklist

- Quality gates: repo-specific tests, lint and build all pass on the intended revision.
- Coolify source points to intended repository/branch; if checkout SHA differs from server's branch head, do **not** report that SHA deployed.
- A Git webhook is not racing with a duplicate CLI deploy.
- The job waits for Coolship's deployment to finish (not `--no-wait`).
- App status, health route and deployed revision confirmed afterward.
- For schema migrations, volumes and other stateful operations, there is an explicit backup and rollback/forward-fix plan.

## Preview apps

`coolship preview --pr N` only works when Coolify has registered the pull request using its Git provider integration/preview deployment feature. Preview variables are separate; avoid exposing production secrets to untrusted PR code. Use isolated storage when appropriate.

## Version pinning

The included workflow uses `go install github.com/joaomnuno/coolship@v0.4.0` with Go 1.26 to avoid `curl | sh` in CI. Future versions should be intentionally upgraded after reviewing changes; `main` may have unreleased functionality. The example is intentionally manual and fails before deployment until the application supplies three executable hooks:

- `scripts/check-deployment.sh`: run the project's required tests/build checks.
- `scripts/verify-coolify-source.sh EXPECTED_SHA`: verify the linked Coolify source repository/branch resolves to this SHA; exit nonzero on mismatch or unavailable evidence.
- `scripts/verify-release.sh EXPECTED_SHA`: check real application readiness and its release marker after deployment; exit nonzero on mismatch or unavailable evidence.

These hook paths belong to the application repository, not this skill package. Implement them for the app's API/runtime; do not replace them with unconditional success. A failed post-deploy check must fail the workflow and trigger investigation, not a blind duplicate deploy. A source branch can advance during a build, so verification after deployment remains necessary.
