#!/usr/bin/env python3
"""
Kubernetes Cluster Architecture Diagram

Demonstrates: K8s provider icons, cluster hierarchy, ingress flow,
service mesh, persistent storage, and monitoring stack.
"""

import os
from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod, StatefulSet, Deployment, ReplicaSet, Job
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.k8s.rbac import ServiceAccount
from diagrams.k8s.infra import Node
from diagrams.k8s.clusterconfig import HPA
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.logging import Loki
from diagrams.onprem.network import Nginx, Istio
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka
from diagrams.onprem.inmemory import Redis

outformat = os.environ.get("DIAGRAM_OUTFORMAT", "png")
name = os.environ.get("DIAGRAM_NAME", "kubernetes-cluster")

graph_attr = {
    "fontsize": "14",
    "bgcolor": "#f0f4f8",
    "pad": "0.5",
    "nodesep": "0.5",
    "ranksep": "0.8",
}

with Diagram(
    "Kubernetes Production Cluster",
    filename=name,
    outformat=outformat,
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    ingress = Nginx("NGINX\nIngress Controller")

    with Cluster("Kubernetes Cluster"):

        with Cluster("Namespace: production"):
            ing = Ingress("Ingress\nRules")
            mesh = Istio("Istio\nService Mesh")

            with Cluster("Frontend"):
                fe_svc = Service("frontend-svc")
                fe_deploy = Deployment("frontend")
                fe_pods = [Pod("fe-pod-1"), Pod("fe-pod-2")]
                fe_hpa = HPA("HPA\nmin:2 max:10")

            with Cluster("Backend API"):
                api_svc = Service("api-svc")
                api_deploy = Deployment("api-server")
                api_pods = [Pod("api-pod-1"), Pod("api-pod-2"), Pod("api-pod-3")]
                api_hpa = HPA("HPA\nmin:3 max:20")

            with Cluster("Workers"):
                worker_deploy = Deployment("workers")
                worker_pods = [Pod("worker-1"), Pod("worker-2")]
                worker_job = Job("cron-job")

        with Cluster("Namespace: data"):
            with Cluster("PostgreSQL HA"):
                pg_svc = Service("postgres-svc")
                pg_sts = StatefulSet("postgres")
                pg_primary = Pod("pg-primary")
                pg_replica = Pod("pg-replica")
                pg_pvc1 = PVC("data-0")
                pg_pvc2 = PVC("data-1")

            redis_svc = Service("redis-svc")
            redis = Redis("Redis\nCache")

            kafka_svc = Service("kafka-svc")
            kafka = Kafka("Kafka\nEvents")

        with Cluster("Namespace: monitoring"):
            prom = Prometheus("Prometheus")
            grafana = Grafana("Grafana")
            loki = Loki("Loki\nLogs")

        with Cluster("Storage"):
            sc = StorageClass("gp3\nStorageClass")
            pvs = [PV("pv-01"), PV("pv-02"), PV("pv-03")]

    # --- Connections ---
    # Ingress flow
    ingress >> ing >> mesh
    mesh >> fe_svc >> fe_deploy
    fe_deploy >> fe_pods
    fe_hpa >> Edge(style="dashed") >> fe_deploy

    mesh >> api_svc >> api_deploy
    api_deploy >> api_pods
    api_hpa >> Edge(style="dashed") >> api_deploy

    # Backend to workers
    api_svc >> Edge(label="Tasks") >> worker_deploy
    worker_deploy >> worker_pods

    # Data connections
    api_svc >> Edge(color="blue", label="SQL") >> pg_svc >> pg_sts
    pg_sts >> pg_primary
    pg_sts >> pg_replica
    pg_primary >> Edge(style="dashed", label="WAL\nReplication") >> pg_replica

    api_svc >> Edge(color="red", label="Cache") >> redis_svc >> redis
    worker_deploy >> Edge(color="orange", label="Events") >> kafka_svc >> kafka

    # Storage
    pg_pvc1 >> Edge(style="dotted") >> sc
    pg_pvc2 >> Edge(style="dotted") >> sc
    sc >> pvs

    # Monitoring
    prom >> Edge(style="dotted", color="gray") >> grafana
    prom >> Edge(style="dotted", color="gray") >> loki
