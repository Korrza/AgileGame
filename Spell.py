class Spell:
    def __init__(self, name: str, magic: bool, power: int, precision: float, description: str, _type: dict, cooldown: int = None, status: dict = None):
        self.name = name
        self.magic = magic
        self.power = power
        self.precision = precision
        self.cooldown = cooldown
        self.description = description
        self._type = _type
        self.status = status
