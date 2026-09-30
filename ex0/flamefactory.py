from ex0.creature_factory import CreatureFactory
import ex0.creatures


class FlameFactory(CreatureFactory):
    def create_base(self) -> ex0.creatures.Creature:
        a_flameling = ex0.creatures.Flameling()
        return a_flameling

    def create_evolved(self) -> ex0.creatures.Creature:
        a_pyrodon = ex0.creatures.Pyrodon()
        return a_pyrodon
