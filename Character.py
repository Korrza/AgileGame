import Statistics
import Actions


class Character:
    def __init__(self, _id: int, name: str, statistics: Statistics, actions: Actions):
        self._id = _id
        self.name = name
        self.statistics = statistics
        self.actions = actions

    def get_basic_attack_damage(self):
        return self.statistics.attack * self.actions.basic_attack

    def get_physical_attack_damage(self):
        return self.statistics.attack * self.actions.physical_attack

    def get_magical_attack_damage(self):
        return self.statistics.attack * self.actions.magical_action

    def get_healing(self):
        return self.statistics.power * self.actions.magical_action


class Player(Character):
    def __init__(self, _id: int, statistics: Statistics, name: str = None, second_player: bool = False):
        name = name if name is not None else 'Player 2' if second_player else 'Player 1'
        super().__init__(_id, name, statistics)


class Robot(Character):
    def __init__(self, _id: int, statistics: Statistics, name: str = 'Robot'):
        super().__init__(_id, name, statistics)
