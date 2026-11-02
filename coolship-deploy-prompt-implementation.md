Created a portable AI deployment skill tailored to your Coolify infrastructure and your [Coolship CLI](https://github.com/joaomnuno/coolship?utm_source=chatgpt.com).

Coolship Deployment Agent Skill

12 files · Agent Skills format · No credentials included

&#x20;Download complete skill (.zip)

View SKILL.md

## What the skill teaches an AI agent

- Infrastructure discovery: Recognize your self-hosted Coolify instances, contexts, applications and environments.
- Application deployment: Use `coolship init`, `link`, `deploy`, `status` and `logs`.
- Different application types: Deploy Dockerfiles, Docker Compose, Python APIs, React/Next.js projects and monorepos.
- Configuration: Handle environment variables, domains, Cloudflare routing, persistent volumes and health checks.
- CI/CD: Deploy through GitHub Actions or Coolify's automatic Git integration without duplicate triggers.
- Deployment verification: Confirm the deployed Git commit, health, runtime logs and availability.
- Failure recovery: Diagnose broken builds, incorrect ports, unreachable servers and deployment timeouts.

I used your actual Coolship repository documentation, including its command syntax and the `coolify-lx` example context. Historical infrastructure details are explicitly marked as requiring live verification.

## How to use it with another AI

Extract the package into your project's `.agents/skills/` directory:

```
your-project/
├── .agents/
│   └── skills/
│       └── coolship-deploy/
│           ├── SKILL.md
│           ├── references/
│           ├── assets/
│           └── scripts/
├── Dockerfile
└── ...
```

The structure follows the open [Agent Skills specification](https://agentskills.io/specification?utm_source=chatgpt.com) and can be consumed by compatible agents. Other AI models can read `SKILL.md` directly as ordinary Markdown.

You can then give an agent a request such as:

> Deploy this application to my self-hosted Coolify using the Coolship deployment skill. Inspect the repository, determine the appropriate configuration, verify the target, and deploy after the required checks.

Important: The skill contains no API tokens and does not grant deployment access. An agent still needs its own authorized CLI environment.

No applications were modified or deployed while creating this package.&#x20;
