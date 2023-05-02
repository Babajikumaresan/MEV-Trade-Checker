#simple program to monitor the mempool using blocknative 
#Author Babaji Kumaresan
#get a key from blocknative and you are good to go.

import asyncio
import websockets
import json
import datetime

async def token_transfers(api_key, token_contract_address):
    async with websockets.connect("wss://api.blocknative.com/v0/ws") as websocket:
        subscription_payload = {
            "action": "subscribe",
            "type": "token",
            "options": {
                "eventName": "Transfer",
                "tokenAddress": token_contract_address
            },
            "dappId": api_key,
            "network": "main",
            "timeStamp": datetime.datetime.utcnow().isoformat(),
            "version": "1.0.0"
        }
        await websocket.send(json.dumps(subscription_payload))

        while True:
            response = await websocket.recv()
            print(f"Received: {response}")

# Replace these placeholders with your actual values
YOUR_API_KEY = "" #blocknative api key
TOKEN_CONTRACT_ADDRESS = "0x6982508145454Ce325dDbE47a25d4ec3d2311933"

asyncio.get_event_loop().run_until_complete(pepe_token_transfers(YOUR_API_KEY, TOKEN_CONTRACT_ADDRESS))
