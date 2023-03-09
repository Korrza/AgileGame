import random
from time import sleep
import msvcrt as key

from Classes.Character import Robot
from Constants.inputs import PLAYERS_NB_MESSAGE, PLAYERS_NB_CHOICES, CHARACTER_MESSAGE, CHARACTER_CHOICES
from Utils.character_manager import create_robot, get_spell, launch_spell, manage_xp, \
    assign_player_type, create_player, read_player_input
from Utils.displayer import display_winner, display_hp
from colorama import init, Fore

init(autoreset=True)


class Game:

    def __init__(self):
        self.players = []
        self.turn = 0

    def get_players(self):
        players_number = read_player_input(PLAYERS_NB_MESSAGE, PLAYERS_NB_CHOICES)

        if players_number == '1':
            player_type_choice = read_player_input(CHARACTER_MESSAGE, CHARACTER_CHOICES)

            player_type = assign_player_type(player_type_choice)

            self.players.append(create_player(player_type))
            self.players.append(create_robot())

        elif players_number == '2':
            first_player_type_choice = read_player_input(CHARACTER_MESSAGE, CHARACTER_CHOICES)
            second_player_type_choice = read_player_input(CHARACTER_MESSAGE, CHARACTER_CHOICES)

            first_player_type = assign_player_type(first_player_type_choice)
            second_player_type = assign_player_type(second_player_type_choice)

            self.players.append(create_player(first_player_type))
            self.players.append(create_player(second_player_type, second_player=True))

        print(f"\n{Fore.LIGHTBLUE_EX}{self.players[0].name} {Fore.LIGHTCYAN_EX}VS {Fore.LIGHTBLUE_EX}{self.players[1].name}")

    def launch_turn(self):
        print(f"\n{Fore.LIGHTCYAN_EX}TURN {self.turn}")
        sleep(0.1)
        for player in self.players:
            if player.statistics.current_hp > 0:
                if isinstance(player, Robot):
                    spell_index = random.randint(0, len(player.spells) - 1)
                    spell = player.spells[spell_index]
                else:
                    spell = get_spell(player)

                target = self.players[0] if player == self.players[1] else self.players[1]
                spell_success = launch_spell(spell, target, player)
                if spell_success:
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
        self.get_players()

        # Game loop
        self.turn = 1

        while self.players[0].statistics.current_hp > 0 and self.players[1].statistics.current_hp > 0:
            self.launch_turn()

        winner = self.get_winner()
        display_winner(winner)
        manage_xp(winner)

        print(f"{Fore.LIGHTCYAN_EX}Do you want to restart the game ? (y/n)\n")

        key_pressed = key.getch()
        if key_pressed == b'y':
            self.restart_game()
        else:
            print(f"{Fore.LIGHTCYAN_EX}Thanks for playing !")

    def restart_game(self):
        print(f"{Fore.LIGHTCYAN_EX}Restarting game\n")
        self.players = []
        self.turn = 0
        self.launch_game()
