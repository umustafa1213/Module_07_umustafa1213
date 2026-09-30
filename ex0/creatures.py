import abc


class Creature(abc.ABC):
    def __init__(self):
        self.name: str = "basic_creature"
        self.type: str = "basic_type"

    @abc.abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"
        self.attack_type = "Ember"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_type}!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Flying"
        self.attack_type = "Flamethrower"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_type}!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__()
        self.name = "Aquabub"
        self.type = "Water"
        self.attack_type = "Water Gun"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_type}!"


class Torragon(Creature):
    def __init__(self):
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"
        self.attack_type = "Hydro Pump"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_type}!"
