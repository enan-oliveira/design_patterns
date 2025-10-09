from ui_factory import UIFactory

class Application:
    def __init__(self, factory: UIFactory):
        self.button = factory.create_button()
        self.menu = factory.create_menu()

    def render_ui(self):
        self.button.render()
        self.menu.render()
