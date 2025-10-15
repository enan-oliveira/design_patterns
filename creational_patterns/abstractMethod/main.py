from light_factory import LightFactory
from dark_factory import DarkFactory
from application import Application

if __name__ == "__main__":
    theme = input("Escolha o tema (light/dark): ").strip().lower()

    if theme == "light":
        factory = LightFactory()
    elif theme == "dark":
        factory = DarkFactory()
    else:
        raise ValueError("Tema inválido!")

    app = Application(factory)
    app.render_ui()
