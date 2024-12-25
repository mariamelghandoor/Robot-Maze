import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
from agent import Agent
import random
import matplotlib.pyplot as plt
import numpy as np
import json

class QLearning:
    def __init__(self, shape, learning_rate, discount_factor, epsilon):
        assert 0 < learning_rate < 1, "Learning rate must be between 0 and 1."
        assert 0 < discount_factor < 1, "Discount factor must be between 0 and 1."
        assert 0 <= epsilon <= 1, "Epsilon must be between 0 and 1."

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = np.zeros(shape=shape)

    def update(self, s_t, a_t, reward, s_next):
        # Fix indexing here, using s_t[0] and s_t[1] to access the correct indices in q_table
        self.q_table[s_t[0], s_t[1], a_t] += self.learning_rate * self._get_temporal_difference(s_t, a_t, reward, s_next)

    def _get_temporal_difference(self, s_t, a_t, reward, s_next):
        return self._get_temporal_difference_target(reward, s_next) - self.q_table[s_t[0], s_t[1], a_t]

    def _get_temporal_difference_target(self, reward, s_next):
        return reward + self.discount_factor * np.max(self.q_table[s_next[0], s_next[1]])

    def get_best_action(self, s_t):
        # Fix: use s_t[0] and s_t[1] for correct indexing
        return np.argmax(self.q_table[s_t[0], s_t[1]])

    def get_action(self, s_t):
        # Epsilon-greedy policy: explore with probability epsilon, exploit with probability 1 - epsilon
        if random.uniform(0, 1) < self.epsilon:
            return random.choice([0, 1, 2, 3])  # Up, Down, Left, Right (0, 1, 2, 3)
        else:
            return self.get_best_action(s_t)



def replace_none(data):
    # Recursive function to replace "None" with Python's None
    if isinstance(data, dict):
        return {k: replace_none(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_none(item) for item in data]
    elif data == "None":
        return None
    else:
        return data

with open('Mazes json/maze5.json', 'r') as file:
    maze = json.load(file)

shape = (32, 32, 4)
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.5  # 20% chance to explore randomly
agent = QLearning(shape, learning_rate, discount_factor, epsilon)

# Replace "None" strings with None
maze = replace_none(maze)

# Simulate agent learning through the maze
episodes = 1000
for episode in range(episodes):
    s_t = (0, 0)
    done = False
    total_reward = 0

    while not done:
        a_t = agent.get_action(s_t)
        # Determine the next state (action to move)
        if a_t == 0:  # Up
            s_next = (max(s_t[0] - 1, 0), s_t[1])
        elif a_t == 1:  # Down
            s_next = (min(s_t[0] + 1, shape[0] - 1), s_t[1])
        elif a_t == 2:  # Left
            s_next = (s_t[0], max(s_t[1] - 1, 0))
        elif a_t == 3:  # Right
            s_next = (s_t[0], min(s_t[1] + 1, shape[1] - 1))

        # Check if the next state is a valid state (not an obstacle or None)
        if maze[s_next[0]][s_next[1]] is None:
            reward = -100  # Penalize for hitting an obstacle
            s_next = s_t  # Stay in the same state (retry)
        else:
            reward = maze[s_next[0]][s_next[1]] if maze[s_next[0]][s_next[1]] is not None else -0.04


        # If the agent reaches the goal or a penalty, end the episode
        if reward == +1 or reward == -1:
            done = True

        # Update Q-table
        agent.update(s_t, a_t, reward, s_next)

        # Move to the next state
        s_t = s_next
        total_reward += reward

    if episode % 100 == 0:
        print(f"Episode {episode} completed.")
    

# Test the learned policy after training
s_t = (0, 0)  # Start position
steps = []
while maze[s_t[0]][s_t[1]] != 1:  # Until goal is reached
    a_t = agent.get_best_action(s_t)
    # Determine the next state (action to move)
    if a_t == 0:  # Up
        s_next = (max(s_t[0] - 1, 0), s_t[1])
    elif a_t == 1:  # Down
        s_next = (min(s_t[0] + 1, shape[0] - 1), s_t[1])
    elif a_t == 2:  # Left
        s_next = (s_t[0], max(s_t[1] - 1, 0))
    elif a_t == 3:  # Right
        s_next = (s_t[0], min(s_t[1] + 1, shape[1] - 1))

    # Ensure we don't try to move into an invalid state (None)
    if maze[s_next[0]][s_next[1]] is None:
        pass  # Stop if trying to move into an obstacle
    steps.append(s_next)
    s_t = s_next

print("Optimal path:", steps)