from queue import Queue
from maze import Maze

class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]

    def reset_visited(self):
        self.visited = [[False for _ in range(self.maze.width)] for _ in range(self.maze.height)]

    def bfs(self):
        queue = Queue()
        queue.put([self.maze.start])
        while not queue.empty():
            path = queue.get()
            x, y = path[-1]
            if (x, y) == self.maze.goal:
                return path
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                    self.visited[nx][ny] = True
                    new_path = list(path) + [(nx, ny)]
                    queue.put(new_path)
        return None

    def dfs(self, x=None, y=None, path=None):
        if x is None and y is None:
            x, y = self.maze.start
            path = [(x, y)]
            self.visited[x][y] = True
        if (x, y) == self.maze.goal:
            return path
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                self.visited[nx][ny] = True
                result = self.dfs(nx, ny, path + [(nx, ny)])
                if result:
                    return result
        return None
