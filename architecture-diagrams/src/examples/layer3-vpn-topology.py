"""
Layer 3 VPN Network Topology Diagram

Shows enterprise VPN architecture with:
- Headquarters with servers and VPN concentrator
- Two branch offices with routers
- Remote workers with SSL VPN
- IPsec/MPLS VPN tunnels
- Color-coded clusters per site
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Router, VPN, Firewall, Switch, Subnet
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.os import Windows
from diagrams.onprem.database import PostgreSQL

# Graph styling
graph_attr = {
    "fontsize": "16",
    "bgcolor": "#ffffff",
    "pad": "0.8",
    "nodesep": "1.0",
    "ranksep": "1.2",
    "splines": "curved",
}

with Diagram(
    "Layer 3 VPN Network Topology",
    filename="layer3-vpn-topology",
    outformat="png",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):

    # Internet Cloud (central hub)
    internet = Internet("Internet\nCloud")

    # ===== HEADQUARTERS CLUSTER =====
    with Cluster("Headquarters - Main Office", graph_attr={
        "bgcolor": "#e3f2fd",
        "style": "rounded",
        "color": "#1976d2",
        "penwidth": "2.5",
        "fontsize": "14",
        "fontcolor": "#1565c0",
    }):

        # VPN Concentrator / Firewall
        hq_vpn_gateway = VPN("VPN Concentrator\n& Firewall")
        hq_router = Router("HQ Core\nRouter")
        hq_switch = Switch("Core Switch")

        # Internal Servers
        with Cluster("Server Farm", graph_attr={
            "bgcolor": "#fff3e0",
            "style": "rounded",
            "color": "#f57c00",
            "penwidth": "1.5",
        }):
            file_server = Server("File Server")
            app_server = Server("Application\nServer")
            db_server = PostgreSQL("Database\nServer")

        # HQ Users
        with Cluster("HQ Users", graph_attr={
            "bgcolor": "#f1f8e9",
            "style": "rounded",
            "color": "#689f38",
            "penwidth": "1.5",
        }):
            hq_users = Windows("HQ Workstations")

        # HQ internal connections
        hq_vpn_gateway >> Edge(color="#333333", style="solid") >> hq_router
        hq_router >> Edge(color="#333333", style="solid") >> hq_switch
        hq_switch >> Edge(color="#666666", style="solid") >> [file_server, app_server, db_server]
        hq_switch >> Edge(color="#666666", style="solid") >> hq_users

    # ===== BRANCH OFFICE 1 CLUSTER =====
    with Cluster("Branch Office 1", graph_attr={
        "bgcolor": "#f3e5f5",
        "style": "rounded",
        "color": "#7b1fa2",
        "penwidth": "2.5",
        "fontsize": "14",
        "fontcolor": "#6a1b9a",
    }):
        branch1_router = Router("Branch 1\nRouter")
        branch1_switch = Switch("Branch 1\nSwitch")
        branch1_server = Server("Local\nFile Server")
        branch1_users = Windows("Branch 1\nUsers")

        # Branch 1 internal connections
        branch1_router >> Edge(color="#333333", style="solid") >> branch1_switch
        branch1_switch >> Edge(color="#666666", style="solid") >> [branch1_server, branch1_users]

    # ===== BRANCH OFFICE 2 CLUSTER =====
    with Cluster("Branch Office 2", graph_attr={
        "bgcolor": "#fce4ec",
        "style": "rounded",
        "color": "#c2185b",
        "penwidth": "2.5",
        "fontsize": "14",
        "fontcolor": "#ad1457",
    }):
        branch2_router = Router("Branch 2\nRouter")
        branch2_switch = Switch("Branch 2\nSwitch")
        branch2_server = Server("Local\nFile Server")
        branch2_users = Windows("Branch 2\nUsers")

        # Branch 2 internal connections
        branch2_router >> Edge(color="#333333", style="solid") >> branch2_switch
        branch2_switch >> Edge(color="#666666", style="solid") >> [branch2_server, branch2_users]

    # ===== REMOTE WORKERS CLUSTER =====
    with Cluster("Remote Workers", graph_attr={
        "bgcolor": "#e0f2f1",
        "style": "rounded",
        "color": "#00897b",
        "penwidth": "2.5",
        "fontsize": "14",
        "fontcolor": "#00695c",
    }):
        remote_laptop = Mobile("Remote\nLaptop")
        remote_tablet = Tablet("Remote\nTablet")
        remote_home = Windows("Home Office\nWorkstation")

    # ===== VPN CONNECTIONS TO INTERNET =====

    # HQ to Internet
    hq_vpn_gateway >> Edge(
        label="Primary Link\n100 Mbps",
        color="#1976d2",
        style="solid",
        penwidth="2.5"
    ) >> internet

    # Branch 1 to Internet (IPsec VPN)
    branch1_router >> Edge(
        label="IPsec Tunnel\n50 Mbps",
        color="#7b1fa2",
        style="dashed",
        penwidth="2.5"
    ) >> internet

    # Branch 2 to Internet (MPLS VPN)
    branch2_router >> Edge(
        label="MPLS VPN\n50 Mbps",
        color="#c2185b",
        style="dashed",
        penwidth="2.5"
    ) >> internet

    # Remote Workers to Internet (SSL VPN)
    remote_laptop >> Edge(
        label="SSL VPN",
        color="#00897b",
        style="dotted",
        penwidth="2.0"
    ) >> internet

    remote_tablet >> Edge(
        label="SSL VPN",
        color="#00897b",
        style="dotted",
        penwidth="2.0"
    ) >> internet

    remote_home >> Edge(
        label="SSL VPN",
        color="#00897b",
        style="dotted",
        penwidth="2.0"
    ) >> internet

    # ===== VPN TUNNELS (Internet to HQ) =====
    # These represent the encrypted tunnels terminating at HQ

    internet >> Edge(
        label="IPsec Tunnel",
        color="#7b1fa2",
        style="dashed",
        penwidth="2.5"
    ) >> hq_vpn_gateway

    internet >> Edge(
        label="MPLS VPN",
        color="#c2185b",
        style="dashed",
        penwidth="2.5"
    ) >> hq_vpn_gateway

    internet >> Edge(
        label="SSL VPN\n(Remote Workers)",
        color="#00897b",
        style="dotted",
        penwidth="2.0"
    ) >> hq_vpn_gateway
