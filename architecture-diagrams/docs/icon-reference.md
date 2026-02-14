# Architecture Diagrams — Icon Reference

Complete catalog of all available icons in the Diagrams Python library.

**Total:** 2634 icons across 17 providers

> **Progressive Disclosure:** This index provides navigation and commonly-used icons. Each provider has a dedicated reference file in `docs/icons/` — load only what you need.

---

## Provider Files

| Provider | Icons | File | Best For |
|----------|-------|------|----------|
| [Generic](icons/generic.md) | 26 | `icons/generic.md` | Network devices, OS, compute, storage, virtualization |
| [AWS](icons/aws.md) | 562 | `icons/aws.md` | Amazon Web Services cloud architecture |
| [Azure](icons/azure.md) | 810 | `icons/azure.md` | Microsoft Azure cloud architecture |
| [GCP](icons/gcp.md) | 144 | `icons/gcp.md` | Google Cloud Platform architecture |
| [Kubernetes](icons/kubernetes.md) | 69 | `icons/kubernetes.md` | K8s clusters, pods, services, storage |
| [On-Premise](icons/onprem.md) | 211 | `icons/onprem.md` | Self-hosted infra, databases, CI/CD, monitoring |
| [SaaS](icons/saas.md) | 42 | `icons/saas.md` | Chat, identity, CDN, social, logging |
| [Programming](icons/programming.md) | 81 | `icons/programming.md` | Languages, frameworks, runtimes |
| [Other Clouds](icons/cloud-providers.md) | 689 | `icons/cloud-providers.md` | Elastic, Firebase, DigitalOcean, IBM, OCI, OpenStack, Outscale, Alibaba, GIS |

---

## Quick Start — Most Common Icons

### Network & Infrastructure
```python
from diagrams.generic.network import Firewall, Router, Switch, Subnet, VPN
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.storage import Storage
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.place import Datacenter
from diagrams.generic.os import Ubuntu, Windows, LinuxGeneral
from diagrams.generic.blank import Blank  # Invisible layout node
```

### AWS (Top Services)
```python
from diagrams.aws.compute import EC2, ECS, Lambda, Fargate, EKS
from diagrams.aws.database import RDS, Aurora, Dynamodb, ElastiCache
from diagrams.aws.network import ELB, Route53, CloudFront, VPC, APIGateway
from diagrams.aws.storage import S3, EFS
from diagrams.aws.security import Cognito, WAF, IAM, KMS
from diagrams.aws.integration import SQS, SNS, Eventbridge, StepFunctions
from diagrams.aws.management import Cloudwatch, AutoScaling
from diagrams.aws.analytics import Kinesis, Athena, Glue
from diagrams.aws.general import Users, Client
```

### Azure (Top Services)
```python
from diagrams.azure.compute import VM, FunctionApps, ContainerInstances, KubernetesServices
from diagrams.azure.database import CosmosDb, SQLDatabases, CacheForRedis
from diagrams.azure.network import LoadBalancers, ApplicationGateway, DNS, VirtualNetworks
from diagrams.azure.storage import BlobStorage, StorageAccounts
from diagrams.azure.security import KeyVaults, ActiveDirectory
from diagrams.azure.web import AppServices
```

### GCP (Top Services)
```python
from diagrams.gcp.compute import GCE, GKE, Functions, Run, AppEngine
from diagrams.gcp.database import SQL as GcpSQL, Spanner, Firestore, Memorystore
from diagrams.gcp.network import LoadBalancing, CDN, DNS as GcpDNS, VPC as GcpVPC
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery, PubSub, Dataflow
```

### Kubernetes
```python
from diagrams.k8s.compute import Pod, Deployment, StatefulSet, ReplicaSet, DaemonSet
from diagrams.k8s.network import Ingress, Service, NetworkPolicy
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.k8s.infra import Node as K8sNode, Master
from diagrams.k8s.clusterconfig import HPA, ConfigMap, Secret
```

### On-Premise (Top Tools)
```python
# Web / Proxy
from diagrams.onprem.network import Nginx, HAProxy, Traefik, Istio, Kong
# Databases
from diagrams.onprem.database import PostgreSQL, MySQL, MongoDB, Redis as OnPremRedis
from diagrams.onprem.database import Cassandra, Neo4J, InfluxDB, Clickhouse
# Queues
from diagrams.onprem.queue import Kafka, RabbitMQ, Celery, Nats
# Containers & CI/CD
from diagrams.onprem.container import Docker
from diagrams.onprem.ci import Jenkins, GithubActions, GitlabCI
from diagrams.onprem.gitops import ArgoCD, Flux
# Monitoring
from diagrams.onprem.monitoring import Prometheus, Grafana, Datadog
from diagrams.onprem.logging import Loki, Fluentbit
# IAC & VCS
from diagrams.onprem.iac import Terraform, Ansible
from diagrams.onprem.vcs import Git, Github, Gitlab
```

### Custom Icons
```python
from diagrams.custom import Custom
my_service = Custom("My Service", "./path/to/icon.png")
```

### C4 Model
```python
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship
```

---

## How to Use This Reference

1. **Start here** — Check the Quick Start section above for common icons
2. **Need more?** — Open the specific provider file from the Provider Files table
3. **Custom icons** — Use `diagrams.custom.Custom` with any local PNG/JPG

**Import pattern:** `from diagrams.<provider>.<category> import <ClassName>`

**Naming aliases:** Some classes have short aliases (e.g., `EC2` = `EC2Instance`, `ELB` = `ElasticLoadBalancing`). Check the provider file for the full list.

---

*2634 icons across 17 providers — auto-generated from the installed `diagrams` Python package.*
