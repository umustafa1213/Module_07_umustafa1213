from ex2.battlestrategy import BattleStrategy
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability
import typing


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            transformer = typing.cast(TransformCapability, creature)
            print(transformer.transform())
            print(creature.attack())
            print(transformer.revert())
        else:
            raise ValueError(f"Invalid Creature '{creature.name}'"
                             " for this aggressive strategy")
