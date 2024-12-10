import tkinter as tk
from maze import Maze
from robot import Robot
from robot_view import RobotView
from maze_view import MazeView

class MazeApp:
    """Main application to run the maze with the robot."""
    def __init__(self, root, maze_file, start_position):
        self.root = root
        self.cell_size = 30

        # Initialize the maze
        self.maze = Maze(maze_file)
        self.canvas = tk.Canvas(root, width=len(self.maze.maze[0]) * self.cell_size,
                                height=len(self.maze.maze) * self.cell_size)
        self.canvas.pack()

        # Initialize views
        self.maze_view = MazeView(self.canvas, self.maze, self.cell_size)
        self.maze_view.draw()

        # Initialize robot
        self.robot = Robot(self.maze, start_position)
        self.robot_view = RobotView(self.canvas, self.robot, self.cell_size)

        # Start the robot's search
        self.root.after(500, self.run_robot)

    def run_robot(self):
        """Animate the robot's movement."""
        if not self.robot.found_exit:
            self.robot.step()
        self.robot_view.draw()
        if not self.robot.found_exit:
            self.root.after(200, self.run_robot)  # Delay for each step
        else:
            print("Robot has found the exit!")
            print("Path:", self.robot.path)

if __name__ == "__main__":
    maze_file = "mapa.csv"  # Path to the maze file
    start_position = (1, 1)  # Robot's starting position

    root = tk.Tk()
    root.title("Autonomous Robot Maze Solver")
    app = MazeApp(root, maze_file, start_position)
    root.mainloop()
