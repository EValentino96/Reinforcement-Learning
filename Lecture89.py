import gymnasium as gym
import time
#import matplotlib.pyplot as plt
#from IPython.display import clear_output, display

env_name = "MountainCar-v0"
env = gym.make(env_name, render_mode='human')

observation = env.reset()[0]
total_steps = 600

def simple_agent(observation):
    #print(observation)
    # Observation
    position = observation[0]
    velocity = observation[1]

    # When to go right -->
    if -0.1 < position < 0.4:
        action = 2

    # When to go left -->
    elif velocity < 0 and position < -0.2:
        action = 0

    # When to not do anything
    else:
        action = 1

    return action

for step in range(total_steps):

    env.render()

    # 0 <--
    # 1 stays put
    # 2 -->
    # action = 2 # Our cart goes to the right
    action = simple_agent(observation)

    observation, reward, done, boo, info = env.step(action)

    #print(f"Observation: {observation}")
    
    time.sleep(0.05)

    if done:
        break
        observation = env.reset()[0]

env.close()
