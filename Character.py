import Statistics


class Character:
    def __init__(self, _id: int, name: str, statistics: Statistics):
        self._id = _id
        self.name = name
        self.statistics = statistics

    def basic_attack(self):
        return self.statistics.attacks.basic_attack

    def receive_damage(self, damage_input):
        self.statistics.health_points -= damage_input
        if self.statistics.health_points < 0:
            self.statistics.health_points = 0
        return self.statistics.health_points

class Player(Character):
    pass

class Robot(Character):
    pass
