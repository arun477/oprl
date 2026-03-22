from my_echo_env import MyEchoEnv, CounterAction


env = MyEchoEnv(base_url="http://localhost:8000").sync()
with env:
    result = env.reset()
    print("Reset. Count:", result.observation.count)
    for i in range(10):
        result = env.step(CounterAction(action="increment"))
        print(f"Step {i+1}: count={result.observation.count}, reward={result.reward}, done={result.done}")