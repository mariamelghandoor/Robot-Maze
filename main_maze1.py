from maze import Maze
from agent import Agent
import json

with open('Mazes json\maze1.json', 'r') as file:
    maze1 = json.load(file)

if __name__ == "__main__":
    maze = Maze(maze1)
    agent = Agent(maze)

    # BFS
    bfs_path = agent.bfs()
    maze.plot(bfs_path, 'BFS')

    agent.reset_visited()
    # DFS
    dfs_path = agent.dfs()
    maze.plot(dfs_path, 'DFS')