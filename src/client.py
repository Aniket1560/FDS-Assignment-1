# src/client.py
import asyncio
import time

async def submit_transactions():
    transaction_id = 1
    while True:
        payload = f"TXN_{transaction_id}_DATA"
        print(f"Client submitting: {payload}")
        # Network call to leader node here
        transaction_id += 1
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(submit_transactions())