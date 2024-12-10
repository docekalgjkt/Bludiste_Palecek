class RobotView:
    """Class for visualizing the robot."""
    def __init__(self, canvas, robot, cell_size):
        self.canvas = canvas
        self.robot = robot
        self.cell_size = cell_size
        self.robot_sprite = None

    def draw(self):
        """Draw the robot on its current position."""
        if self.robot_sprite:
            self.canvas.delete(self.robot_sprite)
        x1 = self.robot.position[1] * self.cell_size
        y1 = self.robot.position[0] * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.robot_sprite = self.canvas.create_oval(x1, y1, x2, y2, fill="yellow", outline="black")
