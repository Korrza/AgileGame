import json
import math
import random
import msvcrt as key
from Classes.Character import Player, Robot
from Classes.PlayerType import PlayerType
from Classes.Spell import Spell
from Classes.Statistics import Statistics
from colorama import init, Fore

init(autoreset=True)


def get_all_player_spells(player_type: PlayerType) -> list[Spell]:
    with open(f"spells_{player_type.name}.json", "r") as f:
        spell_data = json.load(f)

    return [Spell(**spell) for spell in spell_data]


def get_all_robot_spells() -> list[Spell]:
    spell_data = []
    with open(f"spells_mage.json", "r") as f:
        mage_spells_data = json.load(f)
        for spell in mage_spells_data:
            spell_data.append(spell)
    with open(f"spells_warrior.json", "r") as f:
        warrior_spells_data = json.load(f)
        for spell in warrior_spells_data:
            spell_data.append(spell)
    with open(f"spells_dragon.json", "r") as f:
        dragon_spells_data = json.load(f)
        for spell in dragon_spells_data:
            spell_data.append(spell)

    return [Spell(**spell) for spell in spell_data]


def create_player(player_type: PlayerType, second_player: bool = False) -> Player:
    spells = get_all_player_spells(player_type)
    return Player(_id=1, statistics=Statistics(100, 100, 10, 10, 0, 0), spells=spells, status=0,
                  player_type=player_type,
                  second_player=second_player)


def create_robot() -> Robot:
    spells = get_all_robot_spells()

    return Robot(_id=1, statistics=Statistics(100, 100, 10, 10, 0, 0), spells=spells, status=0)


def get_spell(character: Player) -> Spell:
    print(f"{Fore.LIGHTBLUE_EX}{character.name}{Fore.LIGHTCYAN_EX}, choose your spell. (a/z/e/r)\n")
    key_pressed = key.getch()

    match key_pressed:
        case b'a':
            return character.spells[0]
        case b'z':
            return character.spells[1]
        case b'e':
            return character.spells[2]
        case b'r':
            return character.spells[3]


def compute_damage(attack: int, power: int) -> int:
    return math.ceil(attack * (power / 100))


def launch_spell(spell: Spell, target: Player | Robot, caster: Player | Robot) -> bool:
    if spell.types.get("attack"):
        damage = compute_damage(spell.power, caster.statistics.attack)
        target.statistics.current_hp -= damage
        print(
            f"{Fore.LIGHTBLUE_EX}{caster.name} {Fore.LIGHTCYAN_EX}used {Fore.LIGHTMAGENTA_EX}{spell.name} {Fore.LIGHTCYAN_EX}on {Fore.LIGHTBLUE_EX}{target.name} {Fore.LIGHTCYAN_EX}and deal {Fore.LIGHTYELLOW_EX}{damage} {Fore.LIGHTCYAN_EX}damage !")

    if spell.types.get("heal"):
        heal = compute_damage(spell.power, caster.statistics.attack)
        caster.statistics.current_hp += heal
        print(
            f"{Fore.LIGHTBLUE_EX}{caster.name} {Fore.LIGHTCYAN_EX}used {Fore.LIGHTMAGENTA_EX}{spell.name} {Fore.LIGHTCYAN_EX}on {Fore.LIGHTBLUE_EX}{target.name} {Fore.LIGHTCYAN_EX}and healed {Fore.LIGHTYELLOW_EX}{heal} {Fore.LIGHTCYAN_EX}points !")

    if spell.types.get("buff"):
        # TODO add buff to caster
        print(
            f"{Fore.LIGHTBLUE_EX}{caster.name} {Fore.LIGHTCYAN_EX}used {Fore.LIGHTMAGENTA_EX}{spell.name} {Fore.LIGHTCYAN_EX}on {Fore.LIGHTBLUE_EX}{target.name} {Fore.LIGHTCYAN_EX}!")

    if random.randint(1, 100) > spell.accuracy:
        print(f"{Fore.LIGHTRED_EX}The spell missed !\n")
        return False

    return True


def manage_xp(winner: Player | Robot):
    if winner is not None:
        print(
            f"{Fore.LIGHTWHITE_EX}{winner.name} {Fore.LIGHTCYAN_EX}gained {Fore.LIGHTWHITE_EX}{10} {Fore.LIGHTCYAN_EX}experience points.\n")
    else:
        print(
            f"{Fore.LIGHTWHITE_EX}Both players {Fore.LIGHTCYAN_EX}gained {Fore.LIGHTWHITE_EX}{5} {Fore.LIGHTCYAN_EX}experience points.\n")


def read_player_type_choice() -> str:
    while True:
        player_type_choice = input(f"{Fore.LIGHTCYAN_EX}Choose a character. (m/w/d): ")
        if player_type_choice in {'m', 'w', 'd'}:
            return player_type_choice
        print(f"{Fore.LIGHTRED_EX}Please enter 'm', 'w' or 'd'")


def assign_player_type(player_type_choice: str) -> PlayerType:
    return {
        'm': PlayerType.MAGE,
        'w': PlayerType.WARRIOR,
        'd': PlayerType.DRAGON
    }[player_type_choice]

