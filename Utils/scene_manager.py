import arcade
import arcade.gui


def quit_game(event):
    print("Quit Game")
    arcade.close_window()


def create_button(h_box, text, enabled: bool = True):
    spell_button = arcade.gui.UIFlatButton(text=f"{text}", width=200)
    spell_button.enabled = enabled
    h_box.add(spell_button.with_space_around(right=10, bottom=20))

    return spell_button
