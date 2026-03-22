import asyncio
from echo_env import EchoEnv, CallToolAction, ListToolsAction

async def main():
    # Option 1: Use hosted HuggingFace space (no Docker needed)
    async with EchoEnv(base_url="https://openenv-echo-env.hf.space") as client:

        # Reset
        result = await client.reset()
        print(f"Reset: {result}")

        # List available tools first
        tools = await client.step(ListToolsAction())
        print(f"Available tools: {tools}")

        # Send multiple messages using echo_message tool
        messages = ["Hello, World!", "Testing echo", "Final message"]

        for msg in messages:
            result = await client.step(CallToolAction(
                name="echo_message",
                arguments={"message": msg}
            ))
            print(f"Sent: '{msg}'")
            print(f"  → Result: {result}")
            print(f"  → Reward: {result.reward}")

asyncio.run(main())