#!/usr/bin/env python3
"""
Cisco-Style Network Topology Diagram

Demonstrates: Generic network icons (Router, Switch, Firewall, VPN, Subnet),
clusters for network zones, edge styling, and direction control.
"""

import os
from diagrams import Cluster, Diagram, Edge
from diagrams.generic.network import Firewall, Router, Switch, Subnet, VPN
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.generic.storage import Storage

# Allow overriding output settings via environment
outformat = os.environ.get("DIAGRAM_OUTFORMAT", "png")
name = os.environ.get("DIAGRAM_NAME", "cisco-network")

graph_attr = {
    "fontsize": "16",
    "bgcolor": "#f8f9fa",
    "pad": "0.5",
    "nodesep": "0.8",
    "ranksep": "1.0",
}

with Diagram(
    "Enterprise Network Topology",
    filename=name,
    outformat=outformat,
    show=False,
    direction="TB",
    graph_attr=graph_attr,
):
    # Internet / WAN
    internet = Router("Internet\nGateway")
    vpn = VPN("Site-to-Site\nVPN")

    with Cluster("DMZ"):
        fw_ext = Firewall("External\nFirewall")
        dmz_switch = Switch("DMZ Switch")
        web_servers = [Rack("Web-01"), Rack("Web-02")]

    with Cluster("Internal Network"):
        fw_int = Firewall("Internal\nFirewall")
        core_switch = Switch("Core Switch\nL3")

        with Cluster("Server Farm"):
            app_switch = Switch("App Switch")
            app_servers = [Rack("App-01"), Rack("App-02"), Rack("App-03")]

        with Cluster("Database Zone"):
            db_switch = Switch("DB Switch")
            db_primary = SQL("DB Primary")
            db_replica = SQL("DB Replica")
            san = Storage("SAN Storage")

        with Cluster("Management"):
            mgmt_subnet = Subnet("Mgmt Subnet\n10.0.100.0/24")

    # --- Connections ---
    # WAN to DMZ
    internet >> Edge(color="red", style="bold") >> fw_ext
    vpn >> Edge(color="blue", style="dashed", label="IPSec") >> fw_ext

    # DMZ internal
    fw_ext >> dmz_switch
    for ws in web_servers:
        dmz_switch >> Edge(color="darkgreen") >> ws

    # DMZ to Internal
    dmz_switch >> Edge(color="orange", label="Filtered") >> fw_int

    # Internal core
    fw_int >> core_switch

    # Core to Server Farm
    core_switch >> Edge(color="navy") >> app_switch
    for app in app_servers:
        app_switch >> app

    # Core to Database Zone
    core_switch >> Edge(color="purple") >> db_switch
    db_switch >> db_primary
    db_switch >> db_replica
    db_primary >> Edge(color="gray", style="dashed", label="Replication") >> db_replica
    db_primary >> Edge(color="brown", label="iSCSI") >> san

    # Core to Management
    core_switch >> Edge(color="teal", style="dotted") >> mgmt_subnet
