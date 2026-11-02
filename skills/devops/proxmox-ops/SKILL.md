---
name: proxmox-ops
description: Diagnose and maintain Proxmox virtual machines and containers. Use for Proxmox host, guest, storage, backup or cluster operations.
---

# Proxmox ops

Resolve the exact cluster, node, guest ID and requested operation. Confirm authorization and access using existing secure configuration. Discover live state; do not infer topology or credentials from examples.

Use read-only checks first: node/guest status, storage capacity, task logs, backup age and cluster quorum where relevant. Consult installed command help and the matching Proxmox documentation before executing unfamiliar operations. Avoid dumping credential-bearing configuration.

Before changes, identify affected guests, shared storage, dependencies and rollback options. Confirm usable backups for data-affecting work; snapshots are not independent backups. Preserve quorum and account for maintenance/migration constraints.

Perform only the authorized operation and observe completion and guest health. Guest deletion, disk removal, storage reformatting and cluster membership changes require explicit destructive scope. Do not escalate a guest issue into host networking or cluster changes without evidence and authorization.

Report the exact target, changes, task result, verification and recovery limitations.
