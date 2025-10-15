from ui_factory import UIFactory
from button import Button
from menu import Menu
from light_button import LightButton
from light_menu import LightMenu

class LightFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_menu(self) -> Menu:
        return LightMenu()
