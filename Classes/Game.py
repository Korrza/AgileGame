import random
from time import sleep
import msvcrt as key

from Classes.Character import Robot
from Utils.character_manager import create_robot, get_spell, launch_spell, manage_xp, \
    choose_character_type
from Utils.displayer import display_winner, display_hp
from colorama import init, Fore

init(autoreset=True)


class Game:

    def __init__(self):
        self.players = []
        self.turn = 0

    def get_players(self):
        while True:
            players_number = input(f"{Fore.LIGHTCYAN_EX}How many players? (1 or 2): ")
            if players_number in {'1', '2'}:
                break
            print(f"{Fore.LIGHTRED_EX}Please enter 1 or 2")

        if players_number == '1':
            choose_character_type(self.players)
            self.players.append(create_robot())

        elif players_number == '2':
            choose_character_type(self.players)
            choose_character_type(self.players, second_player=True)

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
