import asyncio
from echo_env import EchoAction, EchoEnv

async def main():
    # Create environment from Docker image
    client = await EchoEnv.from_docker_image("echo-env:latest")

    async with client:
        # Reset
        result = await client.reset()
        print(f"Reset: {result.observation.echoed_message}")

        # Send multiple messages
        messages = ["Hello, World!", "Testing echo", "Final message"]

        for msg in messages:
            result = await client.step(EchoAction(message=msg))
            print(f"Sent: '{msg}'")
            print(f"  → Echoed: '{result.observation.echoed_message}'")
            print(f"  → Length: {result.observation.message_length}")
            print(f"  → Reward: {result.reward}")

asyncio.run(main())