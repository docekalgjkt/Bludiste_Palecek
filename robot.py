class Robot:
    """Class representing a robot that searches for an exit."""
    def __init__(self, maze, start):
        self.maze = maze
        self.position = start  # Current position
        self.visited = set()  # Cells the robot has already visited
        self.stack = [start]  # Stack for DFS search
        self.path = [start]  # Path taken by the robot
        self.found_exit = False
        self.backtracking = False  # Indicates whether the robot is backtracking

    def step(self):
        """Perform one step in the search for the exit."""
        if self.found_exit or not self.stack:
            return

        if not self.backtracking:
            # Move to the next cell
            current = self.stack.pop()

            if current in self.visited:
                self.backtracking = True  # Start backtracking
                return

            # Mark as visited and move to the cell
            self.visited.add(current)
            self.position = current
            self.path.append(current)

            row, col = current

            # Check if it's the exit
            if self.maze.is_exit(row, col):
                self.found_exit = True
                return

            # Add valid neighbors to the stack
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dr, col + dc
                if self.is_valid_move(new_row, new_col):
                    self.stack.append((new_row, new_col))

            # If no neighbors, start backtracking
            if not self.stack:
                self.backtracking = True

        else:
            # Backtracking: Remove the last step from the path
            if len(self.path) > 1:
                self.path.pop()
                self.position = self.path[-1]
            else:
                self.backtracking = False

    def is_valid_move(self, row, col):
        """Check if the robot can move to the given cell."""
        return (
            0 <= row < len(self.maze.maze) and
            0 <= col < len(self.maze.maze[0]) and
            (row, col) not in self.visited and
            self.maze.is_free(row, col)
        )
