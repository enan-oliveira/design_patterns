from abc import ABC, abstractmethod

class Robot:
    def __init__(self):
        self.parts = {}

    def add_part(self, part_name, value):
        self.parts[part_name] = value

    def describe(self):
        print("🤖 Robot Configuration:")
        for part, value in self.parts.items():
            print(f"  - {part}: {value}")
        print()
