#!/bin/sh
# Install the curated frontend skills into the current project.
# Node.js 22.20+ and npx are required; no global tools are installed.
set -eu

if ! command -v npx >/dev/null 2>&1; then
  printf '%s\n' 'Requires npx (Node.js 22.20+).' >&2
  exit 1
fi

if [ "$#" -eq 0 ]; then
  set -- codex claude-code cursor opencode
fi

for agent do
  case "$agent" in
    codex|claude-code|cursor|opencode) ;;
    *)
      printf 'Unsupported agent: %s\n' "$agent" >&2
      printf '%s\n' 'Supported: codex, claude-code, cursor, opencode.' >&2
      exit 2
      ;;
  esac
done

npx skills add coolship-dev/agent-skills \
  --skill frontend-architecture --skill frontend-review -a "$@" -y

npx skills add vercel-labs/agent-skills \
  --skill vercel-react-best-practices \
  --skill vercel-composition-patterns \
  --skill web-design-guidelines -a "$@" -y

npx skills add anthropics/skills --skill frontend-design -a "$@" -y

if command -v playwright-cli >/dev/null 2>&1; then
  playwright-cli install --skills
else
  printf '%s\n' 'Optional: npm install -g @playwright/cli@latest'
  printf '%s\n' 'Then: playwright-cli install --skills'
fi

printf '%s\n' 'Frontend skill installation complete.'
