import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import random
import tracemalloc
from queue import PriorityQueue
from agent import Agent

class GeneticAgent(Agent):
    def __init__(self, maze, population_size=30, generations=1000, mutation_rate=0.1, max_path_length=1000):
        super().__init__(maze)
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.max_path_length = max_path_length  # Limit path length to avoid excessive coloring

    def heuristic(self, x, y):
        goal_x, goal_y = self.maze.goal
        return abs(x - goal_x) + abs(y - goal_y)

    def generate_initial_population(self):
        population = []
        for _ in range(self.population_size):
            path = [self.maze.start]
            while path[-1] != self.maze.goal and len(path) < self.max_path_length:
                x, y = path[-1]
                moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                valid_moves = [move for move in moves if self.maze.is_open(*move)]
                if valid_moves:
                    path.append(random.choice(valid_moves))
                else:
                    break
            population.append(path)
        return population

    def fitness(self, path):
        x, y = path[-1]
        goal_x, goal_y = self.maze.goal
        path_length_penalty = len(path) - 1
        return -(self.heuristic(x, y) + path_length_penalty) 

    def crossover(self, parent1, parent2):
        cut = random.randint(1, min(len(parent1), len(parent2)) - 1)
        child1 = parent1[:cut] + parent2[cut:]
        child2 = parent2[:cut] + parent1[cut:]
        return child1, child2

    def mutate(self, path):
        if random.random() < self.mutation_rate:
            x, y = path[-1]
            moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            valid_moves = [move for move in moves if self.maze.is_open(*move)]
            if valid_moves:
                path.append(random.choice(valid_moves))

       
        return path[:self.max_path_length]  

    def genetic(self):
        tracemalloc.start()
        start_time = time.time()
        
        population = self.generate_initial_population()
        
        for generation in range(self.generations):
            population = sorted(population, key=self.fitness, reverse=True)
            
            if self.fitness(population[0]) >= 0:
                end_time = time.time()
                execution_time = end_time - start_time
                current, peak = tracemalloc.get_traced_memory()
                print(f"Genetic search execution time: {execution_time:.6f} seconds")
                print(f"Peak Memory Usage in Genetic: {peak / 1024/ 1024:.2f} MB")
                return population[0]  
            
            new_population = population[:self.population_size // 2]  
            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(population[:self.population_size // 2], 2)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))
            
            population = new_population
        
        end_time = time.time()
        execution_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"Genetic search execution time: {execution_time:.6f} seconds")
        print(f"Peak Memory Usage in Genetic: {peak / 1024/ 1024:.2f} MB")
        print("No path found from start to goal.")
        return population[0]
