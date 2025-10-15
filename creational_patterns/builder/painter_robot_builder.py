from robot_builder import RobotBuilder

class PainterRobotBuilder(RobotBuilder):
    def build_head(self):
        self.robot.add_part("Head", "Artistic visor with color sensors")

    def build_body(self):
        self.robot.add_part("Body", "Paint storage and mixing system")

    def build_arms(self):
        self.robot.add_part("Arms", "Precision paintbrush and spray nozzles")

    def build_legs(self):
        self.robot.add_part("Legs", "Spider legs for canvas navigation")
