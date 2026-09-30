import abc
from ex0.creatures import Creature


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        ...
