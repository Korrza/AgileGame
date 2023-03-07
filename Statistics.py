from Actions import Attacks, Healing
class Statistics:
    def __init__(self, max_hp: int, current_hp: int, attacks: Attacks, healing: Healing, xp: int):
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attacks = attacks
        self.healing = healing
        self.xp = xp

    def earn_xp(self, xp_input):
        self.xp += xp_input
        return self.xp
