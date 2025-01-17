import heapq
from collections import deque
from game_logic import Direction
from utils import manhattan_distance

class AIAgent:
    def __init__(self, game):
        self.game = game
        self.algorithm = self.greedy_best_first_search

    def set_algorithm(self, choice):
        algorithms = {
            1: ("Greedy Best-First Search", self.greedy_best_first_search),
            2: ("Uniform Cost Search", self.uniform_cost_search),
            3: ("Breadth-First Search", self.breadth_first_search),
            4: ("Depth-First Search", self.depth_first_search),
            5: ("Iterative Deepening Search", self.iterative_deepening_search),
            6: ("A* Search", self.a_star_search)
        }
        
        if choice in algorithms:
            self.algorithm = algorithms[choice][1]
            print(f"Using {algorithms[choice][0]}")
        else:
            print("Invalid choice. Using Greedy Best-First Search by default.")
            self.algorithm = self.greedy_best_first_search

    def get_move(self):
        return self.algorithm()

    def greedy_best_first_search(self):
        head = self.game.snake[0]
        food = self.game.food
        best_direction = min(Direction, key=lambda d: manhattan_distance(
            ((head[0] + d.value[0]) % self.game.width, (head[1] + d.value[1]) % self.game.height),
            food
        ))
        return best_direction

    def uniform_cost_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        frontier = [(0, start, [])]
        explored = set()

        while frontier:
            cost, current, path = heapq.heappop(frontier)

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in Direction:
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1]:  # Allow moving to tail position
                    new_cost = cost + 1
                    new_path = path + [direction]
                    heapq.heappush(frontier, (new_cost, next_pos, new_path))

        return self.greedy_best_first_search()

    def breadth_first_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        queue = deque([(start, [])])
        explored = set()

        while queue:
            current, path = queue.popleft()

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in Direction:
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1]:
                    new_path = path + [direction]
                    queue.append((next_pos, new_path))

        return self.greedy_best_first_search()

    def depth_first_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        stack = [(start, [])]
        explored = set()

        while stack:
            current, path = stack.pop()

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in reversed(list(Direction)):  # Reverse direction order to encourage exploration
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1] and next_pos not in [pos for pos, _ in stack]:
                    new_path = path + [direction]
                    stack.append((next_pos, new_path))

        return self.greedy_best_first_search()

    def iterative_deepening_search(self):
        start = self.game.snake[0]
        goal = self.game.food

        def dls(node, depth, path):
            if depth == 0 and node == goal:
                return path
            elif depth > 0:
                for direction in Direction:
                    next_pos = (
                        (node[0] + direction.value[0]) % self.game.width,
                        (node[1] + direction.value[1]) % self.game.height
                    )

                    if next_pos not in self.game.snake[:-1]:
                        result = dls(next_pos, depth - 1, path + [direction])
                        if result:
                            return result
            return None

        for depth in range(self.game.width * self.game.height):
            result = dls(start, depth, [])
            if result:
                return result[0]

        return self.greedy_best_first_search()

    def a_star_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        frontier = [(0, 0, start, [])]
        explored = set()

        def heuristic(pos):
            return manhattan_distance(pos, goal)

        while frontier:
            _, cost, current, path = heapq.heappop(frontier)

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in Direction:
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1]:
                    new_path = path + [direction]
                    new_cost = cost + 1
                    priority = new_cost + heuristic(next_pos)
                    heapq.heappush(frontier, (priority, new_cost, next_pos, new_path))

        return self.greedy_best_first_search()

import heapq
from collections import deque
from game_logic import Direction
from utils import manhattan_distance

class AIAgent:
    def __init__(self, game):
        self.game = game
        self.algorithm = self.greedy_best_first_search

    def set_algorithm(self, choice):
        algorithms = {
            1: ("Greedy Best-First Search", self.greedy_best_first_search),
            2: ("Uniform Cost Search", self.uniform_cost_search),
            3: ("Breadth-First Search", self.breadth_first_search),
            4: ("Depth-First Search", self.depth_first_search),
            5: ("Iterative Deepening Search", self.iterative_deepening_search),
            6: ("A* Search", self.a_star_search)
        }
        
        if choice in algorithms:
            self.algorithm = algorithms[choice][1]
            print(f"Using {algorithms[choice][0]}")
        else:
            print("Invalid choice. Using Greedy Best-First Search by default.")
            self.algorithm = self.greedy_best_first_search

    def get_move(self):
        return self.algorithm()

    def greedy_best_first_search(self):
        head = self.game.snake[0]
        food = self.game.food
        best_direction = min(Direction, key=lambda d: manhattan_distance(
            ((head[0] + d.value[0]) % self.game.width, (head[1] + d.value[1]) % self.game.height),
            food
        ))
        return best_direction

    def uniform_cost_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        frontier = [(0, start, [])]
        explored = set()

        while frontier:
            cost, current, path = heapq.heappop(frontier)

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in Direction:
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1]:  # Allow moving to tail position
                    new_cost = cost + 1
                    new_path = path + [direction]
                    heapq.heappush(frontier, (new_cost, next_pos, new_path))

        return self.greedy_best_first_search()

    def breadth_first_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        queue = deque([(start, [])])
        explored = set()

        while queue:
            current, path = queue.popleft()

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in Direction:
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1]:
                    new_path = path + [direction]
                    queue.append((next_pos, new_path))

        return self.greedy_best_first_search()

    def depth_first_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        stack = [(start, [])]
        explored = set()

        while stack:
            current, path = stack.pop()

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in reversed(list(Direction)):  # Reverse direction order to encourage exploration
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1] and next_pos not in [pos for pos, _ in stack]:
                    new_path = path + [direction]
                    stack.append((next_pos, new_path))

        return self.greedy_best_first_search()

    def iterative_deepening_search(self):
        start = self.game.snake[0]
        goal = self.game.food

        def dls(node, depth, path):
            if depth == 0 and node == goal:
                return path
            elif depth > 0:
                for direction in Direction:
                    next_pos = (
                        (node[0] + direction.value[0]) % self.game.width,
                        (node[1] + direction.value[1]) % self.game.height
                    )

                    if next_pos not in self.game.snake[:-1]:
                        result = dls(next_pos, depth - 1, path + [direction])
                        if result:
                            return result
            return None

        for depth in range(self.game.width * self.game.height):
            result = dls(start, depth, [])
            if result:
                return result[0]

        return self.greedy_best_first_search()

    def a_star_search(self):
        start = self.game.snake[0]
        goal = self.game.food
        frontier = [(0, 0, start, [])]
        explored = set()

        def heuristic(pos):
            return manhattan_distance(pos, goal)

        while frontier:
            _, cost, current, path = heapq.heappop(frontier)

            if current == goal:
                return path[0] if path else self.greedy_best_first_search()

            if current in explored:
                continue

            explored.add(current)

            for direction in Direction:
                next_pos = (
                    (current[0] + direction.value[0]) % self.game.width,
                    (current[1] + direction.value[1]) % self.game.height
                )

                if next_pos not in self.game.snake[:-1]:
                    new_path = path + [direction]
                    new_cost = cost + 1
                    priority = new_cost + heuristic(next_pos)
                    heapq.heappush(frontier, (priority, new_cost, next_pos, new_path))

        return self.greedy_best_first_search()

