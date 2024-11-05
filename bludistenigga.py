import tkinter as tk
from typing import List, Tuple

class Maze:
    def __init__(self, layout: List[List[int]]):
        self.layout = layout

    def is_free(self, coordinates: Tuple[int, int]) -> bool:
        """Kontroluje, zda jsou souřadnice volné (0)."""
        x, y = coordinates
        return self.layout[y][x] == 0

    def get_width(self) -> int:
        """Vrací šířku bludiště."""
        return len(self.layout[0])

    def get_height(self) -> int:
        """Vrací výšku bludiště."""
        return len(self.layout)

    def get_dimensions(self) -> Tuple[int, int]:
        """Vrací rozměry bludiště (šířka, výška)."""
        return self.get_width(), self.get_height()

    def is_exit(self, coordinates: Tuple[int, int]) -> bool:
        """Zjišťuje, zda jsou souřadnice východ z bludiště."""
        x, y = coordinates
        return y == len(self.layout) - 1 and x == len(self.layout[0]) - 3

class MazeView:
    def __init__(self, maze: Maze, cell_size: int = 40, padding: int = 10):
        self.maze = maze
        self.cell_size = cell_size
        self.padding = padding

    def draw(self, canvas: tk.Canvas):
        """Kreslí bludiště na canvas."""
        for i in range(self.maze.get_height()):
            for j in range(self.maze.get_width()):
                x1 = self.padding + j * self.cell_size
                y1 = self.padding + i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                if self.maze.layout[i][j] == 1:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

class MazeApp:
    def __init__(self, root: tk.Tk, maze_layout: List[List[int]]):
        self.canvas = tk.Canvas(root, width=len(maze_layout[0]) * 40 + 20,
                                height=len(maze_layout) * 40 + 20)
        self.canvas.pack()
        self.maze = Maze(maze_layout)
        self.view = MazeView(self.maze)

    def run(self):
        """Spuštění aplikace a vykreslení bludiště."""
        self.view.draw(self.canvas)

# Data bludiště - 1 je stěna, 0 je cesta
maze_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Nastavení Tkinter okna
root = tk.Tk()
root.title("Maze Game")

# Inicializace aplikace
app = MazeApp(root, maze_data)

# Spuštění aplikace
app.run()

# Hlavní smyčka Tkinteru
root.mainloop()
