import numpy as np
import random
import math

W = [20, 40, 60, 12, 34, 45, 67, 33, 23, 12, 34, 56, 23, 56] # ! Weights
G = [120, 420, 610, 112, 341, 435, 657, 363, 273, 812, 534, 356, 223, 516] # ! Gold

w_max = 150 # ! Bilbo's maximum weight capacity

def score_state_log(x, g, beta):
    return beta * np.dot(x, g)

def propose_state(x, w, w_max):
    M = len(w)

    random_ix = random.randint(0, M - 1)
    proposal = list(x)
    proposal[random_ix] = 1 - proposal[random_ix] # ! Toggle whether the object is in Bilbo's bag.
    
    if np.dot(proposal, w) <= w_max:
        return proposal
    else:
        return propose_state(x, w, w_max)


def MCMC_Knapsack(epochs, w, g, w_max, beta0 = 0.05, beta_increase = 0.02):
    M = len(w)
    beta = beta0
    current_x = [0] * M # ! Starts with no items in bag.
    state_keeper = []
    best_state = current_x
    max_score = 0

    for i in range(epochs):
        state_keeper.append(current_x)
        proposed_x = propose_state(current_x, w, w_max)

        current_score = score_state_log(current_x, g, beta)
        proposed_score = score_state_log(proposed_x, g, beta)
        accept_prob = min(1, math.exp(proposed_score - current_score))

        if current_score > max_score:
            best_state = current_x
        if accept_prob > 0.5: # ? Random coin function ???
            current_x = proposed_x
            max_score = proposed_score
        if i % 500 == 0:
            beta += beta_increase

        return state_keeper, best_state

def main():
    max_state_value = 0
    solution = [0]

    for i in range(10):
        state_keeper, best_state = MCMC_Knapsack(50000, W, G, w_max, 0.0005, 0.0005)
        state_value = np.dot(best_state, G)

        if state_value > max_state_value:
            max_state_value = state_value
            solution = best_state

    print(f"MCMC solution found. {solution} with gold value {max_state_value}")

if __name__ == "__main__":
    main()

