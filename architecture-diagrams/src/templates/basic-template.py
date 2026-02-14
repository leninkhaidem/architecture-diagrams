#!/usr/bin/env python3
"""
Basic Diagram Template

Copy this file and customize for your architecture diagram.
Replace placeholders marked with TODO.
"""

import os
from diagrams import Cluster, Diagram, Edge

# TODO: Import nodes from the appropriate provider
# Examples:
# from diagrams.aws.compute import EC2, Lambda
# from diagrams.generic.network import Router, Switch, Firewall
# from diagrams.k8s.compute import Pod, Deployment
# from diagrams.onprem.database import PostgreSQL
# from diagrams.custom import Custom  # For custom icons

outformat = os.environ.get("DIAGRAM_OUTFORMAT", "png")
name = os.environ.get("DIAGRAM_NAME", "my-diagram")  # TODO: Change name

graph_attr = {
    "fontsize": "14",
    "bgcolor": "#ffffff",  # Background color
    "pad": "0.5",          # Padding around diagram
    "nodesep": "0.6",      # Horizontal spacing between nodes
    "ranksep": "0.8",      # Vertical spacing between ranks
}

with Diagram(
    "My Architecture Diagram",     # TODO: Change title
    filename=name,
    outformat=outformat,
    show=False,                     # Don't auto-open file
    direction="TB",                 # TB, BT, LR, RL
    graph_attr=graph_attr,
):
    # TODO: Define your nodes
    # node1 = EC2("Web Server")
    # node2 = RDS("Database")

    # TODO: Group related nodes
    # with Cluster("Backend Services"):
    #     svc1 = EC2("API")
    #     svc2 = EC2("Worker")

    # TODO: Connect nodes
    # node1 >> Edge(label="HTTPS") >> node2
    # node1 >> [svc1, svc2]

    pass  # Remove this line after adding nodes
