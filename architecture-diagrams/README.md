# Architecture Diagrams Skill

Professional architecture diagram generator using the [Diagrams](https://diagrams.mingrammer.com/) Python library. Creates publication-quality diagrams with real cloud provider icons.

## Supported Providers

- **AWS** — EC2, Lambda, RDS, S3, VPC, CloudFront, SQS, etc.
- **Azure** — VM, Functions, CosmosDb, LoadBalancers, etc.
- **GCP** — GCE, GKE, BigQuery, Cloud Functions, etc.
- **Kubernetes** — Pod, Deployment, Service, Ingress, PV, etc.
- **On-Premise** — Docker, Nginx, PostgreSQL, Kafka, Prometheus, etc.
- **Generic** — Router, Switch, Firewall, VPN, Subnet, Server, etc.
- **Custom** — Use any PNG/JPG as node icon

## Examples

| Diagram | Description |
|---------|-------------|
| `cisco-network.py` | Enterprise network with DMZ, firewalls, server farm |
| `aws-architecture.py` | Production AWS with VPC, ALB, ECS, RDS Multi-AZ |
| `kubernetes-cluster.py` | K8s cluster with namespaces, service mesh, monitoring |

## Quick Start

```bash
# Activate venv
source .venv/bin/activate

# Generate an example
python scripts/generate.py src/examples/cisco-network.py

# Output: output/png/cisco-network.png
```

See `SKILL.md` for full reference documentation.
