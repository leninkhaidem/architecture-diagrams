# Kubernetes Icons

Complete Kubernetes resource icon catalog.

**Total:** 69 icons across 8 categories

**Import pattern:** `from diagrams.k8s.<category> import <ClassName>`

---
### Chaos Engineering

**Import:** `from diagrams.k8s.chaos import ...`

| Class Name | Import Example |
|------------|---------------|
| `ChaosMesh` | `from diagrams.k8s.chaos import ChaosMesh` |
| `LitmusChaos` | `from diagrams.k8s.chaos import LitmusChaos` |

### Cluster Config

**Import:** `from diagrams.k8s.clusterconfig import ...`

| Class Name | Import Example |
|------------|---------------|
| `HPA` | `from diagrams.k8s.clusterconfig import HPA` |
| `HorizontalPodAutoscaler` | `from diagrams.k8s.clusterconfig import HorizontalPodAutoscaler` |
| `LimitRange` | `from diagrams.k8s.clusterconfig import LimitRange` |
| `Limits` | `from diagrams.k8s.clusterconfig import Limits` |
| `Quota` | `from diagrams.k8s.clusterconfig import Quota` |

### Compute

**Import:** `from diagrams.k8s.compute import ...`

| Class Name | Import Example |
|------------|---------------|
| `Cronjob` | `from diagrams.k8s.compute import Cronjob` |
| `DS` | `from diagrams.k8s.compute import DS` |
| `DaemonSet` | `from diagrams.k8s.compute import DaemonSet` |
| `Deploy` | `from diagrams.k8s.compute import Deploy` |
| `Deployment` | `from diagrams.k8s.compute import Deployment` |
| `Job` | `from diagrams.k8s.compute import Job` |
| `Pod` | `from diagrams.k8s.compute import Pod` |
| `RS` | `from diagrams.k8s.compute import RS` |
| `ReplicaSet` | `from diagrams.k8s.compute import ReplicaSet` |
| `STS` | `from diagrams.k8s.compute import STS` |
| `StatefulSet` | `from diagrams.k8s.compute import StatefulSet` |

### Control Plane

**Import:** `from diagrams.k8s.controlplane import ...`

| Class Name | Import Example |
|------------|---------------|
| `API` | `from diagrams.k8s.controlplane import API` |
| `APIServer` | `from diagrams.k8s.controlplane import APIServer` |
| `CCM` | `from diagrams.k8s.controlplane import CCM` |
| `CM` | `from diagrams.k8s.controlplane import CM` |
| `ControllerManager` | `from diagrams.k8s.controlplane import ControllerManager` |
| `KProxy` | `from diagrams.k8s.controlplane import KProxy` |
| `KubeProxy` | `from diagrams.k8s.controlplane import KubeProxy` |
| `Kubelet` | `from diagrams.k8s.controlplane import Kubelet` |
| `Sched` | `from diagrams.k8s.controlplane import Sched` |
| `Scheduler` | `from diagrams.k8s.controlplane import Scheduler` |

### Ecosystem

**Import:** `from diagrams.k8s.ecosystem import ...`

| Class Name | Import Example |
|------------|---------------|
| `ExternalDns` | `from diagrams.k8s.ecosystem import ExternalDns` |
| `Helm` | `from diagrams.k8s.ecosystem import Helm` |
| `Krew` | `from diagrams.k8s.ecosystem import Krew` |
| `Kustomize` | `from diagrams.k8s.ecosystem import Kustomize` |

### Group

**Import:** `from diagrams.k8s.group import ...`

| Class Name | Import Example |
|------------|---------------|
| `NS` | `from diagrams.k8s.group import NS` |
| `Namespace` | `from diagrams.k8s.group import Namespace` |

### Infrastructure

**Import:** `from diagrams.k8s.infra import ...`

| Class Name | Import Example |
|------------|---------------|
| `ETCD` | `from diagrams.k8s.infra import ETCD` |
| `Master` | `from diagrams.k8s.infra import Master` |
| `Node` | `from diagrams.k8s.infra import Node` |

### Network

**Import:** `from diagrams.k8s.network import ...`

| Class Name | Import Example |
|------------|---------------|
| `Endpoint` | `from diagrams.k8s.network import Endpoint` |
| `Ep` | `from diagrams.k8s.network import Ep` |
| `Ing` | `from diagrams.k8s.network import Ing` |
| `Ingress` | `from diagrams.k8s.network import Ingress` |
| `Netpol` | `from diagrams.k8s.network import Netpol` |
| `NetworkPolicy` | `from diagrams.k8s.network import NetworkPolicy` |
| `SVC` | `from diagrams.k8s.network import SVC` |
| `Service` | `from diagrams.k8s.network import Service` |

### Others

**Import:** `from diagrams.k8s.others import ...`

| Class Name | Import Example |
|------------|---------------|
| `CRD` | `from diagrams.k8s.others import CRD` |
| `PSP` | `from diagrams.k8s.others import PSP` |

### Pod Config

**Import:** `from diagrams.k8s.podconfig import ...`

| Class Name | Import Example |
|------------|---------------|
| `CM` | `from diagrams.k8s.podconfig import CM` |
| `ConfigMap` | `from diagrams.k8s.podconfig import ConfigMap` |
| `Secret` | `from diagrams.k8s.podconfig import Secret` |

### RBAC

**Import:** `from diagrams.k8s.rbac import ...`

| Class Name | Import Example |
|------------|---------------|
| `CRB` | `from diagrams.k8s.rbac import CRB` |
| `CRole` | `from diagrams.k8s.rbac import CRole` |
| `ClusterRole` | `from diagrams.k8s.rbac import ClusterRole` |
| `ClusterRoleBinding` | `from diagrams.k8s.rbac import ClusterRoleBinding` |
| `Group` | `from diagrams.k8s.rbac import Group` |
| `RB` | `from diagrams.k8s.rbac import RB` |
| `Role` | `from diagrams.k8s.rbac import Role` |
| `RoleBinding` | `from diagrams.k8s.rbac import RoleBinding` |
| `SA` | `from diagrams.k8s.rbac import SA` |
| `ServiceAccount` | `from diagrams.k8s.rbac import ServiceAccount` |
| `User` | `from diagrams.k8s.rbac import User` |

### Storage

**Import:** `from diagrams.k8s.storage import ...`

| Class Name | Import Example |
|------------|---------------|
| `PV` | `from diagrams.k8s.storage import PV` |
| `PVC` | `from diagrams.k8s.storage import PVC` |
| `PersistentVolume` | `from diagrams.k8s.storage import PersistentVolume` |
| `PersistentVolumeClaim` | `from diagrams.k8s.storage import PersistentVolumeClaim` |
| `SC` | `from diagrams.k8s.storage import SC` |
| `StorageClass` | `from diagrams.k8s.storage import StorageClass` |
| `Vol` | `from diagrams.k8s.storage import Vol` |
| `Volume` | `from diagrams.k8s.storage import Volume` |

