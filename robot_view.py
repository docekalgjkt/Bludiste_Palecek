class RobotView:
    """Class to visually represent the robot."""
    def __init__(self, canvas, robot, cell_size):
        self.canvas = canvas
        self.robot = robot
        self.cell_size = cell_size
        self.robot_id = None

    def draw(self):
        """Draw the robot on the canvas."""
        # Clear the robot's previous position
        if self.robot_id:
            self.canvas.delete(self.robot_id)

        row, col = self.robot.position

        # Draw the robot
        x1, y1 = col * self.cell_size, row * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        color = "red" if not self.robot.backtracking else "blue"  # Red = moving, Blue = backtracking
        self.robot_id = self.canvas.create_oval(x1, y1, x2, y2, fill=color)
