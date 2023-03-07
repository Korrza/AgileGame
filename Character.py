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
    def __init__(self, _id: int, statistics: Statistics, name: str = None, second_player: bool = False):
        if name is None:
            if second_player:
                name = 'Player 2'
            else:
                name = 'Player 1'
        super().__init__(_id, name, statistics)


class Robot(Character):
    def __init__(self, _id: int, statistics: Statistics, name: str = 'Robot'):
        super().__init__(_id, name, statistics)
