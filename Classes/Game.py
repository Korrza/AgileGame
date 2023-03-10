from Classes.Character import Robot, Player
from Classes.PlayerType import PlayerType
from Utils.character_manager import create_robot, assign_player_type, create_player
from colorama import init

init(autoreset=True)


class Game:

    def __init__(self, multiplayer: bool, players_type: list[PlayerType]):
        self.players = []
        self.turn = 0
        self.multiplayer = multiplayer
        self.players_type = players_type

    def get_players(self) -> list[Player | Robot]:
        if self.multiplayer:
            first_player_type = self.players_type[0]
            second_player_type = self.players_type[1]

            self.players.append(create_player(first_player_type))
            self.players.append(create_player(second_player_type, second_player=True))

        else:
            self.players.append(create_player(self.players_type[0]))
            self.players.append(create_robot())

        return self.players

    # def get_winner(self):
    #     if self.players[0].statistics.current_hp <= 0 and self.players[1].statistics.current_hp <= 0:
    #         return None
    #     elif self.players[1].statistics.current_hp <= 0:
    #         return self.players[0]
    #     elif self.players[0].statistics.current_hp <= 0:
    #         return self.players[1]
    #     else:
    #         return None

    # def launch_game(self):
    #     self.get_players()
    #
    #     # Game loop
    #     self.turn = 1
    #
    #     while self.players[0].statistics.current_hp > 0 and self.players[1].statistics.current_hp > 0:
    #         self.launch_turn()
    #
    #     winner = self.get_winner()
    #     display_winner(winner)
    #     manage_xp(winner)
    #
    #     print(f"{Fore.LIGHTCYAN_EX}Do you want to restart the game ? (y/n)\n")
    #
    #     key_pressed = key.getch()
    #     if key_pressed == b'y':
    #         self.restart_game()
    #     else:
    #         print(f"{Fore.LIGHTCYAN_EX}Thanks for playing !")

    # def restart_game(self):
    #     print(f"{Fore.LIGHTCYAN_EX}Restarting game\n")
    #     self.players = []
    #     self.turn = 0
    #     self.launch_game()
