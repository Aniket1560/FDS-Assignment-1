# src/adversary.py
from node import ConsensusNode
import asyncio
import os

class AdversaryNode(ConsensusNode):
    def __init__(self, node_id, peers, mode='B'):
        super().__init__(node_id, peers, mode)

    async def pbft_prepare(self, request):
        # Intentional protocol break: Equivocating by sending conflicting payloads [cite: 13, 27]
        print(f"Adversary {self.node_id} equivocating during Prepare phase")
        malicious_request = request.copy()
        malicious_request['payload'] = "FORGED_TRANSACTION"
        # Send original to some peers, forged to others
        pass

    async def pbft_commit(self, request):
        # Intentional protocol break: Suppressing Commit messages 
        print(f"Adversary {self.node_id} suppressing Commit message")
        pass # Drop the message

if __name__ == "__main__":
    node_id = os.getenv("NODE_ID")
    node = AdversaryNode(node_id, [], 'B')
    asyncio.run(node.start())