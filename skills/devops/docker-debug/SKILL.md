---
name: docker-debug
description: Diagnose Docker and Docker Compose failures. Use for container startup, builds, networking, mounts, health checks or resource problems.
---

# Docker debug

Identify the project, Docker context, Compose project and affected services before commands. Read container configuration and recent changes. Use installed command help where flags are uncertain.

Start with read-only state: service status, bounded logs, exit codes, health results, image identity, resource use and network/mount metadata. Logs and inspect output can contain secrets; select fields and redact values. Distinguish build failures, process crashes, readiness failures and routing failures.

Trace ports from the process bind address through container networking, published ports and upstream proxies. Check service DNS, dependency readiness, filesystem permissions and volume ownership. Do not assume localhost inside a container refers to another service.

Choose a fix supported by evidence and verify application behavior. Restart or rebuild only within authorization. Never use volume removal, system prune, host network changes or privileged containers as a routine fix. Protect persistent data and explain any destructive recovery action before proceeding.
