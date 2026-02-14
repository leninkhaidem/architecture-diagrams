# Architecture Diagrams

A portable Claude Agent Skill for generating professional architecture diagrams using the [Diagrams](https://diagrams.mingrammer.com/) Python library with real cloud provider icons (AWS, Azure, GCP, K8s, OnPrem, Generic).

## Installation

### Prerequisites

- Python 3.7+
- Graphviz system binary

```bash
# Ubuntu/Debian
sudo apt install graphviz

# macOS
brew install graphviz
```

### Install as Claude Skill

```bash
# Clone the repo
git clone https://github.com/leninkhaidem/architecture-diagrams.git

# Copy the skill folder to your Claude skills directory
cp -r architecture-diagrams/architecture-diagrams/ ~/.claude/skills/architecture-diagrams/

# Run setup (creates .venv and installs Python dependencies)
cd ~/.claude/skills/architecture-diagrams/
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### Quick Test

```bash
cd ~/.claude/skills/architecture-diagrams/
source .venv/bin/activate
python scripts/generate.py src/examples/cisco-network.py
# Output: output/png/cisco-network.png
```

## Usage

See `architecture-diagrams/SKILL.md` for full documentation including:

- All available node providers and imports
- Cluster/grouping patterns
- Edge styling guide
- Graph attributes reference
- Common diagram patterns
- Troubleshooting

## Examples

- **Cisco Network** — Enterprise topology with DMZ, firewalls, VLANs
- **AWS Architecture** — Production VPC with ALB, ECS, RDS Multi-AZ, CloudFront
- **Kubernetes Cluster** — Namespaces, service mesh, monitoring stack, storage

## License

MIT
