import Statistics
import msvcrt as key
from time import sleep
from termcolor import colored

class Game: 
    
    def __init__(self, players_number: int, player1: Statistics, player2: Statistics):
        self.players_number = players_number
        self.player1 = player1
        self.player2 = player2

    def set_player():
        while players_number != '1' and players_number != '2':
            players_number = input("How many players ? '(1 or 2)' ")

            if players_number != '1' and players_number != '2':
                print("Please enter 1 or 2")


    def launch_game():
        # Create 2 players
        st_life = 100
        st_attack = 10
        st_experience = 0

        nd_life = 100
        nd_attack = 10
        nd_experience = 0

        # Game loop
        Turn = 1
        winner = ""

        while st_life > 0 and nd_life > 0:
            print(colored("Turn " + str(Turn) + "", 'red', None, attrs=['bold']))

            # Player 1 turn
            
            print(key.getch())
            print(colored("Player 1", "light_blue") + " attack !")
            sleep(0.2)

            nd_life = nd_life - st_attack

            print(colored("Player 1", "light_blue") + " dealt " + colored(str(st_attack), "red") + " damage to Player 2")
            print(colored("Player 2", "light_magenta") + " has " + colored(str(nd_life), "light_green") + " life points left \n")

            sleep(0.3)
            # Player 2 turn
            print(colored("Player 2", "light_magenta") + " attack !")
            sleep(0.2)

            st_life = st_life - nd_attack

            print(colored("Player 2", "light_magenta") + " dealt " + colored(str(nd_attack), "red") + " damage to Player 1")
            print(colored("Player 1", "light_blue") + " has " + colored(str(st_life), "light_green") + " life points left \n")

            Turn = Turn + 1

        # End Game loop

        # Display winner
        if st_life <= 0:
            winner = "Player 2"
            nd_experience = nd_experience + 10
        elif nd_life <= 0:
            winner = "Player 1"
            st_experience = st_experience + 10
        else:
            winner = "Nobody"

        print("The winner is " + winner)


        # Display experience points gained
        print(winner + " gained " + str(10) + " experience points \n")

        # Display level up if applicable


        # Display new stats


        # want to restart game?

        print("Do you want to restart the game ? (y/n)")
        print(key.getch())

        # if yes, restart game
        restart_game()

    def restart_game():
        print("Restarting game")
        launch_game()