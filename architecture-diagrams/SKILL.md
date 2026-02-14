---
name: architecture-diagrams
description: Use when creating professional architecture diagrams, cloud infrastructure visuals, network topologies, Kubernetes cluster diagrams, or microservices architecture diagrams as PNG/SVG images using Python Diagrams library with real provider icons (AWS, Azure, GCP, K8s, OnPrem, Generic)
---

# Architecture Diagrams

**Portable Claude Agent Skill**

Professional architecture diagram generator using the [Diagrams](https://diagrams.mingrammer.com/) Python library. Produces publication-quality diagrams with real cloud provider icons (AWS, Azure, GCP, K8s, OnPrem, Generic).

**Portability:** This entire `architecture-diagrams/` folder is self-contained. Copy it to `~/.claude/skills/` or any project's `.claude/skills/` directory. Run `./scripts/setup.sh` once per location.

## Installation & Setup

### System Prerequisite

Graphviz must be installed system-wide (provides the `dot` binary):

```bash
# Ubuntu/Debian
sudo apt install graphviz

# macOS
brew install graphviz

# RHEL/Fedora
sudo dnf install graphviz
```

### One-Time Setup (Per Installation Location)

```bash
cd <path-to>/architecture-diagrams/
chmod +x scripts/setup.sh
./scripts/setup.sh
```

This creates `.venv/`, installs Python dependencies, and verifies graphviz.

### Automated Setup Check

```bash
cd <path-to>/architecture-diagrams/
if [ ! -d ".venv" ]; then
  ./scripts/setup.sh
fi
echo "Skill ready"
```

## Quick Start

```bash
# 1. Navigate to skill folder
cd <path-to>/architecture-diagrams/

# 2. Verify setup
if [ ! -d ".venv" ]; then ./scripts/setup.sh; fi

# 3. Activate venv
source .venv/bin/activate

# 4. Create a new diagram script (copy template)
cp src/templates/basic-template.py src/examples/my-diagram.py

# 5. Edit the script (import nodes, define topology, connect)

# 6. Generate PNG
python scripts/generate.py src/examples/my-diagram.py

# Output: output/png/my-diagram.png
```

## File Structure

```
architecture-diagrams/        <-- Skill root (portable)
  SKILL.md                    # This file
  requirements.txt            # Python deps (diagrams, graphviz)
  .venv/                      # Python virtual environment (created by setup.sh)
  scripts/
    setup.sh                  # Creates .venv and installs deps
    generate.py               # Runs diagram script, outputs to output/png/
  src/
    templates/                # Starter templates — copy these
      basic-template.py       # Minimal template with TODOs
    examples/                 # Working example diagrams
      cisco-network.py        # Network topology with routers, switches, firewall
      aws-architecture.py     # AWS cloud architecture with VPC, ALB, RDS
      kubernetes-cluster.py   # K8s cluster with namespaces, services, monitoring
  output/png/                 # Generated diagram images
  docs/                       # Additional documentation
```

## Core Concepts

### Diagram Context Manager

Every diagram uses the `Diagram` context manager:

```python
from diagrams import Diagram, Cluster, Edge

with Diagram(
    "Diagram Title",          # Title shown on diagram
    filename="output-name",   # Output filename (no extension)
    outformat="png",          # png, jpg, svg, pdf, dot
    show=False,               # Don't auto-open
    direction="TB",           # TB, BT, LR, RL
    graph_attr={...},         # Graphviz attributes
):
    # nodes and connections here
```

### Direction

| Value | Meaning | Best For |
|-------|---------|----------|
| `TB` | Top to bottom | Hierarchical architectures, network topologies |
| `BT` | Bottom to top | Data flow upward |
| `LR` | Left to right | Pipelines, data flow, timelines |
| `RL` | Right to left | Reverse flows |

### Graph Attributes

```python
graph_attr = {
    "fontsize": "14",       # Title font size
    "bgcolor": "#ffffff",   # Background color
    "pad": "0.5",           # Padding around diagram
    "nodesep": "0.6",       # Horizontal spacing
    "ranksep": "0.8",       # Vertical spacing between ranks
    "splines": "spline",    # Edge routing: spline, ortho, curved, polyline
    "concentrate": "true",  # Merge parallel edges
}
```

## Node Providers Quick Reference

### Generic (Network Infrastructure)

```python
from diagrams.generic.network import Firewall, Router, Switch, Subnet, VPN
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.storage import Storage
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.place import Datacenter
from diagrams.generic.os import Ubuntu, Windows, LinuxGeneral, Debian, RedHat, CentOS
from diagrams.generic.virtualization import Vmware, Virtualbox, Qemu
from diagrams.generic.blank import Blank  # Invisible node for layout control
```

### AWS

```python
# Compute
from diagrams.aws.compute import EC2, ECS, Lambda, Fargate, ElasticBeanstalk, Batch
# Database
from diagrams.aws.database import RDS, Aurora, Dynamodb, ElastiCache, Neptune, Redshift
# Network
from diagrams.aws.network import ELB, Route53, CloudFront, VPC, APIGateway, DirectConnect
# Storage
from diagrams.aws.storage import S3, EFS, FSx
# Security
from diagrams.aws.security import Cognito, WAF, IAM, KMS, CertificateManager
# Integration
from diagrams.aws.integration import SQS, SNS, Eventbridge, StepFunctions
# Management
from diagrams.aws.management import Cloudwatch, Cloudformation, Cloudtrail, AutoScaling
# Analytics
from diagrams.aws.analytics import Kinesis, Athena, Glue, EMR
# General
from diagrams.aws.general import Users, Client
```

### Azure

```python
from diagrams.azure.compute import VM, FunctionApps, ContainerInstances, KubernetesServices
from diagrams.azure.database import CosmosDb, SQLDatabases, CacheForRedis
from diagrams.azure.network import LoadBalancers, ApplicationGateway, DNS, VirtualNetworks
from diagrams.azure.storage import BlobStorage, StorageAccounts
from diagrams.azure.security import KeyVaults, ActiveDirectory
from diagrams.azure.integration import ServiceBus, EventGrid
from diagrams.azure.web import AppServices
```

### GCP

```python
from diagrams.gcp.compute import GCE, GKE, Functions, Run, AppEngine
from diagrams.gcp.database import SQL as GcpSQL, Spanner, Firestore, BigTable, Memorystore
from diagrams.gcp.network import LoadBalancing, CDN, DNS as GcpDNS, VPC as GcpVPC
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, PubSub, Dataflow
from diagrams.gcp.security import IAP, KMS as GcpKMS
```

### Kubernetes

```python
from diagrams.k8s.compute import Pod, Deployment, StatefulSet, ReplicaSet, Job, CronJob, DaemonSet
from diagrams.k8s.network import Ingress, Service, NetworkPolicy
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.k8s.rbac import ServiceAccount, Role, ClusterRole
from diagrams.k8s.infra import Node as K8sNode, Master
from diagrams.k8s.clusterconfig import HPA, ConfigMap, Secret
from diagrams.k8s.podconfig import Container
```

### On-Premise

```python
# Network
from diagrams.onprem.network import Nginx, HAProxy, Traefik, Istio, Envoy, Consul, Kong, Apache
# Database
from diagrams.onprem.database import PostgreSQL, MySQL, MongoDB, Cassandra, Redis as OnPremRedis
from diagrams.onprem.database import Neo4J, CockroachDB, InfluxDB, Clickhouse
# Queue
from diagrams.onprem.queue import Kafka, RabbitMQ, ActiveMQ, Celery, Nats
# Container
from diagrams.onprem.container import Docker
# CI/CD
from diagrams.onprem.ci import Jenkins, GithubActions, GitlabCI, CircleCI
from diagrams.onprem.cd import Spinnaker, Tekton
from diagrams.onprem.gitops import ArgoCD, Flux
# Monitoring
from diagrams.onprem.monitoring import Prometheus, Grafana, Datadog, Splunk, Nagios
from diagrams.onprem.logging import Loki, Fluentbit
from diagrams.onprem.tracing import Jaeger, Tempo
# IAC
from diagrams.onprem.iac import Terraform, Ansible
# VCS
from diagrams.onprem.vcs import Git, Github, Gitlab
# Analytics
from diagrams.onprem.analytics import Spark, Hadoop, Flink
# Auth/Security
from diagrams.onprem.security import Vault, Trivy
# Workflow
from diagrams.onprem.workflow import Airflow, Kubeflow, Nifi
# In-Memory
from diagrams.onprem.inmemory import Redis, Memcached
# Compute
from diagrams.onprem.compute import Server, Nomad
```

### Custom Icons

```python
from diagrams.custom import Custom

# Use any local PNG/JPG image as a node icon
my_service = Custom("My Service", "./path/to/icon.png")
```

## Clusters (Grouping)

```python
with Cluster("VPC"):
    with Cluster("Public Subnet"):
        web = EC2("Web")
    with Cluster("Private Subnet"):
        api = EC2("API")
        db = RDS("Database")
```

**Cluster attributes:**

```python
with Cluster("Styled Group", graph_attr={
    "bgcolor": "#e8f4fd",     # Background color
    "style": "dashed",        # solid, dashed, dotted, rounded
    "color": "#2196F3",       # Border color
    "penwidth": "2.0",        # Border width
    "fontsize": "12",         # Label font size
    "fontcolor": "#333333",   # Label color
    "labeljust": "l",         # Label alignment: l, r, c
}):
    pass
```

## Edges (Connections)

### Basic Connections

```python
# Forward direction
node_a >> node_b

# Backward direction
node_a << node_b

# Bidirectional (no arrows)
node_a - node_b

# One-to-many
node_a >> [node_b, node_c, node_d]

# Chain
node_a >> node_b >> node_c
```

### Styled Edges

```python
from diagrams import Edge

node_a >> Edge(
    label="HTTPS",        # Text label on the edge
    color="blue",         # Edge color (name or hex)
    style="dashed",       # solid, dashed, dotted, bold
    minlen="2",           # Minimum edge length (ranks)
) >> node_b
```

### Edge Style Patterns

| Connection Type | Color | Style | Example |
|----------------|-------|-------|---------|
| Synchronous API | `blue` or `navy` | `solid` | REST/gRPC calls |
| Async messaging | `orange` or `green` | `dashed` | Kafka, SQS, events |
| Database access | `purple` or `red` | `solid` | SQL queries |
| Replication | `gray` | `dashed` | DB replication |
| Monitoring | `gray` | `dotted` | Metrics/logs |
| External API | `brown` or `gold` | `solid` | Third-party |
| Cache | `red` | `solid` | Redis/Memcached |
| Storage | `brown` | `dotted` | S3, NFS, iSCSI |

## Output Formats

| Format | Flag | Use Case |
|--------|------|----------|
| PNG | `png` (default) | Documentation, presentations |
| SVG | `svg` | Scalable web embedding |
| PDF | `pdf` | Print-quality documents |
| JPG | `jpg` | Compressed images |
| DOT | `dot` | Graphviz source for manual editing |

```python
# Single format
with Diagram("Title", outformat="svg"): ...

# Multiple formats at once
with Diagram("Title", outformat=["png", "svg", "pdf"]): ...
```

## Generate Script Usage

```bash
# Activate venv first
source .venv/bin/activate

# Generate from example
python scripts/generate.py src/examples/cisco-network.py

# Custom output name
python scripts/generate.py src/examples/cisco-network.py --name my-network

# SVG format
python scripts/generate.py src/examples/aws-architecture.py --outformat svg

# Custom output directory
python scripts/generate.py src/examples/aws-architecture.py --output-dir /tmp/diagrams/
```

## Common Diagram Patterns

### Network Topology
Layout: `TB`. Use `diagrams.generic.network` for Router, Switch, Firewall, VPN, Subnet. Cluster for DMZ, Internal, Management zones. See `src/examples/cisco-network.py`.

### Cloud Architecture
Layout: `TB`. Use AWS/Azure/GCP provider icons. Cluster for VPC, subnets, AZs. Edge labels for protocols. See `src/examples/aws-architecture.py`.

### Kubernetes Cluster
Layout: `TB`. Use `diagrams.k8s` for Pod, Deployment, Service, Ingress. Cluster for namespaces. OnPrem for monitoring stack (Prometheus, Grafana). See `src/examples/kubernetes-cluster.py`.

### Microservices
Layout: `TB` or `LR`. Mix providers: OnPrem for services, AWS for infra. Cluster for service groups. Edge styles differentiate sync/async/data flows.

### CI/CD Pipeline
Layout: `LR`. Use `diagrams.onprem.ci` and `diagrams.onprem.cd`. Linear flow with branching for environments.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| `ModuleNotFoundError: diagrams` | Activate venv first: `source .venv/bin/activate` |
| `ExecutableNotFound: dot` | Install graphviz: `sudo apt install graphviz` |
| Diagram opens in viewer | Set `show=False` in Diagram() |
| File saved in wrong directory | The script uses `cwd` for output — use `generate.py` to control |
| Import error for provider class | Check exact class name at diagrams.mingrammer.com/docs/nodes/ |
| Cluttered edges overlapping | Use `"splines": "ortho"` or `"concentrate": "true"` in graph_attr |
| Nodes too close together | Increase `nodesep` and `ranksep` in graph_attr |
| Diagram too large/small | Adjust `pad`, `fontsize`, and node count per cluster |
| Custom icon not found | Path must be relative to the script's working directory |
| Multiple outputs not working | Pass list to outformat: `outformat=["png", "svg"]` |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `setup.sh` fails | Ensure Python 3.7+ and graphviz binary are installed |
| `.venv` creation fails | Try `python3 -m venv .venv --clear` to recreate |
| Blank/empty output | Verify nodes are defined inside the `with Diagram()` block |
| Permission denied on output | Check write permissions for `output/png/` directory |
| Slow generation | Large diagrams with many nodes are normal — reduce clusters or nodes |
| `dot` segfault | Update graphviz: `sudo apt install --only-upgrade graphviz` |
