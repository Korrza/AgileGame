import Statistics


class Character:
    def __init__(self, _id: int, name: str, statistics: Statistics):
        self._id = _id
        self.name = name
        self.statistics = statistics

class Player(Character):
    pass

class Robot(Character):
    pass
