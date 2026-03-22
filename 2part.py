import asyncio
from echo_env import EchoEnv, CallToolAction, ListToolsAction

async def main():
    async with EchoEnv(base_url="http://localhost:8000") as client:  # ← changed this

        result = await client.reset()
        print(f"Reset: {result}")

        tools = await client.step(ListToolsAction())
        print(f"Tools: {tools}")

        messages = ["Hello, World!", "Testing echo", "Final message"]
        for msg in messages:
            result = await client.step(CallToolAction(
                name="echo_message",
                arguments={"message": msg}
            ))
            print(f"Sent: '{msg}' → Result: {result}")

asyncio.run(main())