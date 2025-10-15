from warrior_robot_builder import WarriorRobotBuilder
from robot_engineer import RobotEngineer
from chef_robot_builder import ChefRobotBuilder
from painter_robot_builder import PainterRobotBuilder

# Build a Warrior Robot
warrior_builder = WarriorRobotBuilder()
engineer = RobotEngineer(warrior_builder)
warrior_robot = engineer.construct_robot()
warrior_robot.describe()

# Build a Chef Robot
chef_builder = ChefRobotBuilder()
engineer = RobotEngineer(chef_builder)
chef_robot = engineer.construct_robot()
chef_robot.describe()

# Build a Painter Robot
painter_builder = PainterRobotBuilder()
engineer = RobotEngineer(painter_builder)
painter_robot = engineer.construct_robot()
painter_robot.describe()
