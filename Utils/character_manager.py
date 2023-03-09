import json
import math
import random
import msvcrt as key
from Classes.Character import Player, Robot
from Classes.Spell import Spell
from Classes.Statistics import Statistics


def get_all_spells() -> list[Spell]:
    with open("../spells.json", "r") as f:
        spell_data = json.load(f)

    return [Spell(**spell) for spell in spell_data]


def create_player(second_player: bool = False) -> Player:
    spells = get_all_spells()

    return Player(1, Statistics(100, 100, 10, 10, 0, 0), spells, 0,
                  second_player=second_player)


def create_robot() -> Robot:
    spells = get_all_spells()

    return Robot(1, Statistics(100, 100, 10, 10, 0, 0), spells, 0)


def get_spell(character: Player | Robot) -> Spell:
    key_pressed = b'a'

    match key_pressed:
        case b'a':
            return character.spells[0]
        case b'z':
            return character.spells[1]
        case b'e':
            return character.spells[2]
        case b'r':
            return character.spells[3]


def get_spell_test(character: Player | Robot, spell_pos: int) -> Spell:
    return character.spells[spell_pos]


def compute_damage(attack: int, power: int) -> int:
    return math.ceil(attack * (power / 100))


def launch_spell(spell: Spell, target: Player | Robot, caster: Player | Robot):
    miss = False
    damage = None
    heal = None
    buff = None
    if random.randint(1, 100) > spell.accuracy:
        print("The spell missed !")
        return True, None, None, None

    if spell.types.get("attack"):
        damage = compute_damage(spell.power, caster.statistics.attack)
        print(caster.name + " used " + spell.name + " on " + target.name + " and deal " + str(damage) + " damage!")

    if spell.types.get("heal"):
        heal = compute_damage(spell.power, caster.statistics.attack)
        # caster.statistics.current_hp += heal
        print(caster.name + " used " + spell.name + " on " + caster.name + " and healed for " + str(heal) + " points!")

    if spell.types.get("buff"):
        # TODO add buff to caster
        print(caster.name + " used " + spell.name + " on " + caster.name + " !")

    return miss, damage, heal, buff


def manage_xp(winner: Player | Robot):
    if winner is not None:
        print(str(winner.name) + " gained " + str(10) + " experience points \n")
    else:
        print("Both players gained " + str(5) + " experience points \n")