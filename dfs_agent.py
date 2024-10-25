import time
from agent import Agent

class DFSAgent(Agent):
    def dfs(self):
        start_time = time.time()
        
        stack = [[self.maze.start]]
        self.reset_visited()
        self.visited[self.maze.start[0]][self.maze.start[1]] = True

        while stack:
            path = stack.pop()
            x, y = path[-1]
            
            # Check goal
            if (x, y) == self.maze.goal:

                end_time = time.time() 
                execution_time = end_time - start_time 
                print(f"DFS execution time: {execution_time:.6f} seconds")

                return path
            
            # Explore neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:  # Check valid and not visited
                    self.visited[nx][ny] = True
                    new_path = list(path) 
                    new_path.append((nx, ny))
                    stack.append(new_path)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"DFS execution time: {execution_time:.6f} seconds")
        
        print("No path found from start to goal.")
        return None
