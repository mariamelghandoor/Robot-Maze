from maze import Maze
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
import json

with open('Mazes json\maze3.json', 'r') as file:
    maze3 = json.load(file)

if __name__ == "__main__":
    maze = Maze(maze3)

    # BFS
    bfs_agent = BFSAgent(maze)
    path_bfs = bfs_agent.bfs()
    maze.plot(path_bfs, 'BFS')

    # DFS
    dfs_agent = DFSAgent(maze)
    path_dfs = dfs_agent.dfs()
    maze.plot(path_dfs, 'BFS')

