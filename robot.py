class Robot:
    """Class representing a robot that searches for an exit one step at a time."""
    def __init__(self, maze, start):
        self.maze = maze
        self.position = start
        self.path = [start]  # Keeps track of the robot's path
        self.visited = set()  # Keep track of visited cells
        self.stack = [start]  # Stack for DFS search
        self.found_exit = False

    def step(self):
        """Perform one step in the search for the exit."""
        if self.found_exit or not self.stack:
            return

        current = self.stack.pop()

        # If we've already visited this cell, skip it
        if current in self.visited:
            return

        self.visited.add(current)
        self.position = current
        self.path.append(current)

        row, col = current
        if self.maze.is_exit(row, col):
            self.found_exit = True
            return

        # Explore neighbors (Up, Down, Left, Right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.maze.is_free(new_row, new_col) and (new_row, new_col) not in self.visited:
                self.stack.append((new_row, new_col))
