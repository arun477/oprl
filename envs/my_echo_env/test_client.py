from my_echo_env import MyEchoEnv, MyEchoAction


env = MyEchoEnv(base_url="http://localhost:8000").sync()
with env:
    result = env.reset()
    print("Reset:", result.observation.echoed_message)
    result = env.step(MyEchoAction(message="Hello!"))
    print("Echo:", result.observation.echoed_message)
    print("Length:", result.observation.message_length)
    print("Reward:", result.reward)