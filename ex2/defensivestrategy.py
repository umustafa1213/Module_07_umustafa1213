from ex2.battlestrategy import BattleStrategy
from ex0.creatures import Creature
from ex1.capabilities import HealCapability
import typing


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            healer = typing.cast(HealCapability, creature)
            print(creature.attack())
            print(healer.heal())
        else:
            raise ValueError(f"Invalid Creature '{creature.name}'"
                             " for this defensive strategy")
