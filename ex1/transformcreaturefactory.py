from ex0.creature_factory import CreatureFactory
from ex1.creatures import Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        a_shiftling = Shiftling()
        return a_shiftling

    def create_evolved(self) -> Morphagon:
        a_morphagon = Morphagon()
        return a_morphagon
