from robot_builder import RobotBuilder

class RobotEngineer:
    def __init__(self, builder: RobotBuilder):
        self.builder = builder

    def construct_robot(self):
        self.builder.build_head()
        self.builder.build_body()
        self.builder.build_arms()
        self.builder.build_legs()
        return self.builder.get_robot()
