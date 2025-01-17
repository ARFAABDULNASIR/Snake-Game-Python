Snake Game with AI Searches

Overview

This project is a Python implementation of the classic Snake game, enhanced with AI-driven search algorithms to control the snake's movements. The goal of the project is to demonstrate the application of various search strategies in navigating the snake to the food while avoiding obstacles (such as its own body and the game boundaries).

Features

Classic Snake Game: The traditional gameplay mechanics of Snake, including movement, growth, and collision detection.

AI Integration: Multiple search algorithms implemented to determine the optimal path for the snake to reach the food.

Customizable Gameplay: Options to adjust grid size, speed, and search algorithm.

Visual Representation: Real-time visualization of the snake's movement and the selected algorithm's decision-making process.

Search Algorithms Implemented

Uniform Cost Search (UCS): Explores paths based on their cost, ensuring the least costly path is selected.

Breadth-First Search (BFS): Explores all possible moves level by level, guaranteeing the shortest path in an unweighted grid.

Depth-First Search (DFS): Explores paths deeply before backtracking, but may not guarantee the shortest path.

A Search:* Uses a heuristic to prioritize paths, balancing cost and estimated distance to the goal.

Iterative Deepening Search (IDS): Combines the benefits of depth-first and breadth-first searches by incrementally increasing the search depth.

Requirements

Python: Version 3.8 or higher

Libraries:

pygame for game visualization

heapq for priority queue management (used in UCS and A*)
