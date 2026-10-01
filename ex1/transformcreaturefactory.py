from ex0.creature_factory import CreatureFactory
from ex1.creatures import Shiftling, Morphagon
from ex0.creatures import Creature


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        a_shiftling = Shiftling()
        return a_shiftling

    def create_evolved(self) -> Creature:
        a_morphagon = Morphagon()
        return a_morphagon
