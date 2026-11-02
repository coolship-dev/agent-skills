---
name: cloudflare-routing
description: Configure and diagnose Cloudflare DNS, proxy and Tunnel routing. Use for hostname routing, origin reachability, TLS or Cloudflare access failures.
---

# Cloudflare routing

Resolve the intended account, zone, hostname, service and exposure policy. Inspect current DNS, proxy status, tunnel ingress and origin configuration without exposing API or tunnel tokens. Use current official documentation for API semantics and TLS behavior.

Trace the request through DNS, Cloudflare edge/Access, tunnel or public origin, reverse proxy and application port. Check each layer separately; an edge success response does not prove origin health. Distinguish DNS caching, certificate mismatch, origin connection failures and authorization failures.

Review existing records and routing before changing them. Preserve mail and verification records; do not disable TLS verification or publish a private service as a diagnostic shortcut. Scope credentials to the required zone/operation and retain previous values for rollback.

Apply authorized changes and verify DNS plus a real application request, accounting for TTL and cache. Report the hostname, changed layer, observed response and any unresolved origin or access issue.
