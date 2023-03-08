from time import sleep
import msvcrt as key

from Utils.character_manager import create_player, create_robot, get_spell, launch_spell, manage_xp
from Utils.displayer import display_winner, display_hp
from colorama import init, Fore

init(autoreset=True)


class Game:

    def __init__(self):
        self.players = []
        self.turn = 0

    def get_players_number(self):
        while True:
            players_number = input(Fore.LIGHTCYAN_EX + "How many players? (1 or 2): ")
            if players_number in {'1', '2'}:
                break
            print(Fore.LIGHTRED_EX + "Please enter 1 or 2")

        if players_number == '1':
            self.players.append(create_player())
            self.players.append(create_robot())
        elif players_number == '2':
            self.players.append(create_player())
            self.players.append(create_player(True))

        print(f"\n{Fore.LIGHTBLUE_EX}{self.players[0].name} {Fore.LIGHTCYAN_EX}VS {Fore.LIGHTBLUE_EX}{self.players[1].name}")

    def launch_turn(self):
        print(Fore.LIGHTCYAN_EX + "\nTURN " + str(self.turn))
        sleep(0.1)
        for player in self.players:
            if player.statistics.current_hp > 0:
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
        self.get_players_number()

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
