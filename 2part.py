import requests

BASE_URL = "http://localhost:8001"

# Reset
res = requests.post(f"{BASE_URL}/reset", json={})
print("Reset:", res.json())

# Step
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
    obs = data["observation"]
    echoed = obs["result"]["data"]        # the echoed text
    is_error = obs["result"]["is_error"]  # error flag

    print(f"Sent:   '{msg}'")
    print(f"Echoed: '{echoed}'")
    print(f"Error:  {is_error}")
    print(f"Done:   {data['done']}")
    print()

# Final state
state = requests.get(f"{BASE_URL}/state").json()
print("Final state:", state)