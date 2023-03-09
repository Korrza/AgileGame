import arcade
import arcade.gui
from Interface.SceneProperties import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from Interface.View.MenuScene import MenuView
from Interface.View.GameScene import GameView


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
