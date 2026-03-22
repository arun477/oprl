import requests

BASE_URL = "http://localhost:8001"

# Reset
res = requests.post(f"{BASE_URL}/reset", json={})
print("Reset:", res.json())

# Step with correct action format
messages = ["Hello, World!", "Testing echo", "Final message"]
for msg in messages:
    res = requests.post(f"{BASE_URL}/step", json={
        "action": {
            "type": "call_tool",
            "tool_name": "echo_message",
            "arguments": {"message": msg}
        }
    })
    data = res.json()
    print(f"Sent: '{msg}'")
    print(f"  → Raw response: {data}")  # print everything first to see structure