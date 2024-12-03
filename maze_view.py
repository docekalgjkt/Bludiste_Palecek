class MazeView:
    """Class for visualizing the maze."""
    def __init__(self, canvas, maze, cell_size):
        self.canvas = canvas
        self.maze = maze
        self.cell_size = cell_size

    def draw(self):
        """Draw the maze on the canvas."""
        for i, row in enumerate(self.maze.maze):
            for j, cell in enumerate(row):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "grey" if cell == 1 else "lightblue"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
