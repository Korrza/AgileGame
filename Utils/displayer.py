from Classes.Character import Player, Robot


def display_winner(winner: Player | Robot):
    if winner is None:
        print("It's a draw ! \n")
    else:
        print("The winner is " + winner.name + " ! \n")


def display_hp(player: Player | Robot, target: Player | Robot):
    print(f"{target.name}", "light_magenta" + " has " + str(target.statistics.current_hp) + " life points left")
    print(f"{player.name}", "light_blue" + " has " + str(player.statistics.current_hp) + " life points left\n")