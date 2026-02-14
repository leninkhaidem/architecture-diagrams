#!/usr/bin/env python3
"""
AWS Cloud Architecture Diagram

Demonstrates: AWS provider icons, multi-AZ deployment, VPC networking,
load balancing, auto-scaling, managed services, and edge labels.
"""

import os
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2, ECS, Lambda
from diagrams.aws.database import RDS, ElastiCache, Dynamodb
from diagrams.aws.network import ELB, Route53, CloudFront, VPC, APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito, WAF
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.general import Users

outformat = os.environ.get("DIAGRAM_OUTFORMAT", "png")
name = os.environ.get("DIAGRAM_NAME", "aws-architecture")

graph_attr = {
    "fontsize": "14",
    "bgcolor": "#ffffff",
    "pad": "0.5",
    "nodesep": "0.6",
    "ranksep": "0.8",
}

with Diagram(
    "AWS Production Architecture",
    filename=name,
    outformat=outformat,
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    users = Users("End Users")
    dns = Route53("Route 53\nDNS")
    cdn = CloudFront("CloudFront\nCDN")
    waf = WAF("AWS WAF")
    auth = Cognito("Cognito\nAuth")

    with Cluster("VPC - 10.0.0.0/16"):
        api_gw = APIGateway("API Gateway")
        alb = ELB("Application\nLoad Balancer")

        with Cluster("Public Subnets"):
            with Cluster("AZ-1a"):
                web1 = EC2("Web Server 1")
            with Cluster("AZ-1b"):
                web2 = EC2("Web Server 2")

        with Cluster("Private Subnets - Application"):
            with Cluster("ECS Cluster"):
                svc_api = ECS("API Service")
                svc_worker = ECS("Worker Service")
            serverless = Lambda("Event\nProcessor")

        with Cluster("Private Subnets - Data"):
            with Cluster("RDS Multi-AZ"):
                db_primary = RDS("PostgreSQL\nPrimary")
                db_standby = RDS("PostgreSQL\nStandby")

            cache = ElastiCache("Redis\nCache")
            dynamo = Dynamodb("DynamoDB\nSessions")

        # Async messaging
        queue = SQS("SQS\nTask Queue")
        notifications = SNS("SNS\nAlerts")

    # Static assets
    static = S3("S3 Static\nAssets")
    monitoring = Cloudwatch("CloudWatch\nMonitoring")

    # --- Connections ---
    users >> dns >> cdn >> waf >> alb
    users >> Edge(style="dashed", label="Auth") >> auth

    alb >> web1
    alb >> web2
    web1 >> api_gw
    web2 >> api_gw

    api_gw >> svc_api
    svc_api >> Edge(label="Read/Write") >> db_primary
    svc_api >> Edge(label="Cache") >> cache
    svc_api >> Edge(label="Sessions") >> dynamo

    db_primary >> Edge(style="dashed", label="Sync\nReplication") >> db_standby

    svc_api >> Edge(label="Enqueue") >> queue
    queue >> svc_worker
    svc_worker >> Edge(label="Events") >> notifications
    notifications >> serverless

    cdn >> Edge(style="dotted", label="Static") >> static
    svc_api >> Edge(style="dotted", color="gray") >> monitoring
    svc_worker >> Edge(style="dotted", color="gray") >> monitoring
