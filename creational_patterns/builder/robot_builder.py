from abc import ABC, abstractmethod

from robot import Robot

class RobotBuilder(ABC):
    def __init__(self):
        self.robot = Robot()

    @abstractmethod
    def build_head(self): pass

    @abstractmethod
    def build_body(self): pass

    @abstractmethod
    def build_arms(self): pass

    @abstractmethod
    def build_legs(self): pass

    def get_robot(self):
        return self.robot
