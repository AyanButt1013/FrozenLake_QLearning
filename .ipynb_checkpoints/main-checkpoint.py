import gym
env = gym.make("Taxi-v3",render_mode="rgb_array").env
env.reset()
env.render()