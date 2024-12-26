import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
import json
from maze import Maze
from QLearning.TrainTest import train_qlearning, test_qlearning
from QLearning.Q_Learning import QLearning
from agent import Agent


with open('Mazes json\maze5.json', 'r') as file:
    maze = json.load(file)

if __name__ == "__main__":
    # Q-Learning
    # tracemalloc.start()
    start_time = time.time()
    maze = Maze(maze)
    shape = (32, 32, 4)  # Adding 4 actions (Up, Down, Left, Right)

    learning_rate = 0.1
    discount_factor = 0.9
    epsilon = 0.5
    q_agent = QLearning(shape, learning_rate, discount_factor, epsilon)

    agent = Agent(maze)
    episodes = 10000
    train_qlearning(q_agent, maze, agent, episodes, shape)
    test_qlearning(q_agent, maze, shape)
    end_time = time.time()
    execution_time = end_time - start_time
    # current, peak = tracemalloc.get_traced_memory()
    print(f"Q-Learning execution time: {execution_time:.6f} seconds")
    # print(f"Peak Memory Usage in Q-Learning: {peak / 1024 / 1024:.2f} MB")