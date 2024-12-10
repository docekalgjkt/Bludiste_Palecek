import csv

class Maze:
    """Class representing the maze."""
    def __init__(self, maze_file):
        self.maze = self.load_maze(maze_file)

    def load_maze(self, maze_file):
        """Load the maze from a CSV file."""
        maze = []
        with open(maze_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                maze.append(list(map(int, row)))
        return maze

    def is_free(self, row, col):
        """Check if a cell is free (0)."""
        if 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]):
            return self.maze[row][col] == 0
        return False

    def is_exit(self, row, col):
        """Check if a cell is an exit (on the edge and free)."""
        rows, cols = len(self.maze), len(self.maze[0])
        return self.is_free(row, col) and (row == 0 or col == 0 or row == rows - 1 or col == cols - 1)
