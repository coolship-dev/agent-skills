#!/usr/bin/env sh
# Read-only advisory check. Run from the APPLICATION repository.
# Requires git and Coolship. Nonzero means checks are missing or failed;
# zero does not establish deployment authorization, readiness or remote SHA.
set -u
export CI=true
printf 'Coolship preflight: no deployment will be submitted\n'
if ! command -v git >/dev/null 2>&1; then
  printf 'ERROR: git is not available\n' >&2
  exit 2
fi
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'ERROR: run inside an application Git worktree\n' >&2
  exit 2
fi
if ! revision=$(git rev-parse --verify HEAD 2>/dev/null); then
  printf 'ERROR: application repository has no committed revision\n' >&2
  exit 2
fi
printf 'Repository: %s\n' "$(git rev-parse --show-toplevel)"
printf 'Branch: %s\n' "$(git branch --show-current)"
printf 'Commit: %s\n' "$revision"
if [ -n "$(git status --porcelain)" ]; then
  printf 'WARNING: uncommitted changes are not uploaded by Coolship\n'
else
  printf 'Working tree: clean\n'
fi
if git rev-parse --abbrev-ref '@{upstream}' >/dev/null 2>&1; then
  upstream=$(git rev-parse --abbrev-ref '@{upstream}')
  ahead=$(git rev-list --count '@{upstream}..HEAD')
  behind=$(git rev-list --count 'HEAD..@{upstream}')
  printf 'Upstream: %s; ahead=%s, behind=%s (cached local metadata)\n' "$upstream" "$ahead" "$behind"
else
  printf 'WARNING: no tracked upstream; verify Git push and Coolify source\n'
fi
if ! command -v coolship >/dev/null 2>&1; then
  printf 'ERROR: coolship not found; remote checks unavailable\n' >&2
  exit 1
fi
result=0
coolship --version || result=1
printf '\nResolved context and binding\n'
coolship config show || result=1
printf '\nRemote diagnosis (a new app may not be running yet)\n'
coolship doctor || result=1
printf '\nCurrent target status\n'
coolship status || result=1
printf '\nVerify target, pushed revision and health before deploying.\n'
exit "$result"
