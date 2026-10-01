from ex0.creature_factory import CreatureFactory
from ex0.creatures import Creature, Flameling, Pyrodon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        a_flameling = Flameling()
        return a_flameling

    def create_evolved(self) -> Creature:
        a_pyrodon = Pyrodon()
        return a_pyrodon
