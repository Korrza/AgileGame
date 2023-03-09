import arcade
import arcade.gui

from Interface.SceneProperties import SCREEN_WIDTH, SCREEN_HEIGHT
from Classes.Game import Game
from Interface.View.PauseScene import PauseView
from Utils.character_manager import launch_spell
from Utils.scene_manager import create_button


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.players = []
        self.players_spell_played = 0
        self.text = "Choose a spell."
        self.turn = 0
        self.background = None
        self.winner = None

        self.shapes = arcade.ShapeElementList()
        color1 = (98, 47, 89)
        color2 = (24, 23, 71)
        points = (0, 0), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)
        colors = (color1, color1, color2, color2)
        self.shapes.append(arcade.create_rectangle_filled_with_colors(points, colors))

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.pause()

    def pause(self):
        pause_view = PauseView(self)
        self.window.show_view(pause_view)

    def apply_spell(self, spell_info, spell_index):
        print(spell_info)

        if spell_info['damage'] is not None:
            self.players[1].statistics.current_hp = max(self.players[1].statistics.current_hp - spell_info['damage'], 0)
        if spell_info['heal'] is not None:
            self.players[0].statistics.current_hp = min(self.players[0].statistics.current_hp + spell_info['heal'], self.players[0].statistics.max_hp)

        self.text = spell_info['text']
        self.players_spell_played = spell_index + 1

        if self.players[1].statistics.current_hp <= 0:
            self.winner = self.players[1]

    def on_click_spell(self, spell_index):
        spell_info = launch_spell(self.players[0].spells[spell_index], self.players[1], self.players[0])
        self.apply_spell(spell_info, 0)

    def on_show_view(self):
        self.setup()
        self.manager.enable()

        h_box = arcade.gui.UIBoxLayout(vertical=False)

        self.buttons_initialisation(h_box)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=h_box)
        )

    def buttons_initialisation(self, h_box):
        number_of_spells = len(self.players[0].spells)
        for i in range(number_of_spells):
            spell = create_button(h_box, f"Spell {i + 1}")
            spell.on_click = lambda event, spell_index=i: self.on_click_spell(spell_index)

    def setup(self):
        game = Game()
        self.players = game.get_players()
        self.background = arcade.load_texture("Resources/Backgrounds/background.png")

    def on_draw(self):
        self.clear()
        self.shapes.draw()

        # Background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, self.background)
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 100, SCREEN_WIDTH - 50, 100,
                                      [0, 0, 0, 100])

        arcade.draw_text(self.players[0].name, 25, SCREEN_HEIGHT - 40, arcade.color.WHITE, font_size=20,
                         anchor_x="left")
        arcade.draw_text(self.players[1].name,SCREEN_WIDTH - 25, SCREEN_HEIGHT - 40, arcade.color.WHITE, font_size=20,
                         anchor_x="right")
        # Life bar
        arcade.draw_rectangle_filled(150, SCREEN_HEIGHT - 70, 250, 30, [84, 27, 25, 150])
        arcade.draw_rectangle_filled(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 70, 250, 30, [84, 27, 25, 150])
        arcade.draw_rectangle_filled(150, SCREEN_HEIGHT - 70,
                                     self.players[0].statistics.current_hp * 2.5, 30, [70, 147, 70, 255])
        arcade.draw_rectangle_filled(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 70,
                                     self.players[1].statistics.current_hp * 2.5, 30, [70, 147, 70, 255])

        # Dialogue box
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 2, 100, SCREEN_WIDTH - 50, 100,
                                      arcade.color.GRAY, border_width=5)

        arcade.draw_text(self.text, 40, 110, arcade.color.WHITE, font_size=20, anchor_x="left")

        # Turn
        arcade.draw_text(f'Turn {self.turn}', SCREEN_WIDTH / 2, SCREEN_HEIGHT - 60, arcade.color.WHITE, font_size=30,
                         anchor_x="center")

        self.manager.draw()

    def on_update(self, delta_time):

        if self.players[0].statistics.current_hp > 0 and self.players[1].statistics.current_hp > 0:

            if self.players_spell_played != 0:
                self.players_spell_played = 0
                self.turn += 1

        # winner = self.get_winner()
        # display_winner(winner)
        # manage_xp(winner)