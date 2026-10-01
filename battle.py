from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    if isinstance(factory, CreatureFactory):
        my_basecreature = factory.create_base()
        my_evolvedcreature = factory.create_evolved()
        print("Testing factory")
        print(my_basecreature.describe())
        print(my_basecreature.attack())
        print(my_evolvedcreature.describe())
        print(my_evolvedcreature.attack())
    else:
        raise TypeError("No factory object provided")
    return


def base_battle(factory_1: CreatureFactory,
                factory_2: CreatureFactory) -> None:
    if (isinstance(factory_1, CreatureFactory)
       and isinstance(factory_2, CreatureFactory)):
        my_basecreature1 = factory_1.create_base()
        my_basecreature2 = factory_2.create_base()
        print("Testing battle")
        print(my_basecreature1.describe())
        print("vs.")
        print(my_basecreature2.describe())
        print("fight!")
        print(my_basecreature1.attack())
        print(my_basecreature2.attack())
    else:
        raise TypeError("Need to provide two valid factory objects")
    return


def main() -> None:
    my_flamefactory = FlameFactory()
    my_aquafactory = AquaFactory()
    try:
        test_factory(my_flamefactory)
        print()
        test_factory(my_aquafactory)
        print()
        base_battle(my_flamefactory, my_aquafactory)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
