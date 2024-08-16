import gymnasium as gym
import time

env = gym.make('Breakout-v4', render_mode='human')

# Go for N many frames
env.reset()
total_steps = 200

for step in range(total_steps):

    # Generate environment
    env.render()

    # Grab random action!
    random_action = env.action_space.sample()

    # Actually use the random action on the environment
    # Keep in mind since we're grabbing random action,
    # our first action might not start the game! Since,
    # you need to press the "spacebar" to start the game.
    observation, reward, done, boo, info = env.step(random_action)

    #clear_output(wait=True)
    #plt.imshow(observation)
    #display(plt.gcf())
    
    # Show some of our information
    print(f'Reward: {reward}')
    print(f'Done: {done}')
    print(f'Info: {info}')

    if done:
        break
    
    time.sleep(0.05)

# Close the environment once we're done interacting with it.
env.close()
