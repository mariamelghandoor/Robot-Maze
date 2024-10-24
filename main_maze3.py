from maze import Maze
from agent import Agent

maze3 = [
    
]

if __name__ == "__main__":
    maze = Maze(maze3)
    agent = Agent(maze)

    # BFS
    bfs_path = agent.bfs()
    maze.plot(bfs_path, 'BFS')

    agent.reset_visited()
    # DFS
    dfs_path = agent.dfs()
    maze.plot(dfs_path, 'DFS')
