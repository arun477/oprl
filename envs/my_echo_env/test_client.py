from my_echo_env import MyEchoEnv, CounterAction


env = MyEchoEnv(base_url="http://localhost:8000").sync()
with env:
    result = env.reset()
    print("Reset:", result.observation.echoed_message)
    result = env.step(CounterAction(action="increment"))
    print("Echo:", result.observation.echoed_message)
    print("Length:", result.observation.message_length)
    print("Reward:", result.reward)