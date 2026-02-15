"""
Cisco-Style Network Topology Diagram
=====================================
Multi-tier enterprise network with Internet gateway, security perimeter,
core routing, distribution/access switching, and server infrastructure.
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Router, Switch, Firewall, Subnet
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server
from diagrams.generic.storage import Storage
from diagrams.generic.device import Mobile

# Diagram configuration
graph_attr = {
    "fontsize": "16",
    "bgcolor": "#ffffff",
    "pad": "0.8",
    "nodesep": "1.0",
    "ranksep": "1.2",
    "splines": "spline",
}

with Diagram(
    "Enterprise Network Topology",
    filename="cisco-topology",
    outformat="png",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):

    # Internet/Cloud Gateway
    internet = Internet("Internet")

    # Edge Security
    with Cluster("DMZ / Edge Security", graph_attr={
        "bgcolor": "#ffe6e6",
        "style": "rounded",
        "color": "#cc0000",
        "penwidth": "2.0"
    }):
        firewall = Firewall("Edge Firewall")

    # Core Network
    with Cluster("Core Layer", graph_attr={
        "bgcolor": "#e6f3ff",
        "style": "rounded",
        "color": "#0066cc",
        "penwidth": "2.0"
    }):
        core_router = Router("Core Router")

    # Distribution Layer
    with Cluster("Distribution Layer", graph_attr={
        "bgcolor": "#fff9e6",
        "style": "rounded",
        "color": "#cc9900",
        "penwidth": "2.0"
    }):
        dist_switch_1 = Switch("Dist Switch 1")
        dist_switch_2 = Switch("Dist Switch 2")

    # Access Layer
    with Cluster("Access Layer", graph_attr={
        "bgcolor": "#e6ffe6",
        "style": "rounded",
        "color": "#009900",
        "penwidth": "2.0"
    }):
        access_switch_1 = Switch("Access SW 1")
        access_switch_2 = Switch("Access SW 2")
        access_switch_3 = Switch("Access SW 3")

    # Server Farm
    with Cluster("Data Center / Server Farm", graph_attr={
        "bgcolor": "#f0e6ff",
        "style": "rounded",
        "color": "#6600cc",
        "penwidth": "2.0"
    }):
        web_server = Server("Web Server")
        app_server = Server("App Server")
        db_server = Server("Database Server")
        storage = Storage("Network Storage")

    # End Users
    with Cluster("End Users", graph_attr={
        "bgcolor": "#f5f5f5",
        "style": "rounded",
        "color": "#666666",
        "penwidth": "2.0"
    }):
        workstation_1 = Mobile("Workstation 1")
        workstation_2 = Mobile("Workstation 2")
        workstation_3 = Mobile("Workstation 3")

    # Network Connections

    # Internet to Firewall
    internet >> Edge(label="WAN", color="red", style="bold") >> firewall

    # Firewall to Core Router
    firewall >> Edge(label="Trusted", color="blue", style="solid") >> core_router

    # Core Router to Distribution Switches (redundant paths)
    core_router >> Edge(label="Trunk", color="navy", style="solid") >> dist_switch_1
    core_router >> Edge(label="Trunk", color="navy", style="solid") >> dist_switch_2

    # Distribution to Access Switches (redundant uplinks)
    dist_switch_1 >> Edge(color="orange", style="solid") >> access_switch_1
    dist_switch_1 >> Edge(color="orange", style="solid") >> access_switch_2
    dist_switch_2 >> Edge(color="orange", style="solid") >> access_switch_2
    dist_switch_2 >> Edge(color="orange", style="solid") >> access_switch_3

    # Distribution to Server Farm (direct connection for performance)
    dist_switch_1 >> Edge(label="10Gb Fiber", color="purple", style="bold") >> web_server
    dist_switch_2 >> Edge(label="10Gb Fiber", color="purple", style="bold") >> app_server

    # Server Farm Internal Connections
    web_server >> Edge(label="HTTP/API", color="green", style="solid") >> app_server
    app_server >> Edge(label="SQL", color="darkred", style="solid") >> db_server
    db_server >> Edge(label="iSCSI", color="brown", style="dashed") >> storage
    app_server >> Edge(label="NFS/SMB", color="brown", style="dotted") >> storage

    # Access Switches to End Users
    access_switch_1 >> Edge(label="1Gb", color="gray", style="solid") >> workstation_1
    access_switch_2 >> Edge(label="1Gb", color="gray", style="solid") >> workstation_2
    access_switch_3 >> Edge(label="1Gb", color="gray", style="solid") >> workstation_3
