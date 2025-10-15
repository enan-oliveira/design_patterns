from ui_factory import UIFactory
from button import Button
from menu import Menu
from dark_button import DarkButton
from dark_menu import DarkMenu

class DarkFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_menu(self) -> Menu:
        return DarkMenu()
