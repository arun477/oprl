import asyncio
from echo_env import EchoEnv

async def main():
    async with EchoEnv(base_url="http://localhost:8000") as client:

        # Reset
        result = await client.reset()
        print(f"Reset: {result}")

        # List available tools
        tools = await client.list_tools()
        print(f"Tools: {tools}")

        # Send messages using call_tool directly
        messages = ["Hello, World!", "Testing echo", "Final message"]
        for msg in messages:
            result = await client.call_tool("echo_message", message=msg)
            print(f"Sent: '{msg}' → Result: {result}")

asyncio.run(main())