from time import sleep
import msvcrt as key

from Utils.character_manager import create_player, create_robot, get_spell, launch_spell, manage_xp
from Utils.displayer import display_winner, display_hp


class Game:

    def __init__(self):
        self.players = []
        self.turn = 0

    def get_players_number(self):
        # while True:
        #     players_number = input("How many players? (1 or 2): ")
        #     if players_number in {'1', '2'}:
        #         break
        #     print("Please enter 1 or 2")
        #

        players_number = '1'

        if players_number == '1':
            self.players.append(create_player())
            self.players.append(create_robot())
        elif players_number == '2':
            self.players.append(create_player())
            self.players.append(create_player(True))

        return self.players

    def launch_turn(self):
        print("Turn " + str(self.turn))
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

    # def launch_game(self):
    #     self.get_players_number()
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
    #     print("Do you want to restart the game ? (y/n)")
    #
    #     key_pressed = key.getch()
    #     if key_pressed == b'y':
    #         self.restart_game()
    #     else:
    #         print("Thanks for playing !")

    def restart_game(self):
        print("Restarting game")
        self.launch_game()
