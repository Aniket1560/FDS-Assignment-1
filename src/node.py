# src/node.py
import asyncio
import json
import os
from crypto_utils import generate_keys, sign_message, verify_signature

class ConsensusNode:
    def __init__(self, node_id, peers, mode='A'):
        self.node_id = node_id
        self.peers = peers
        self.mode = mode # 'A' for Paxos, 'B' for PBFT
        self.private_key, self.public_key = generate_keys()
        self.ledger = []
        self.is_leader = False
        
    async def start(self):
        print(f"Node {self.node_id} starting in Mode {self.mode}")
        asyncio.create_task(self.heartbeat_sender())
        # Server listening logic goes here...

    async def heartbeat_sender(self):
        while True:
            if self.is_leader:
                # Broadcast heartbeat to peers
                pass
            await asyncio.sleep(1)

    # Mode A: Paxos Implementation 
    async def paxos_prepare(self, proposal_id):
        # Implement Prepare phase
        pass

    async def paxos_promise(self, proposal_id):
        # Implement Promise phase
        pass

    async def paxos_accept(self, proposal_id, value):
        # Implement Accept phase
        pass

    async def paxos_accepted(self, proposal_id, value):
        # Implement Accepted phase. Log to disk upon consensus.
        self.log_to_disk(value)

    # Mode B: PBFT Implementation 
    async def pbft_pre_prepare(self, request):
        # Implement Pre-prepare
        pass

    async def pbft_prepare(self, request):
        # Implement Prepare with signature verification
        pass

    async def pbft_commit(self, request):
        # Implement Commit with signature verification
        self.log_to_disk(request['payload'])

    def log_to_disk(self, transaction):
        with open(f"ledger_{self.node_id}.log", "a") as f:
            f.write(f"{transaction}\n")

if __name__ == "__main__":
    node_id = os.getenv("NODE_ID")
    mode = os.getenv("MODE", "A")
    node = ConsensusNode(node_id, [], mode)
    asyncio.run(node.start())