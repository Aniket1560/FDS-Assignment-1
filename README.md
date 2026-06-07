# Distributed Consensus Engine (Paxos & PBFT)

This repository contains a resilient distributed state machine capable of enduring both benign (crash) faults and malicious (Byzantine) faults. The system is designed to maintain a consistent, append-only transaction ledger across a cluster of 5 nodes.

Video Link : https://youtu.be/z84yB7ex_Og

## Architecture
The system features two distinct operational modes:
* **Mode A (Crash-Fault Tolerance):** Utilizes Leader Election and Basic Paxos to withstand up to 2 simultaneous node crashes.
* **Mode B (Byzantine-Fault Tolerance):** Utilizes Practical Byzantine Fault Tolerance (PBFT) with RSA-based cryptographic signatures to remain resilient against 1 malicious (Byzantine) node.



## Project Structure
```text
├── src/
│   ├── node.py          # Main daemon (Leader Election, Paxos, PBFT)
│   ├── adversary.py     # Byzantine node simulating malicious faults
│   ├── client.py        # Client workload simulator
│   └── crypto_utils.py  # RSA key generation and message signing
├── tests/
│   └── chaos_test.sh    # Script to trigger network faults via Toxiproxy
├── Dockerfile           # Node container configuration
├── docker-compose.yml   # Cluster orchestration
└── project_report.pdf   # Comprehensive architecture and evaluation report
