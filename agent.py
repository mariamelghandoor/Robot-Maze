# agent.py

class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]

    def reset_visited(self):
        self.visited = [[False for _ in range(self.maze.width)] for _ in range(self.maze.height)]
