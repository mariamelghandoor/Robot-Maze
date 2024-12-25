import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
import random
import matplotlib.pyplot as plt
import numpy as np
import json
from agent import Agent
from maze import Maze
import copy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


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
        self.q_table[s_t[0], s_t[1], a_t] += self.learning_rate * (
            reward + self.discount_factor * np.max(self.q_table[s_next[0], s_next[1]])
            - self.q_table[s_t[0], s_t[1], a_t]
        )

    def get_best_action(self, s_t):
        return np.argmax(self.q_table[s_t[0], s_t[1]])

    def get_action(self, s_t):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice([0, 1, 2, 3])  # Up, Down, Left, Right
        else:
            return self.get_best_action(s_t)


# Load the maze
with open('Mazes json/maze5.json', 'r') as file:
    maze_data = json.load(file)

maze = Maze(maze_data)
shape = (32, 32, 4)  # Adding 4 actions (Up, Down, Left, Right)

# Initialize Q-Learning agent
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.5
q_agent = QLearning(shape, learning_rate, discount_factor, epsilon)

# Initialize the agent
agent = Agent(maze)

# Train the agent
episodes = 1000
for episode in range(episodes):
    s_t = maze.start
    agent.reset_visited()
    total_reward = 0
    done = False

    while not done:
        a_t = q_agent.get_action(s_t)

        # Determine the next state based on the action
        if a_t == 0:  # Up
            s_next = (max(s_t[0] - 1, 0), s_t[1])
        elif a_t == 1:  # Down
            s_next = (min(s_t[0] + 1, shape[0] - 1), s_t[1])
        elif a_t == 2:  # Left
            s_next = (s_t[0], max(s_t[1] - 1, 0))
        elif a_t == 3:  # Right
            s_next = (s_t[0], min(s_t[1] + 1, shape[1] - 1))

        if maze.is_open_Qlearning(s_next[0], s_next[1]):
            reward = maze[s_next]
            # print('maze[s_next]', maze[s_next])
        else:
            reward = -100  # Penalize hitting a wall
            s_next = s_t

        if s_next == maze.goal:
            reward = 1  # Reward for reaching the goal
            done = True
        # print('reward', reward)
        q_agent.update(s_t, a_t, reward, s_next)
        s_t = s_next
        total_reward += reward

    if episode % 100 == 0:
        print(f"Episode {episode} completed with total reward: {total_reward}")

# Test the learned policy
s_t = maze.start
path = [s_t]

while s_t != maze.goal:
    a_t = q_agent.get_best_action(s_t)
    if a_t == 0:  # Up
        s_next = (max(s_t[0] - 1, 0), s_t[1])
    elif a_t == 1:  # Down
        s_next = (min(s_t[0] + 1, shape[0] - 1), s_t[1])
    elif a_t == 2:  # Left
        s_next = (s_t[0], max(s_t[1] - 1, 0))
    elif a_t == 3:  # Right
        s_next = (s_t[0], min(s_t[1] + 1, shape[1] - 1))

    if maze.is_open_Qlearning(s_next[0], s_next[1]):
        path.append(s_next)
        s_t = s_next
    else:
        break

print("Optimal path:", path)
maze.plot_Qlearning(path, "Q-Learning")
