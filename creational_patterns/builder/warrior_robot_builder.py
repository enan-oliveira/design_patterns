from robot_builder import RobotBuilder

class WarriorRobotBuilder(RobotBuilder):
    def build_head(self):
        self.robot.add_part("Head", "Helmet with infrared vision")

    def build_body(self):
        self.robot.add_part("Body", "Armored torso")

    def build_arms(self):
        self.robot.add_part("Arms", "Laser cannons")

    def build_legs(self):
        self.robot.add_part("Legs", "Tank treads")
