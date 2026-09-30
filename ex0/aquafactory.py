from ex0.creature_factory import CreatureFactory
import ex0.creatures


class AquaFactory(CreatureFactory):
    def create_base(self) -> ex0.creatures.Creature:
        an_aquabub = ex0.creatures.Aquabub()
        return an_aquabub

    def create_evolved(self) -> ex0.creatures.Creature:
        a_torragon = ex0.creatures.Torragon()
        return a_torragon
