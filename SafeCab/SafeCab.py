import gym
import SafeCab.SafeCabEnv
import numpy as np
import colorama
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

colorama.init()
env = gym.make('SafeCab-v0')

env.reset()
env.render()
print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))


class Agent:

    def __init__(self, n_states, n_actions, decay=0.0001, learning=0.7, gamma=0.618):
        self.n_actions = n_actions
        self.q_table = np.zeros((n_states, n_actions))
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.epsilon = self.max_epsilon
        self.decay = decay
        self.learning = learning
        self.gamma = gamma
        self.epsilons_ = []

    def choose_action(self, explore=True):
        exploration_tradeoff = np.random.uniform(0, 1)

        if explore and exploration_tradeoff < self.epsilon:  # ! Exploration
            return np.random.randint(self.n_actions)
        else:  # ! Exploitation: choose largest Q value for state.
            return np.argmax(self.q_table[state, :])

    def learn(self, state, action, reward, next_state, done, episode):
        self.q_table[state, action] = self.q_table[state, action] + \
            self.learning * (reward + self.gamma *
                             np.max(self.q_table[next_state, :]) - self.q_table[state, action])

        if done:
            self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon) * \
                np.exp(-self.decay * episode)

            self.epsilons_.append(self.epsilon)


episodes = 60000
test_episodes = 10

agent = Agent(env.observation_space.n, env.action_space.n)

untrained_frames = []

for episode in range(test_episodes):
    state = env.reset()
    step = 1

    while True:
        action = agent.choose_action()

        next_state, reward, done, info = env.step(action)

        untrained_frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'episode': episode,
            'step': step,
            'reward': reward
        })

        if done:
            step = 0
            break

        state = next_state
        step += 1

SafeCab.SafeCabEnv.print_frames(untrained_frames)

rewards = []

for episode in range(episodes):
    state = env.reset()
    episode_rewards = []

    while True:

        action = agent.choose_action()

        next_state, reward, done, info = env.step(action)
        agent.learn(state, action, reward, next_state, done, episode)

        state = next_state
        episode_rewards.append(reward)

        if done == True:
            break

    rewards.append(np.mean(episode_rewards))

plt.plot(savgol_filter(rewards, 1001, 2))
plt.title("Smoothened training reward per episode")
plt.xlabel('Episode')
plt.ylabel('Total Reward')

plt.plot(agent.epsilons_)
plt.title("Epsilon for episode")
plt.xlabel('Episode')
plt.ylabel('Epsilon')

frames = []
rewards = []

for episode in range(test_episodes):
    state = env.reset()
    episode_rewards = []

    step = 1

    while True:
        action = agent.choose_action(explore=False)

        next_state, reward, done, info = env.step(action)

        frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'episode': episode,
            'step': step,
            'reward': reward
        })

        episode_rewards.append(reward)

        if done:
            step = 0
            break

        state = next_state
        step += 1

    rewards.append(np.mean(episode_rewards))

env.close()

plt.plot(rewards)
plt.title("Test reward per episode")
plt.ylim((0, 150))
plt.xlabel('Episode')
plt.ylabel('Total Reward')

SafeCab.SafeCabEnv.print_frames(frames)
