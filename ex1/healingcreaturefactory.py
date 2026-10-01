from ex0.creature_factory import CreatureFactory
from ex1.creatures import Sproutling, Bloomelle
from ex0.creatures import Creature


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        a_sproutling = Sproutling()
        return a_sproutling

    def create_evolved(self) -> Creature:
        a_bloomelle = Bloomelle()
        return a_bloomelle
