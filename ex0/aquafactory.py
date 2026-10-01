from ex0.creature_factory import CreatureFactory
from ex0.creatures import Creature, Aquabub, Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        an_aquabub = Aquabub()
        return an_aquabub

    def create_evolved(self) -> Creature:
        a_torragon = Torragon()
        return a_torragon
