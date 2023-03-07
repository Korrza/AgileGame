import msvcrt as key
from time import sleep
from termcolor import colored
from Actions import Attacks, Healing
from Character import Player, Robot
from Statistics import Statistics


class Game:
    
    def __init__(self):
        self.players_number = 0
        self.player1 = None
        self.player2 = None
        self.turn = 0

    def launch_game(self):
        # Create 2 players
        self.get_player_number()
        self.create_players()

        # Game loop
        self.turn = 1
        winner = ""

        while self.player1.statistics.current_hp > 0 and self.player2.statistics.current_hp > 0:
            self.launch_turn()

        winner = self.get_winner()
        self.display_winner(winner)
        self.manage_xp(winner)

        print("Do you want to restart the game ? (y/n)")
        # print(key.getch())

        # self.restart_game()

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
            self.player1 = Player(1, Statistics(100, 100, Attacks(1), Healing(1), 0))
            self.player2 = Robot(2, Statistics(100, 100, Attacks(1), Healing(1), 0))
        elif self.players_number == '2':
            self.player1 = Player(1, Statistics(100, 100, Attacks(1), Healing(1), 0))
            self.player2 = Player(2, Statistics(100, 100, Attacks(1), Healing(1), 0), second_player=True)

    def launch_turn(self):
        print(colored("Turn " + str(self.turn) + "", 'red', None, attrs=['bold']))
        sleep(0.5)
        
        # Player 1 turn
        print(colored("Player 1", "light_blue") + " attack !")

        self.player2.statistics.current_hp -= 10

        print(colored("Player 1", "light_blue") + " deal " + colored(str(10), "red") + " damage to Player 2")
        print(colored("Player 2", "light_magenta") + " has " + colored(str(self.player2.statistics.current_hp), "light_green") + " life points left \n")

        # Player 2 turn
        print(colored("Player 2", "light_magenta") + " attack !")
        self.player1.statistics.current_hp -= 10

        print(colored("Player 2", "light_magenta") + " deal " + colored(str(10), "red") + " damage to Player 1")
        print(colored("Player 1", "light_blue") + " has " + colored(str(self.player1.statistics.current_hp), "light_green") + " life points left \n")
        sleep(0.5)

        self.turn += 1

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