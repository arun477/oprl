import asyncio
from echo_env import EchoEnv, CallToolAction

async def main():
    async with EchoEnv(base_url="http://localhost:8001") as client:

        result = await client.reset()
        print(f"Reset: {result}")

        messages = ["Hello, World!", "Testing echo", "Final message"]
        for msg in messages:
            result = await client.call_tool("echo_message", message=msg)
            print(f"Sent: '{msg}' → Result: {result}")

asyncio.run(main())