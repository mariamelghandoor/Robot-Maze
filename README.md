# Maze-Solving Platform

Welcome to the Maze-Solving Platform! This project is designed to help you explore and understand various search algorithms used in artificial intelligence and robotics. The platform allows a robot to navigate through a maze to reach a goal using different algorithms, including BFS, DFS, A*, Dijkstra's, and more. Each algorithm's pathfinding process is visualized in real-time, making it an excellent tool for learning and testing AI techniques.

## Features

- **Multiple Search Algorithms**: The platform supports a wide range of search algorithms, including:
  - **Uninformed Search Algorithms**:
    - Breadth-First Search (BFS)
    - Depth-First Search (DFS)
    - Iterative Deepening Search (IDS)
    - Uniform Cost Search (UCS)
  - **Heuristic Search Algorithms**:
    - Greedy Best-First Search (using Manhattan and Euclidean distances)
    - A* Search (using Manhattan and Euclidean distances)
  - **Local Search Algorithms**:
    - Hill Climbing
    - Stochastic Hill Climbing
    - First-Choice Hill Climbing
    - Steepest Ascent Hill Climbing
    - Simulated Annealing
    - Genetic Algorithm
  - **Reinforcement Learning**:
    - Q-Learning

- **Real-Time Visualization**: Watch as the robot navigates the maze, avoiding obstacles and finding the optimal path to the goal. The visualization helps you understand how each algorithm works in practice.

- **Customizable Mazes**: The platform allows you to load different mazes from JSON files, making it easy to test and compare algorithms on various maze configurations.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (install via `pip`):
  - `matplotlib` (for visualization)
  - `numpy` (for numerical operations)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mariamelghandoor/Robot-Maze.git

2. **Run the Platform**:
   
   - Choose which maze you want to run, this is an example for maze 1
   ```bash
    python mazes/main_maze1.py

## Usage

1. **Load a Maze**:
   - The platform loads a maze from a JSON file (`Mazes json/maze1.json` by default). You can modify this file or create new ones to test different maze configurations.

2. **Run Algorithms**:
   - The `main.py` script contains code to run various algorithms. By default, some algorithms are commented out. Uncomment the ones you want to test and run the script.

3. **Visualize the Results**:
   - The platform will display the path taken by the robot for each algorithm, along with the algorithm's name. This helps you compare the efficiency and effectiveness of different search strategies.

### Example

Here's an example of how to run the Greedy Best-First Search algorithm using the Manhattan distance heuristic:

```python
# Greedy Best-First Search 
    greedy_agent = GreedyAgent2(maze)
    path_greedy = greedy_agent.greedy()
    maze.plot(path_greedy, 'greedy')
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- This project was inspired by various AI and robotics courses and textbooks.
- Special thanks to the contributors of the `matplotlib` and `numpy` libraries for making visualization and numerical operations easy. 

---

Happy maze-solving! 🚀
