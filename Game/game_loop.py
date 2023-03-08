import json
import math
import random
from time import sleep

import msvcrt as key
from Character import Player, Robot
from Spell import Spell
from Statistics import Statistics


class Game:

    def __init__(self):
        self.players = []
        self.turn = 0

    def get_players_number(self):
        while True:
            players_number = input("How many players? (1 or 2): ")
            if players_number in {'1', '2'}:
                break
            print("Please enter 1 or 2")

        if players_number == '1':
            self.players.append(create_player())
            self.players.append(create_robot())
        elif players_number == '2':
            self.players.append(create_player())
            self.players.append(create_player(True))

    def launch_turn(self):
        print("Turn " + str(self.turn))
        sleep(0.1)
        for player in self.players:
            # Tour du joueur en cours
            if player.statistics.current_hp > 0:
                spell = get_spell(player)
                target = self.players[0] if player == self.players[1] else self.players[1]
                launch_spell(spell, target, player)

                display_hp(player, target)

        self.turn += 1

    def get_winner(self):
        if self.players[0].statistics.current_hp <= 0 and self.players[1].statistics.current_hp <= 0:
            return None
        elif self.players[1].statistics.current_hp <= 0:
            return self.players[0]
        elif self.players[0].statistics.current_hp <= 0:
            return self.players[1]
        else:
            return None

    def launch_game(self):
        self.get_players_number()

        # Game loop
        self.turn = 1

        while self.players[0].statistics.current_hp > 0 and self.players[1].statistics.current_hp > 0:
            self.launch_turn()

        winner = self.get_winner()
        display_winner(winner)
        manage_xp(winner)

        print("Do you want to restart the game ? (y/n)")

        key_pressed = key.getch()
        if key_pressed == b'y':
            self.restart_game()
        else:
            print("Thanks for playing !")

    def restart_game(self):
        print("Restarting game")
        self.launch_game()


def create_player(second_player: bool = False) -> Player:
    with open("spells.json", "r") as f:
        spell_data = json.load(f)

    spells = [Spell(**spell) for spell in spell_data]

    return Player(1, Statistics(100, 100, 10, 10, 0, 0), spells, 0,
                  second_player=second_player)


def create_robot() -> Robot:
    with open("spells.json", "r") as f:
        spell_data = json.load(f)

    spells = [Spell(**spell) for spell in spell_data]

    return Robot(1, Statistics(100, 100, 10, 10, 0, 0), spells, 0)


def get_spell(character: Player | Robot) -> Spell:
    key_pressed = key.getch()

    match key_pressed:
        case b'a':
            return character.spells[0]
        case b'z':
            return character.spells[1]
        case b'e':
            return character.spells[2]
        case b'r':
            return character.spells[3]


def display_hp(player: Player | Robot, target: Player | Robot):
    print(f"{target.name}", "light_magenta" + " has " + str(target.statistics.current_hp) + " life points left")
    print(f"{player.name}", "light_blue" + " has " + str(player.statistics.current_hp) + " life points left\n")


def compute_damage(attack: int, power: int) -> int:
    return math.ceil(attack * (power / 100))


def launch_spell(spell: Spell, target: Player | Robot, caster: Player | Robot):
    if random.randint(1, 100) > spell.accuracy:
        print("The spell missed !")

    if spell.types.get("attack"):
        damage = compute_damage(spell.power, caster.statistics.attack)
        target.statistics.current_hp -= damage
        print(caster.name + " used " + spell.name + " on " + target.name + " and deal " + str(damage) + " damage!")

    if spell.types.get("heal"):
        heal = compute_damage(spell.power, caster.statistics.attack)
        caster.statistics.current_hp += heal
        print(caster.name + " used " + spell.name + " on " + caster.name + " and healed for " + str(heal) + " points!")

    if spell.types.get("buff"):
        # TODO add buff to caster
        print(caster.name + " used " + spell.name + " on " + caster.name + " !")


def display_winner(winner: Player | Robot):
    if winner is None:
        print("It's a draw ! \n")
    else:
        print("The winner is " + winner.name + " ! \n")


def manage_xp(winner: Player | Robot):
    if winner is not None:
        print(str(winner.name) + " gained " + str(10) + " experience points \n")
    else:
        print("Both players gained " + str(5) + " experience points \n")