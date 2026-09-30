from ex2.battlestrategy import BattleStrategy
from ex0.creatures import Creature


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        print(creature.attack())
