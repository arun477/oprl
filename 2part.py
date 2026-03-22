import requests

BASE_URL = "http://localhost:8001"

# Reset
res = requests.post(f"{BASE_URL}/reset", json={})
print("Reset:", res.json())

# Check action schema
schema = requests.get(f"{BASE_URL}/schema").json()
print("Action schema:", schema["action"])

# Step with a message
messages = ["Hello, World!", "Testing echo", "Final message"]
for msg in messages:
    res = requests.post(f"{BASE_URL}/step", json={"action": {"message": msg}})
    data = res.json()
    print(f"Sent: '{msg}'")
    print(f"  → Observation: {data['observation']}")
    print(f"  → Reward: {data['reward']}")
    print(f"  → Done: {data['done']}")

# Check state
state = requests.get(f"{BASE_URL}/state").json()
print("State:", state)