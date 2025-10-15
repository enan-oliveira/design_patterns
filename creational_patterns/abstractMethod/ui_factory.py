from abc import ABC, abstractmethod

from button import Button
from menu import Menu

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_menu(self) -> Menu:
        pass
