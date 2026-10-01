from ex0.creature_factory import CreatureFactory
from ex1.creatures import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        a_sproutling = Sproutling()
        return a_sproutling

    def create_evolved(self) -> Bloomelle:
        a_bloomelle = Bloomelle()
        return a_bloomelle
