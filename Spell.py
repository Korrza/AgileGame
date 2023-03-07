class Spell:
    def __init__(self, name: str, magic: bool, power: int, accuracy: float, description: str, types: dict, cooldown: int = None, status: dict = None):
        self.name = name
        self.magic = magic
        self.power = power
        self.accuracy = accuracy
        self.cooldown = cooldown
        self.description = description
        self.types = types
        self.status = status
