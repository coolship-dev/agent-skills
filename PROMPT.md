# Designing your AI skills repository

After reviewing the approaches used by Cursor, Claude Code, pstack, and Vercel, my recommendation is to build a model-agnostic skills repository based on the open Agent Skills specification.

For your own development projects and Coolship, I'd use a single canonical repository, rather than maintaining separate versions for Cursor, Claude, Codex, and OpenCode.

The architecture should follow three principles:

1. Write once, use across agents. Keep the reusable instructions in standard `SKILL.md` files.
2. Keep skills focused. Deployment, debugging, code review, and infrastructure management should be separate capabilities.
3. Load only what's necessary. Keep detailed documentation, scripts, and templates outside the main skill instructions.

## 1. What existing projects are doing

[Cursor AI Logo | Free SVG & PNG Download](https://images.openai.com/static-rsc-4/JvOKqQN9aK-4Sk2XzoANbNy3R-XLs9jR39Y1pnc0diCBq4J4iEONRTmXxyv9dbtti_JleJuMMZ8wngBeWSvPyM5mJxOWQfiyzn18G6Yp3ExqdfhFjEPRXO6oGfp0T-aXNgZPZqcp2FcYkY5Zqfu_QG2hDGGykauWQF8yYWYdW0s?purpose=inline)

[Cursor plugins](https://github.com/cursor/plugins?utm_source=chatgpt.com)

Cursor supports skills in `.agents/skills/` and `.cursor/skills/`, including nested category folders. Its plugin system can additionally package agents, commands, rules, and tools.

Takeaway: Separate portable skills from platform-specific integrations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://cursor.com\&sz=32)

Cursor Docs+1



[Home](https://images.openai.com/static-rsc-4/gYlNccbPmRJKobSaMgeihIHF_fOeB3tyBQTsLPCeYIXE0NUINM4BRHgK_yhAAfTpGgshwfMsHCAgYxRBfXfM3YAY-ZZ3W5q1_Yk0I_XneYQGvrlqLyKv4Syfam4qWSbPzUNq2m_6Oom9Zdgm-sB8LrbIwCBXuxRGSA-4CZ8ElwU?purpose=inline)

[Anthropic skills](https://github.com/anthropics/skills?utm_source=chatgpt.com)

Anthropic organizes skills as self-contained directories, each with a `SKILL.md` and optional `scripts/`, `references/`, and `assets/`. Its skill creator also supports testing and iterative improvement.

Takeaway: A skill should be a complete, independently reusable package.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



[PStack 1.0.4 VSIX (Latest Version) - VsixHub](https://images.openai.com/static-rsc-4/FcAkzbg-Od9e2VcxJLY1TsfOJoLSiZusu4KcutvwEjPHCsxA1cV3aF8Oj8GsOn6IZ_MmakQ1UjlB3LMldUpkU1gjM9mwCWfab9Fu_glYj07rnA-UFQO3wsTHEXWg2rJq3jQMdEpiEFRo5c4fPlDdFnp46loOzTWjfDFtA8w3w-A?purpose=inline)

[pstack](https://github.com/cursor/plugins/tree/main/pstack?utm_source=chatgpt.com)

pstack packages workflows as skills and agents, with a Cursor plugin manifest. Its `unslop` skill is a concise, actionable checklist with stable rule identifiers, rather than a broad personality prompt.

Takeaway: Write instructions as concrete procedures and review criteria.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



[How to Use Vercel - Getting Started Guide (2026) | Delv](https://images.openai.com/static-rsc-4/II9DBEprjDf0_Y2RIUGxgZ4bjOULzr-2p-vKNBRgqy7HlRqGOMqEpPcOwUNksEJ5cF_VNDkA9VOZEQMGM7tEd68wU6Qq1Ie8oBMWk56TuhpHeXCmYhRbaAIW1gPry2H2caHr25d3R9XsGDeBbGjL3gVZdw_ZqTY_kipySshbK7A?purpose=inline)

[Vercel agent-skills](https://github.com/vercel-labs/agent-skills?utm_source=chatgpt.com)

Vercel maintains a central `skills/` directory with specialized skills for things like React performance and web design. Its installation CLI supports multiple agent environments.

Takeaway: Use an agent-independent repository with selective installation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



The common denominator is the [Agent Skills specification](https://agentskills.io/specification?utm_source=chatgpt.com): a directory containing a `SKILL.md` with YAML metadata. This is the format I would adopt as the foundation, rather than inventing a Coolship-specific format.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://agentskills.io\&sz=32)

Agent Skills



## 2. My proposed repository structure

I would call the repository `agent-skills`, ideally under the Coolship GitHub organization once that's available.

coolship/agent-skills

Proposed

```
agent-skills/
├── README.md
├── AGENTS.md
├── LICENSE
├── .github/
│   └── workflows/
│       └── validate-skills.yml
│
├── skills/
│   ├── engineering/
│   │   ├── plan-feature/
│   │   ├── implement-feature/
│   │   ├── debug-issue/
│   │   ├── review-code/
│   │   └── unslop/
│   │
│   ├── web/
│   │   ├── react-best-practices/
│   │   └── web-ui-review/
│   │
│   ├── devops/
│   │   ├── coolship-deploy/
│   │   │   ├── SKILL.md
│   │   │   ├── references/
│   │   │   │   ├── coolify.md
│   │   │   │   └── coolship-cli.md
│   │   │   ├── scripts/
│   │   │   │   └── preflight.sh
│   │   │   └── evals/
│   │   │       └── cases.json
│   │   ├── docker-debug/
│   │   ├── proxmox-ops/
│   │   └── cloudflare-routing/
│   │
│   ├── python/
│   │   ├── python-project-setup/
│   │   └── opencv-development/
│   │
│   └── embedded/
│       └── platformio-workflow/
│
├── docs/
│   ├── contributing.md
│   └── authoring-guidelines.md
│
└── scripts/
    └── validate-skills.py
```

Each leaf directory under `skills/` contains its own `SKILL.md`. Additional folders are added only when needed.

This borrows Anthropic's self-contained packaging and Cursor's category grouping while retaining Vercel's convenient installable `skills/` root. The installation CLI recognizes these nested catalog layouts.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

npx skills · GitHub+1



### What belongs where?

| Component            | Purpose                                                      |
| -------------------- | ------------------------------------------------------------ |
| `SKILL.md`           | The agent's instructions for one specific capability         |
| `references/`        | Detailed documentation loaded only when needed               |
| `scripts/`           | Executable, reproducible operations                          |
| `assets/`            | Configuration templates, schemas, and other static resources |
| `evals/`             | Example tasks and expected behavior for testing              |
| Root `AGENTS.md`     | Instructions for agents maintaining this repository          |
| Root `README.md`     | Human-readable catalog and installation instructions         |
| `.github/workflows/` | Validation on pull requests                                  |

The distinction between the root `AGENTS.md` and your skills is important. `AGENTS.md` governs agents working on the skills repository. It is not automatically distributed as a universal instruction to every project that installs one of your skills.

## 3. How I would design each skill

Your Coolify/Coolship deployment workflow is a particularly good example.

skills/devops/coolship-deploy/SKILL.md

```
---
name: coolship-deploy
description: Deploy, update, and troubleshoot
  applications using self-hosted Coolify and the
  Coolship CLI. Use when a user wants to deploy
  a project, publish changes, inspect a failed
  deployment, or roll back an application.
compatibility: Requires access to the deployment
  environment and its configured tools.
---

# Coolship deployment

## Goal

Deploy applications safely and verify that they
are functioning before reporting success.

## Workflow

1. Inspect the repository and existing deployment
   configuration.
2. Identify the target environment and deployment
   method.
3. Read the relevant reference:
   - `references/coolship-cli.md`
   - `references/coolify.md`
4. Validate prerequisites and configuration.
5. Run tests and build checks where applicable.
6. Deploy using the verified workflow.
7. Check deployment status and application health.
8. Report the result and rollback procedure.

## Rules

- Never invent CLI commands or flags.
- Prefer the project's established deployment method.
- Never print or commit credentials.
- Obtain confirmation before destructive operations
  or unrequested production changes.
- Do not claim success without verification.
- Stop and report a blocking failure.

## Output

Report the environment, deployment method,
verification results, application URL if known,
and any required follow-up actions.
```

Notice that the main file describes the decision process, not every command the agent might execute.

All the technical details, like how to configure Coolify or the supported commands of your Coolship CLI, belong in the reference files.

That gives you two important benefits. You can update the deployment system without rewriting the entire skill, and the model doesn't need to read several thousand tokens of infrastructure documentation for every deployment.

The open specification explicitly encourages progressive loading: metadata first, `SKILL.md` when activated, and supporting resources on demand. It recommends keeping the main file below 500 lines.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://agentskills.io\&sz=32)

Agent Skills



## 4. What I'd borrow specifically from pstack

pstack has an interesting architectural idea beyond its individual skills.

It has an entry-point workflow called `poteto-mode` that selects specialized skills for harder tasks. Instead of expecting a user to know which capability to invoke, it chooses a suitable procedure and coordinates the rest.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



Potential future Coolship workflow

User requests a task

Project-workflow skill

Choose an appropriate process

Plan

Implement

Review

Verify and deploy

I'd eventually create a `project-workflow` skill that selects from smaller skills, but I would not implement this immediately.

A good starting point is five or six genuinely useful skills. Building a complicated orchestrator before those individual workflows are reliable adds unnecessary complexity.

Another important lesson from pstack: its workflows sometimes use Cursor-specific tools and model names, requiring a separate compatibility guide for Claude Code.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



For your repository, I'd reverse that approach: write vendor-neutral instructions first and add platform-specific adaptations only when necessary.

## 5. How to install and share your skills

I'd use the [Vercel skills CLI](https://github.com/vercel-labs/skills?utm_source=chatgpt.com) instead of writing a custom installer. It already supports Cursor, Claude Code, Codex, OpenCode, and many others.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

npx skills · GitHub



Inspect available skills

```
npx skills add OWNER/agent-skills --list
```

Install one skill into a project

```
npx skills add OWNER/agent-skills \
  --skill coolship-deploy \
  -a cursor -a claude-code -a codex
```

Install it globally for your user

```
npx skills add OWNER/agent-skills \
  --skill coolship-deploy \
  -g -a cursor -a claude-code -a codex
```

Manage installed skills

```
npx skills list
npx skills check
npx skills update
```

Replace OWNER with your GitHub account or organization. These commands are supported by the CLI; your proposed repository needs to exist first.

The CLI can use a shared installation with symlinks into the appropriate agent directories. For example, Claude Code uses `.claude/skills/`, while Cursor supports `.agents/skills/` and `.cursor/skills/`.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



For project-specific workflows, install only the relevant skills at project scope. For things you use constantly across repositories, global installation is more appropriate.

### Should you support Cursor and Claude plugins too?

Eventually, yes. But distinguish two things:

| Format             | What it provides                                                                       | Initial priority |
| ------------------ | -------------------------------------------------------------------------------------- | ---------------- |
| Agent Skills       | Portable instructions, scripts, and references                                         | Essential        |
| Cursor plugin      | Skills plus Cursor-specific agents, rules, commands, and marketplace integration       | Later            |
| Claude Code plugin | Skills plus Claude-specific hooks, agents, MCP integrations, and marketplace packaging | Later            |

Both plugin systems support structured plugin manifests, but they're a distribution and integration layer, not a prerequisite for writing useful skills.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub+1



## 6. Which skills I'd create first

For your programming work and the Coolship infrastructure, I'd prioritize these:

coolship-deploy

Coolify deployments, CLI workflows, verification, rollback

10/10

debug-issue

Reproduce, isolate root causes, fix, and verify

9/10

review-code

Detect regressions, correctness issues, security concerns

9/10

plan-feature

Turn requirements into an implementable technical plan

8/10

unslop

Remove unnecessary complexity, boilerplate, and vague output

8/10

docker-debug

Diagnose container networking, logs, and service failures

8/10

python-project-setup

Python environments, package management, tests, linting

7/10

proxmox-ops

Safe diagnosis and maintenance of virtualized infrastructure

7/10

My suggested implementation priorities, not scores from external benchmarks.

For `unslop`, I'd adapt the spirit of pstack's checklist instead of blindly copying its wording. I'd also distinguish prose quality from code quality: unnecessary abstractions and generated boilerplate deserve different checks from overpolished or generic writing.

## 7. Testing and maintaining the repository

This is where Anthropic's `skill-creator` provides a useful model: evaluate skills against realistic tasks, rather than assuming a well-written prompt will work reliably.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



For each important skill, maintain a few cases covering:

- Triggering: Does the agent select the skill when appropriate, and avoid it when irrelevant?
- Execution: Does it follow the expected procedure?
- Safety and failure handling: Does it stop appropriately on missing credentials, failed health checks, or potentially destructive actions?

For `coolship-deploy`, I'd use at least a successful staging deployment, a deployment with a missing configuration value, and a failed health-check scenario.

The repository CI should validate metadata, naming, referenced local paths, and runnable scripts. The reference `skills-ref` validator can check format compliance, while your own integration tests can verify actual behavior.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



One last operational decision: keep the general deployment instructions separate from private operational information. For public skills, use generic configuration and discovery instructions. If a skill needs sensitive infrastructure topology, store that detail in a private operations repository or a permission-controlled configuration source. Never embed access tokens or passwords in skills.

## My recommendation for version 1

Start with one repository, one portable format, and a small set of tested skills. Don't create a Cursor plugin, Claude plugin, or complicated multi-agent orchestration system until you have a specific need for them.

Your first milestone should be:

Initial repository checklist

Create the agent-skills GitHub repository

Add README.md and AGENTS.md

Create the coolship-deploy skill

Create debug-issue and review-code

Add format validation and basic evaluation cases

Test installation in Cursor and Claude Code

0 of 6 complete Copy checklist

The most important architectural decision: treat skills as reusable procedures, not giant system prompts. Once your deployment skill works correctly in two different agents, you'll have proven the repository design and can grow it with confidence.
