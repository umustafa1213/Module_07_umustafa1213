import abc
from ex0.creatures import Creature


class CreatureFactory(abc.ABC):
    def __init__(self):
        self.name = "None"
        self.type = "None"

    @abc.abstractmethod
    def create_base(self) -> Creature:
        ...

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"
