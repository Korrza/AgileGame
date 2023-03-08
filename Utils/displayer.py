from Classes.Character import Player, Robot
from colorama import init, Fore

init(autoreset=True)


def display_winner(winner: Player | Robot):
    if winner is None:
        print(f"{Fore.LIGHTWHITE_EX}IT'S A DRAW ! \n")
    else:
        print(f"{Fore.LIGHTCYAN_EX}THE WINNER IS {Fore.LIGHTWHITE_EX}{winner.name} {Fore.LIGHTCYAN_EX}! \n")


def display_hp(player: Player | Robot, target: Player | Robot):
    print(f"{Fore.LIGHTBLUE_EX}{target.name} {Fore.LIGHTCYAN_EX}has {Fore.LIGHTGREEN_EX}{str(target.statistics.current_hp)} {Fore.LIGHTCYAN_EX}life points left.")
    print(f"{Fore.LIGHTBLUE_EX}{player.name} {Fore.LIGHTCYAN_EX}has {Fore.LIGHTGREEN_EX}{str(player.statistics.current_hp)} {Fore.LIGHTCYAN_EX}life points left\n")