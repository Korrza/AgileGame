from Classes.Game import Game
from colorama import init, Fore

init(autoreset=True)

print(f"{Fore.LIGHTCYAN_EX}WELCOME TO THE AGILE GAME!\n")

# launch game
game = Game()
game.launch_game()

# if no, exit game1
