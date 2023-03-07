import Statistics
import Spell


class Character:
    def __init__(self, _id: int, name: str, statistics: Statistics, spells: list[Spell], status: int):
        self._id = _id
        self.name = name
        self.statistics = statistics
        self.spells = spells
        self.status = status


class Player(Character):
    def __init__(self, _id: int, statistics: Statistics, name: str = None, second_player: bool = False):
        name = name if name is not None else 'Player 2' if second_player else 'Player 1'
        super().__init__(_id, name, statistics)


class Robot(Character):
    def __init__(self, _id: int, statistics: Statistics, name: str = 'Robot'):
        super().__init__(_id, name, statistics)
