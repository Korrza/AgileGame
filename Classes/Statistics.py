class Statistics:
    def __init__(self, max_hp: int, current_hp: int, attack: int, power: int, level:int, xp: int):
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attack = attack
        self.power = power
        self.level = level
        self.xp = xp

    def earn_xp(self, xp_input):
        self.xp += xp_input
        return self.xp
