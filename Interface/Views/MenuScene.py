import arcade
import arcade.gui

from Interface.SceneProperties import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from Interface.Views.GameScene import GameView


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        self.menu_background = None
        self.menu_gradient = None

        self.menu_setup()

    def menu_setup(self):
        self.menu_background = arcade.load_texture("Resources/Backgrounds/menu_background.png")

        start_button = arcade.gui.UIFlatButton(text="1 Player", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))
        start_button.on_click = self.show_view

        start_button = arcade.gui.UIFlatButton(text="2 Player", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))
        start_button.on_click = self.show_multi_view

        quit_button = arcade.gui.UIFlatButton(text="Quit Game", width=200)
        self.v_box.add(quit_button)
        quit_button.on_click = self.quit_game

        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))

        self.menu_gradient = arcade.create_ellipse_filled_with_colors(SCREEN_WIDTH / 2, SCREEN_HEIGHT + 50,
                                                                      SCREEN_WIDTH, SCREEN_HEIGHT,
                                                                      inside_color=(255, 201, 66, 255),
                                                                      outside_color=(212, 88, 246, 0))

    def draw_menu(self):
        self.menu_gradient.draw()
        self.manager.draw()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.menu_background)
        arcade.draw_text(SCREEN_TITLE, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

    def show_view(self, event):
        self.window.show_view(SoloChooserView())

    def show_multi_view(self, event):
        self.window.show_view(MultiChooserView())

    @staticmethod
    def quit_game(event):
        print("Quit Game")
        arcade.close_window()

    def on_show_view(self):
        arcade.set_background_color([135, 124, 248])

    def on_draw(self):
        self.clear()
        self.draw_menu()


class SoloChooserView(arcade.View):
    def __init__(self):
        super().__init__()
        self.character_manager = arcade.gui.UIManager()
        self.cm_b_manager = arcade.gui.UIManager()
        self.stats_box_manager = arcade.gui.UIManager()

        self.cm_b_box = arcade.gui.UIBoxLayout(vertical=False)
        self.cm_box = arcade.gui.UIBoxLayout(vertical=False)
        self.stats_box = arcade.gui.UIBoxLayout()

        self.char_select_background = None
        self.char_select_gradient = None
        self.character_sprite = None
        self.stats_sprites = []

        self.character_selection_setup()

    def character_selection_setup(self):
        self.character_manager.enable()
        self.cm_b_manager.enable()
        self.stats_box_manager.enable()

        self.char_select_background = arcade.load_texture("Resources/Backgrounds/char_select_background.png")

        back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        start_button = arcade.gui.UIFlatButton(text="Start !", width=300)
        self.cm_b_box.add(back_button.with_space_around(right=15, bottom=30))
        self.cm_b_box.add(start_button.with_space_around(left=15, bottom=30))
        start_button.on_click = self.launch_game
        back_button.on_click = self.back_to_menu

        self.character_sprite = arcade.Sprite("Resources/Characters/Sound.png", scale=0.4,
                                              center_x=SCREEN_WIDTH/2, center_y=SCREEN_HEIGHT/2)

        sprite_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture("Resources/Buttons/Fairy_button.png"), scale=0.75,
            texture_hovered=arcade.load_texture("Resources/Buttons/Fairy_button_hover.png"))
        self.cm_box.add(sprite_button.with_space_around(right=30, bottom=150))
        sprite_button.on_click = self.switch_to_fairy

        sprite_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture("Resources/Buttons/Warrior_button.png"), scale=0.75,
            texture_hovered=arcade.load_texture("Resources/Buttons/Warrior_button_hover.png"))
        self.cm_box.add(sprite_button.with_space_around(bottom=150))
        sprite_button.on_click = self.switch_to_warrior

        sprite_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture("Resources/Buttons/Sound_button.png"), scale=0.75,
            texture_hovered=arcade.load_texture("Resources/Buttons/Sound_button_hover.png"))
        self.cm_box.add(sprite_button.with_space_around(left=30, bottom=150))
        sprite_button.on_click = self.switch_to_sound

        self.cm_b_manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.cm_b_box))
        self.character_manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x",
                                                             anchor_y="bottom", child=self.cm_box))

        self.char_select_gradient = arcade.create_ellipse_filled_with_colors(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                                                                             SCREEN_WIDTH, SCREEN_HEIGHT,
                                                                             inside_color=(16, 29, 68),
                                                                             outside_color=(12, 43, 70))

        self.set_player_stats()

    def set_player_stats(self):
        self.stats_sprites.append(arcade.Sprite("Resources/Icons/heart_icon.png"))
        self.stats_sprites.append(arcade.Sprite("Resources/Icons/attack_icon.png"))
        self.stats_sprites.append(arcade.Sprite("Resources/Icons/mana_icon.png"))
        self.stats_sprites.append(arcade.Sprite("Resources/Icons/speed_icon.png"))

        for stats_sprite in self.stats_sprites:
            self.stats_box.add(arcade.gui.UISpriteWidget(sprite=stats_sprite, width=60, height=60))

        self.stats_box_manager.add(arcade.gui.UIAnchorWidget(anchor_x="left", anchor_y="center_y", align_x=300,
                                                             child=self.stats_box))

    def draw_player_spells(self):
        for i in range(4):
            arcade.draw_rectangle_filled(SCREEN_WIDTH - 300, SCREEN_HEIGHT - 220 - i * 110, 350, 100,
                                         color=(10, 10, 10, 150))
            arcade.draw_text(f"Fire Ball {i + 1}", SCREEN_WIDTH - 460, SCREEN_HEIGHT - 180 - i * 110,
                             color=arcade.color.WHITE, anchor_x="left", anchor_y="top", font_size=20)
            arcade.draw_text(f"Power : {i * 15 + 5}", SCREEN_WIDTH - 460, SCREEN_HEIGHT - 210 - i * 110,
                             color=arcade.color.WHITE, anchor_x="left", anchor_y="top", font_size=12)
            arcade.draw_text(f"cooldown : {i + 1}", SCREEN_WIDTH - 140, SCREEN_HEIGHT - 210 - i * 110,
                             color=arcade.color.WHITE, anchor_x="right", anchor_y="top", font_size=12)
            arcade.draw_text(f"Launch a Fire Ball that deal fire damages, caster and target have a chance to be burn",
                             SCREEN_WIDTH - 460, SCREEN_HEIGHT - 260 - i * 110,
                             color=arcade.color.WHITE, anchor_x="left", anchor_y="bottom", font_size=10,
                             multiline=True, width=325)


    def switch_to_fairy(self, event):
        self.character_sprite.texture = arcade.load_texture("Resources/Characters/Fairy.png")

    def switch_to_warrior(self, event):
        self.character_sprite.texture = arcade.load_texture("Resources/Characters/Warrior.png")

    def switch_to_sound(self, event):
        self.character_sprite.texture = arcade.load_texture("Resources/Characters/Sound.png")

    def draw_solo_character_selection(self):
        self.char_select_gradient.draw()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.char_select_background)
        self.character_manager.draw()
        self.cm_b_manager.draw()

        arcade.draw_text("1 VS IA", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 75,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        self.character_sprite.draw()
        self.stats_box_manager.draw()
        self.show_stats_values()

    @staticmethod
    def show_stats_values():
        arcade.draw_text("100", 270, SCREEN_HEIGHT / 2 + 80, arcade.color.WHITE,
                         font_size=20, anchor_x="center")
        arcade.draw_text("15", 270, SCREEN_HEIGHT / 2 + 15, arcade.color.WHITE,
                         font_size=20, anchor_x="center")
        arcade.draw_text("50", 270, SCREEN_HEIGHT / 2 - 45, arcade.color.WHITE,
                         font_size=20, anchor_x="center")
        arcade.draw_text("10", 270, SCREEN_HEIGHT / 2 - 105, arcade.color.WHITE,
                         font_size=20, anchor_x="center")

    def back_to_menu(self, event):
        self.window.show_view(MenuView())

    def launch_game(self, event):
        self.window.show_view(GameView())

    def on_show_view(self):
        arcade.set_background_color([135, 124, 248])

    def on_draw(self):
        self.clear()
        self.draw_solo_character_selection()
        self.draw_player_spells()


class MultiChooserView(arcade.View):
    def __init__(self):
        super().__init__()
        self.character_manager = arcade.gui.UIManager()
        self.cm_b_manager = arcade.gui.UIManager()

        self.cm_b_box = arcade.gui.UIBoxLayout(vertical=False)
        self.left_cm_box = arcade.gui.UIBoxLayout(vertical=False)
        self.right_cm_box = arcade.gui.UIBoxLayout(vertical=False)

        self.char_select_background = None
        self.char_select_gradient = None
        self.p1_character_sprite = None
        self.p2_character_sprite = None

        self.character_selection_setup()

    def character_selection_setup(self):
        self.character_manager.enable()
        self.cm_b_manager.enable()

        self.char_select_background = arcade.load_texture("Resources/Backgrounds/char_select_background.png")

        back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        start_button = arcade.gui.UIFlatButton(text="Start !", width=300)
        self.cm_b_box.add(back_button.with_space_around(right=15, bottom=30))
        self.cm_b_box.add(start_button.with_space_around(left=15, bottom=30))
        start_button.on_click = self.launch_game
        back_button.on_click = self.back_to_menu

        self.p1_character_sprite = arcade.Sprite("Resources/Characters/Sound.png", scale=0.4,
                                              center_x=SCREEN_WIDTH/2 - 300, center_y=SCREEN_HEIGHT/2)

        self.p2_character_sprite = arcade.Sprite("Resources/Characters/Warrior.png", scale=0.4,
                                                 center_x=SCREEN_WIDTH / 2 + 300, center_y=SCREEN_HEIGHT / 2)

        self.character_select(False)
        self.character_select(True)

        self.char_select_gradient = arcade.create_ellipse_filled_with_colors(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                                                                             SCREEN_WIDTH, SCREEN_HEIGHT,
                                                                             inside_color=(16, 29, 68),
                                                                             outside_color=(12, 43, 70))

    def character_select(self, multiplayer: bool):
        box = self.left_cm_box if multiplayer else self.right_cm_box
        sprite_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture("Resources/Buttons/Fairy_button.png"), scale=0.75,
            texture_hovered=arcade.load_texture("Resources/Buttons/Fairy_button_hover.png"))
        box.add(sprite_button.with_space_around(right=30, bottom=150))
        sprite_button.on_click = self.p1_switch_to_fairy if multiplayer else self.p2_switch_to_fairy

        sprite_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture("Resources/Buttons/Warrior_button.png"), scale=0.75,
            texture_hovered=arcade.load_texture("Resources/Buttons/Warrior_button_hover.png"))
        box.add(sprite_button.with_space_around(bottom=150))
        sprite_button.on_click = self.p1_switch_to_warrior if multiplayer else self.p2_switch_to_warrior

        sprite_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture("Resources/Buttons/Sound_button.png"), scale=0.75,
            texture_hovered=arcade.load_texture("Resources/Buttons/Sound_button_hover.png"))
        box.add(sprite_button.with_space_around(left=30, bottom=150))
        sprite_button.on_click = self.p1_switch_to_sound if multiplayer else self.p2_switch_to_sound

        offset = -300 if multiplayer else 300
        self.cm_b_manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.cm_b_box))
        self.character_manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", align_x=offset,
                                                             anchor_y="bottom", child=box))

    def p1_switch_to_fairy(self, event):
        self.p1_character_sprite.texture = arcade.load_texture("Resources/Characters/Fairy.png")

    def p1_switch_to_warrior(self, event):
        self.p1_character_sprite.texture = arcade.load_texture("Resources/Characters/Warrior.png")

    def p1_switch_to_sound(self, event):
        self.p1_character_sprite.texture = arcade.load_texture("Resources/Characters/Sound.png")

    def p2_switch_to_fairy(self, event):
        self.p2_character_sprite.texture = arcade.load_texture("Resources/Characters/Fairy.png")

    def p2_switch_to_warrior(self, event):
        self.p2_character_sprite.texture = arcade.load_texture("Resources/Characters/Warrior.png")

    def p2_switch_to_sound(self, event):
        self.p2_character_sprite.texture = arcade.load_texture("Resources/Characters/Sound.png")

    def draw_solo_character_selection(self):
        self.char_select_gradient.draw()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.char_select_background)
        self.character_manager.draw()
        self.cm_b_manager.draw()
        arcade.draw_text("1 VS 1", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 75,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        self.p1_character_sprite.draw()
        self.p2_character_sprite.draw()

    def back_to_menu(self, event):
        self.window.show_view(MenuView())
        pass

    def launch_game(self, event):
        self.window.show_view(GameView())

    def on_show_view(self):
        arcade.set_background_color([135, 124, 248])

    def on_draw(self):
        self.clear()
        self.draw_solo_character_selection()

