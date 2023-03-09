from Classes.Character import Player, Robot
from colorama import init, Fore

init(autoreset=True)


def display_winner(winner: Player | Robot) -> str:
    if winner is None:
        text = "IT'S A DRAW !"
    else:
        text = f"{winner.name.upper()} WON !"
    return text


def display_hp(player: Player | Robot, target: Player | Robot):
    print(f"{Fore.LIGHTBLUE_EX}{target.name} {Fore.LIGHTCYAN_EX}has {Fore.LIGHTGREEN_EX}{target.statistics.current_hp} {Fore.LIGHTCYAN_EX}life points left.")
    print(f"{Fore.LIGHTBLUE_EX}{player.name} {Fore.LIGHTCYAN_EX}has {Fore.LIGHTGREEN_EX}{player.statistics.current_hp} {Fore.LIGHTCYAN_EX}life points left\n")