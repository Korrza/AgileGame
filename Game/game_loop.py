import json
import math
import msvcrt as key
import random
from time import sleep
from termcolor import colored
from Character import Player, Robot
from Spell import Spell
from Statistics import Statistics


class Game:
    
    def __init__(self):
        self.players_number = 0
        self.player1 = None
        self.player2 = None
        self.turn = 0

    def launch_game(self):
        self.get_player_number()
        self.create_players()

        # Game loop
        self.turn = 1

        while self.player1.statistics.current_hp > 0 and self.player2.statistics.current_hp > 0:
            self.launch_turn()

        winner = self.get_winner()
        self.display_winner(winner)
        self.manage_xp(winner)

        print("Do you want to restart the game ? (y/n)")
        
        key_pressed = key.getch()
        if key_pressed == b'y':
            self.restart_game()
        else:
            print("Thanks for playing !")

    def restart_game(self):
        print("Restarting game")
        self.launch_game()

    def get_player_number(self):
        while self.players_number != '1' and self.players_number != '2':
            self.players_number = input("How many players ? '(1 or 2)' ")

            if self.players_number != '1' and self.players_number != '2':
                print("Please enter 1 or 2")

    def create_players(self):
        if self.players_number == '1':
            self.player1 = self.create_one_character()
            self.player2 = self.create_robot_character()
        elif self.players_number == '2':
            self.player1 = self.create_one_character()
            self.player2 = self.create_one_character(True)

    def create_one_character(self, second_player: bool = False):
        spells = json.load(open('spells.json'))
        character = Player(1, Statistics(100, 100, 10, 10, 0, 0), [Spell(**spells[0]), Spell(**spells[1]), Spell(**spells[2]), Spell(**spells[4])], 0, second_player = second_player)
        return character

    def create_robot_character(self):
        spells = json.load(open('spells.json'))
        character = Robot(1, Statistics(100, 100, 10, 10, 0, 0) , [Spell(**spells[0]), spells[1], spells[2], spells[4]], 0)
        return character

    def launch_turn(self):
        print(colored("Turn " + str(self.turn) + "", 'red', None, attrs=['bold']))
        sleep(0.1)
        
        # Player 1 turn
        spell = self.get_spell(self.player1)
        self.launch_spell(spell, self.player2, self.player1)
        print(colored("Player 1", "light_blue") + " attack !")

        print(colored("Player 2", "light_magenta") + " has " + colored(str(self.player2.statistics.current_hp), "light_green") + " life points left \n")

        # Player 2 turn
        print(colored("Player 2", "light_magenta") + " attack !")
        self.player1.statistics.current_hp -= 10

        print(colored("Player 2", "light_magenta") + " deal " + colored(str(10), "red") + " damage to Player 1")
        print(colored("Player 1", "light_blue") + " has " + colored(str(self.player1.statistics.current_hp), "light_green") + " life points left \n")
        sleep(0.1)

        self.turn += 1

    def get_spell(self, player: Player | Robot):
        key_pressed = key.getch()

        match key_pressed:
            case b'a':
                return player.spells[0]
            case b'z':
                return player.spells[1]
            case b'e':
                return player.spells[2]
            case b'r':
                return player.spells[3]


    def launch_spell(self, spell : Spell, target: Player | Robot, caster: Player | Robot):
        if random.randint(1, 100) > spell.accuracy:
            print("The spell missed !")

        if spell.types.attack:
            target.statistics.current_hp -= self.compute_damage(spell.power, caster.statistics.attack)
            print(caster.name + " used " + spell.name + " on " + target.name + " !")

        if spell.types.heal:
            caster.statistics.current_hp += self.compute_damage(spell.power, caster.statistics.attack)
            print(caster.name + " used " + spell.name + " on " + caster.name + " !")

        if spell.types.buff:
            # TODO add buff to caster
            print(caster.name + " used " + spell.name + " on " + caster.name + " !")

    @staticmethod
    def compute_damage(attack, power):
        return math.ceil(attack * (power / 100))

    def get_winner(self):
        if self.player1.statistics.current_hp <= 0 and self.player2.statistics.current_hp <= 0:
            return None
        elif self.player2.statistics.current_hp <= 0:
            return self.player1
        elif self.player1.statistics.current_hp <= 0:
            return self.player2
        else:
            return None

    @staticmethod
    def display_winner(winner: Player | Robot):
        if winner is None:
            print("It's a draw ! \n")
        else:
            print("The winner is " + winner.name + " ! \n")

    @staticmethod
    def manage_xp(winner: Player | Robot):
        if winner is not None:
            print(str(winner.name) + " gained " + str(10) + " experience points \n")
        else:
            print("Both players gained " + str(5) + " experience points \n")