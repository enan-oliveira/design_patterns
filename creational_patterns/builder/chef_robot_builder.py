from robot_builder import RobotBuilder

class ChefRobotBuilder(RobotBuilder):
    def build_head(self):
        self.robot.add_part("Head", "Chef hat with recipe database")

    def build_body(self):
        self.robot.add_part("Body", "Kitchen-grade stainless steel")

    def build_arms(self):
        self.robot.add_part("Arms", "Multi-functional cooking tools")

    def build_legs(self):
        self.robot.add_part("Legs", "Wheeled base with spice rack")
