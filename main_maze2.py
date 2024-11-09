from maze import Maze
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
from ids import IDSAgent
from UCS import UCSAgent
import json

with open('Mazes json\maze2.json', 'r') as file:
    maze2 = json.load(file)

if __name__ == "__main__":
    maze = Maze(maze2)

    # BFS
    bfs_agent = BFSAgent(maze)
    path_bfs = bfs_agent.bfs()
    maze.print_maze(path_bfs)
    maze.plot(path_bfs, 'BFS')

    # DFS
    dfs_agent = DFSAgent(maze)
    path_dfs = dfs_agent.dfs()
    maze.plot(path_dfs, 'DFS')

    # IDS
    ids_agent = IDSAgent(maze)
    path_ids = ids_agent.ids()
    maze.plot(path_ids, 'IDS')

    #UCS
    ucs_agent = UCSAgent(maze)
    path_ucs = ucs_agent.ucs()
    maze.plot(path_ucs, 'UCS')