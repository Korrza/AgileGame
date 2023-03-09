import arcade
import arcade.gui

from Interface.SceneProperties import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from Interface.View.GameScene import GameView
from Utils.scene_manager import quit_game


class MenuView(arcade.View):
    BUTTON_WIDTH = 200
    BUTTON_MARGIN_BOTTOM = 20
    START_BUTTON = "Start Game"
    QUIT_BUTTON = "Quit Game"

    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text=self.START_BUTTON, width=self.BUTTON_WIDTH)
        self.v_box.add(start_button.with_space_around(bottom=self.BUTTON_MARGIN_BOTTOM))
        start_button.on_click = self.start_button

        quit_button = arcade.gui.UIFlatButton(text=self.QUIT_BUTTON, width=self.BUTTON_WIDTH)
        self.v_box.add(quit_button)
        quit_button.on_click = quit_game

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def start_button(self, event):
        print(self.START_BUTTON)
        game_view = GameView()
        self.window.show_view(game_view)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_draw(self):
        self.clear()
        self.manager.draw()
        arcade.draw_text(SCREEN_TITLE, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text(":D", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 135,
                         arcade.color.GRAY, font_size=20, anchor_x="center")