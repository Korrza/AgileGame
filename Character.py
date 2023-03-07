import Statistics


class Character:
    def __init__(self, _id: int, name: str, statistics: Statistics):
        self._id = _id
        self.name = name
        self.statistics = statistics

    def basic_attack(self):
        return self.statistics.attacks.basic_attack

    def basic_healing(self):
        return self.statistics.healing.basic_healing

    def receive_damage(self, damage_input):
        self.statistics.health_points -= damage_input
        if self.statistics.health_points < 0:
            self.statistics.health_points = 0
        return self.statistics.health_points

class Player(Character):
    def __init__(self, _id: int, statistics: Statistics, name: str = None, second_player: bool = False):
        name = name if name is not None else 'Player 2' if second_player else 'Player 1'
        super().__init__(_id, name, statistics)


class Robot(Character):
    def __init__(self, _id: int, statistics: Statistics, name: str = 'Robot'):
        super().__init__(_id, name, statistics)
