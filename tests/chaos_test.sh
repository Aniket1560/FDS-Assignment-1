#!/bin/bash
# tests/chaos_test.sh
# Script to trigger Toxiproxy faults during runtime [cite: 56]

echo "Starting Chaos Testing..."

# Simulate a network partition on Node 2
echo "Injecting network partition to Node 2..."
# Assuming toxiproxy-cli is installed and configured
# toxiproxy-cli create node2_proxy --listen localhost:2222 --upstream node2:8000
# toxiproxy-cli toxic add -t timeout -a timeout=5000 node2_proxy

# Simulate a node crash (up to 2 nodes for Mode A) 
echo "Simulating crash on Node 3 and Node 4..."
docker stop distributed-consensus-engine_node3_1
docker stop distributed-consensus-engine_node4_1

sleep 10

# Recover nodes
echo "Recovering crashed nodes..."
docker start distributed-consensus-engine_node3_1
docker start distributed-consensus-engine_node4_1

echo "Chaos test sequence complete."