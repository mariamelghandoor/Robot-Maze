import time
import heapq
from queue import Queue
from agent import Agent

class UCSAgent(Agent):
    def construct_path(self, visited, start, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = visited[current][1]  # Get the parent node
        path.reverse()
        return path
    

    def ucs(self):
        start_time = time.time()
        
        pqueue = [(0, self.maze.start)]  # Priority queue with (cost, node)
        costs = {self.maze.start: 0}  # Track minimum cost to reach each node
        self.reset_visited()
        self.visited = {self.maze.start: (0, None)}  # Track parent and cost for path reconstruction

        while pqueue:
            current_cost, current_node = heapq.heappop(pqueue)
            x, y = current_node
            node_cost = self.maze[current_node]

            
            # Check if we've reached the goal
            if (x, y) == self.maze.goal:
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"UCS execution time: {execution_time:.6f} seconds")
                
                path = self.construct_path(self.visited, self.maze.start, self.maze.goal)
                total_path_cost = sum(self.maze[node] for node in path)
                print(f"Total path cost: {total_path_cost}")
                
                return path # total_path_cost, path
            
            # Explore neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)
                
                # Ensure within maze bounds
                if 0 <= nx < self.maze.height and 0 <= ny < self.maze.width:
                    neighbor_cost = self.maze[neighbor]
                    new_cost = current_cost + neighbor_cost
                    
                    # Check if new path to neighbor is cheaper
                    if self.maze.is_open(nx, ny) and (neighbor not in costs or new_cost < costs[neighbor]):
                        costs[neighbor] = new_cost
                        heapq.heappush(pqueue, (new_cost, neighbor))
                        self.visited[neighbor] = (new_cost, current_node)  # Store cost and parent for path reconstruction

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"UCS execution time: {execution_time:.6f} seconds")

        print("No path found from start to goal.")
        return None