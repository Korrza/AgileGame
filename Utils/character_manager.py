import json
import math
import random
import msvcrt as key
from Classes.Character import Player, Robot
from Classes.Spell import Spell
from Classes.Statistics import Statistics
from colorama import init, Fore

init(autoreset=True)


def get_all_spells() -> list[Spell]:
    with open("spells.json", "r") as f:
        spell_data = json.load(f)

    return [Spell(**spell) for spell in spell_data]


def create_player(second_player: bool = False) -> Player:
    spells = get_all_spells()

    return Player(1, Statistics(100, 100, 10, 10, 0, 0), spells, 0,
                  second_player=second_player)


def create_robot() -> Robot:
    spells = get_all_spells()

    return Robot(1, Statistics(100, 100, 10, 10, 0, 0), spells, 0)


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
        print(f"{Fore.LIGHTWHITE_EX}{winner.name} {Fore.LIGHTCYAN_EX}gained {Fore.LIGHTWHITE_EX}{10} {Fore.LIGHTCYAN_EX}experience points.\n")
    else:
        print(f"{Fore.LIGHTWHITE_EX}Both players {Fore.LIGHTCYAN_EX}gained {Fore.LIGHTWHITE_EX}{5} {Fore.LIGHTCYAN_EX}experience points.\n")
