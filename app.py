import tkinter as tk
from tkinter import filedialog, messagebox
from maze import Maze
from maze_readers import CSVReader, XMLReader, TXTReader
from robot import Robot
from robot_view import RobotView
from maze_view import MazeView

class MazeApp:
    """Main application for the maze solver."""
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")
        self.cell_size = 30

        self.maze = None
        self.start_position = None
        self.robot = None
        self.robot_view = None
        self.maze_view = None

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """Create UI widgets."""
        self.load_button = tk.Button(self.root, text="Load Maze", command=self.load_maze)
        self.load_button.pack()

        self.start_button = tk.Button(self.root, text="Start Robot", command=self.start_robot, state=tk.DISABLED)
        self.start_button.pack()

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

    def load_maze(self):
        """Load a maze file."""
        file_path = filedialog.askopenfilename(title="Select a Maze File",
                                               filetypes=[("CSV Files", "*.csv"),
                                                          ("XML Files", "*.xml"),
                                                          ("TXT Files", "*.txt")])
        if not file_path:
            return

        try:
            # Determine file type and read maze
            if file_path.endswith('.csv'):
                maze_data = CSVReader.read(file_path)
            elif file_path.endswith('.xml'):
                maze_data = XMLReader.read(file_path)
            elif file_path.endswith('.txt'):
                maze_data = TXTReader.read(file_path)
            else:
                raise ValueError("Unsupported file format")

            self.maze = Maze(maze_data)
            self.start_position = None  # Reset start position
            self.start_button.config(state=tk.DISABLED)

            # Draw the maze
            self.canvas.delete("all")
            self.canvas.config(width=len(self.maze.maze[0]) * self.cell_size,
                               height=len(self.maze.maze) * self.cell_size)
            self.maze_view = MazeView(self.canvas, self.maze, self.cell_size)
            self.maze_view.draw()

            # Bind click event for selecting robot start position
            self.canvas.bind("<Button-1>", self.set_robot_start)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load maze: {e}")

    def set_robot_start(self, event):
        """Set the robot's starting position."""
        if not self.maze:
            return

        row, col = event.y // self.cell_size, event.x // self.cell_size

        if self.maze.is_free(row, col):
            self.start_position = (row, col)
            self.robot = Robot(self.maze, self.start_position)

            # Draw the robot's starting position
            self.robot_view = RobotView(self.canvas, self.robot, self.cell_size)
            self.robot_view.draw()

            # Enable the start button
            self.start_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Invalid Start Position", "Please click on a free cell to place the robot.")

    def start_robot(self):
        """Start the robot's search."""
        if not self.robot or not self.start_position:
            messagebox.showerror("Error", "Please set a start position for the robot.")
            return

        self.run_robot()

    def run_robot(self):
        """Animate the robot's movement."""
        if not self.robot.found_exit:
            self.robot.step()
        self.robot_view.draw()
        if not self.robot.found_exit:
            self.root.after(200, self.run_robot)
        else:
            messagebox.showinfo("Success", "The robot found the exit!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
