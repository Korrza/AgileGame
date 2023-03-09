import json
import math
import random
from Classes.Character import Player, Robot
from Classes.PlayerType import PlayerType
from Classes.Spell import Spell
from Classes.Statistics import Statistics
from colorama import init, Fore

init(autoreset=True)


def load_spells_from_file(file_path: str) -> list[Spell]:
    with open(file_path, "r") as f:
        spell_data = json.load(f)
    return [Spell(**spell) for spell in spell_data]


def assign_all_player_spells(player_type: PlayerType) -> list[Spell]:
    file_path = f"../spells_{player_type.name}.json"
    return load_spells_from_file(file_path)


def assign_all_robot_spells() -> list[Spell]:
    file_paths = [f"../spells_{robot_type}.json" for robot_type in ["mage", "warrior", "dragon"]]
    spells = []
    for file_path in file_paths:
        spells.extend(load_spells_from_file(file_path))
    return spells


def create_player(player_type: PlayerType, second_player: bool = False) -> Player:
    spells = assign_all_player_spells(player_type)
    return Player(_id=1, statistics=Statistics(100, 100, 10, 10, 0, 0), spells=spells, status=0,
                  player_type=player_type,
                  second_player=second_player)


def create_robot() -> Robot:
    spells = assign_all_robot_spells()

    return Robot(_id=1, statistics=Statistics(100, 100, 10, 10, 0, 0), spells=spells, status=0)


# def get_spell(character: Player | Robot, spell_pos: int) -> Spell:
#     return character.spells[spell_pos]


def compute_damage(attack: int, power: int) -> int:
    return math.ceil(attack * (power / 100))


def launch_spell(spell: Spell, target: Player | Robot, caster: Player | Robot) -> dict:
    miss = False
    damage = None
    heal = None
    buff = None
    text = f"{caster.name} used {spell.name}."
    if random.randint(1, 100) > spell.accuracy:
        miss = True
        text += f"\n\n{caster.name} missed!"
    else:
        if spell.types.get("attack"):
            damage = compute_damage(spell.power, caster.statistics.attack)
            text += f"\n\n{target.name} lost {damage} HP!"

        if spell.types.get("heal"):
            heal = compute_damage(spell.power, caster.statistics.attack)
            text += f"\n\n{caster.name} recovered {heal} HP!"

        if spell.types.get("buff"):
            # TODO add buff to caster
            buff = None

    return {'miss': miss, 'damage': damage, 'heal': heal, 'buff': buff, 'text': text}


def manage_xp(winner: Player | Robot):
    if winner is not None:
        print(
            f"{Fore.LIGHTWHITE_EX}{winner.name} {Fore.LIGHTCYAN_EX}gained {Fore.LIGHTWHITE_EX}{10} {Fore.LIGHTCYAN_EX}experience points.\n")
    else:
        print(
            f"{Fore.LIGHTWHITE_EX}Both players {Fore.LIGHTCYAN_EX}gained {Fore.LIGHTWHITE_EX}{5} {Fore.LIGHTCYAN_EX}experience points.\n")


def read_player_input(message: str, choices: list[str]) -> str:
    while True:
        player_input = input(f"{Fore.LIGHTCYAN_EX}{message} {choices}")
        if player_input in choices:
            return player_input
        print(f"{Fore.LIGHTRED_EX}Please enter any of: {choices}")


def assign_player_type(player_type_choice: str) -> PlayerType:
    return {
        'm': PlayerType.MAGE,
        'w': PlayerType.WARRIOR,
        'd': PlayerType.DRAGON
    }[player_type_choice]

