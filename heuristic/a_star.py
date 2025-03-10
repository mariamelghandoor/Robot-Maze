import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import tracemalloc
from queue import PriorityQueue
from agent import Agent

class A_StarAgent(Agent):
    def heuristic(self, x, y):
        goal_x, goal_y = self.maze.goal
        return abs(x - goal_x) + abs(y - goal_y)

    def a_star(self):
        tracemalloc.start()
        start_time = time.time()
        pq = PriorityQueue()
        start = self.maze.start
        g_cost = {start: 0}
        pq.put((self.heuristic(start[0], start[1]), [start]))
        self.reset_visited()
        self.visited[start[0]][start[1]] = True

        while not pq.empty():
            _, path = pq.get()
            x, y = path[-1]

            if (x, y) == self.maze.goal:
                end_time = time.time()
                execution_time = end_time - start_time
                current, peak = tracemalloc.get_traced_memory()
                print(f"A* search execution time: {execution_time:.6f} seconds")
                print(f"Peak Memory Usage in A*: {peak / 1024/ 1024:.2f} MB")
                return path

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if self.maze.is_open(nx, ny) and not self.visited[nx][ny]:
                    new_g_cost = g_cost[(x, y)] + self.maze[x,y]  # cost of 1 per step
                    if (nx, ny) not in g_cost or new_g_cost < g_cost[(nx, ny)]:
                        g_cost[(nx, ny)] = new_g_cost
                        f_cost = new_g_cost + self.heuristic(nx, ny)
                        new_path = list(path) + [(nx, ny)]
                        pq.put((f_cost, new_path))
                        self.visited[nx][ny] = True

        end_time = time.time()
        execution_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"A* search execution time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage in A*: {peak/ 1024/ 1024:.2f} MB")
        print("No path found from start to goal.")
        return None
