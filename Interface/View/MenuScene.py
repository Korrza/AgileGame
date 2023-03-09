import arcade
import arcade.gui

from Interface.SceneProperties import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from Interface.View.GameScene import GameView


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))
        start_button.on_click = self.start_button

        quit_button = arcade.gui.UIFlatButton(text="Quit Game", width=200)
        self.v_box.add(quit_button)
        quit_button.on_click = self.quit_game

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def start_button(self, event):
        print("Start Game")
        game_view = GameView()
        self.window.show_view(game_view)

    @staticmethod
    def quit_game(event):
        print("Quit Game")
        arcade.close_window()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_draw(self):
        self.clear()
        self.manager.draw()
        arcade.draw_text(SCREEN_TITLE, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text(":D", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 135,
                         arcade.color.GRAY, font_size=20, anchor_x="center")