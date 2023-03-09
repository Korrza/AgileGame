import arcade
import arcade.gui


def quit_game(event):
    print("Quit Game")
    arcade.close_window()


def create_button(h_box, text):
    spell = arcade.gui.UIFlatButton(text=f"{text}", width=200)
    h_box.add(spell.with_space_around(right=10, bottom=20))

    return spell
