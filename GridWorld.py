"""
Implementation of Grid World for Reinforcement Learning in Python 3.6.4.

"""

import numpy as np

# * Global variables

ROWS, COLS = 3, 4
WIN = (0, 3)
LOSS = (1, 3)
START = (2, 0)
DETERMINISTIC = True

class State:
    def __init__(self, state = START):
        self.board = np.zeros([ROWS, COLS])
        self.ended = False
        self.state = state
        self.deterministic = DETERMINISTIC

    def give_reward(self):
        if self.state == WIN:
            return 1
        elif self.state == LOSS:
            return -1
        else:
            return 0

    def is_end(self):
        if (self.state == WIN) or (self.state == LOSS):
            self.ended = True

    def next_position(self, action):
        if self.deterministic:
            if action == "UP":
                next_state = (self.state[0] - 1, self.state[1])
            elif action == "DOWN":
                next_state = (self.state[0] + 1, self.state[1])
            elif action == "LEFT":
                next_state = (self.state[0], self.state[1] - 1)
            elif action == "RIGHT":
                next_state = (self.state[0], self.state[1] + 1)

            if (next_state[0] >= 0) and (next_state[0] <= 2):
                if (next_state[1] >= 0) and (next_state[1] <= 3):
                    if next_state != (1, 1):
                        return next_state
            return self.state

    def display(self):
        self.board[self.state] = 1
        output = "|"
        
        for i in range(0, ROWS):
            print('##############')
            for j in range(0, COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                
                output += token + "|"

            print(output)
        print('##############')



class Agent:

    def __init__(self):
        self.states = []
        self.actions = "UP DOWN LEFT RIGHT".split()
        self.state = State()
        self.learning_rate = 0.2
        self.exp_rate = 0.3

        self.state_values = {}

        for i in range(ROWS):
            for j in range(COLS):
                self.state_values[(i, j)] = 0

    def choose_action(self):
        max_next_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            for a in self.actions:
                next_reward = self.state_values[self.state.next_position(a)]
                if next_reward >= max_next_reward:
                    action = a
                    max_next_reward = next_reward
        
        return action

    def take_action(self, action):
        position = self.state.next_position(action)
        return State(state = position)

    def reset(self):
        self.states = []
        self.state = State()

    def play(self, rounds = 10):
        i = 0

        while i < rounds:
            if self.state.ended:
                reward = self.state.give_reward()
                self.state_values[self.state.state] = reward
                print(f'Game ended. Final reward: {reward}')

                for s in reversed(self.states):
                    reward = self.state_values[s] + self.learning_rate * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                
                self.reset()
                i += 1

            else:
                action = self.choose_action()
                self.states.append(self.state.next_position(action))
                print(f"Round {i}.")
                print(f"Current position is {self.state.state} with action {action}.")
                self.state = self.take_action(action)
                self.state.is_end()
                print(f"Next state {self.state.state}.")
                print("##############")
                i += 1
                

    def show_values(self):
        for i in range(0, ROWS):
            print("##############")
            output = "|"
            for j in range(0, COLS):
                output += str(self.state_values[(i, j)]).ljust(6) + "|"

        print("##############")
        print(output)

if __name__ == "__main__":
    agent = Agent()

    agent.play(50)
    print(agent.show_values())

