from ex0.creatures import Creature
from ex1.capabilities import HealCapability
from ex1.capabilities import TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__()
        self.name = "Sproutling"
        self.type = "Grass"
        self.attack_type = "Vine Whip"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_type}!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__()
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"
        self.attack_type = "Petal Dance"

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_type}!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__()
        self.name = "Shiftling"
        self.type = "Normal"
        self.attack_type = "Normal"
        self.transformed = False

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        if self.transformed is False:
            self.transformed = True
            return f"{self.name} shifts into a sharper form!"
        else:
            return f"{self.name} is already transformed."

    def revert(self) -> str:
        if self.transformed is True:
            self.transformed = False
            return f"{self.name} returns to normal."
        else:
            return f"{self.name} is already normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__()
        self.name = "Morphagon"
        self.type = "Normal/Dragon"
        self.attack_type = "Normal"
        self.transformed = False

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        if self.transformed is False:
            self.transformed = True
            return f"{self.name} morphs into a dragonic battle form!"
        else:
            return f"{self.name} is already transformed."

    def revert(self) -> str:
        if self.transformed is True:
            self.transformed = False
            return f"{self.name} stabilizes its form."
        else:
            return f"{self.name} is already normal."
