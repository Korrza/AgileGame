from Actions import Attacks, Healing
class Statistics:
    def __init__(self, max_hp: int, current_hp: int, attacks: Attacks, experience: int):
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attacks = attacks
        self.experience = experience
