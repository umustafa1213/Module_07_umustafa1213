import ex1


def main() -> None:
    my_healingcreaturefactory = ex1.HealingCreatureFactory()
    my_sproutling = my_healingcreaturefactory.create_base()
    my_bloomelle = my_healingcreaturefactory.create_evolved()
    print("Testing Creature with healing capability")
    print("base:")
    print(my_sproutling.describe())
    print(my_sproutling.attack())
    print(my_sproutling.heal())
    print("evolved:")
    print(my_bloomelle.describe())
    print(my_bloomelle.attack())
    print(my_bloomelle.heal())
    print()
    my_transformfactory = ex1.TransformCreatureFactory()
    my_shiftling = my_transformfactory.create_base()
    my_morphagon = my_transformfactory.create_evolved()
    print("Testing Creature with transform capability")
    print("base:")
    print(my_shiftling.describe())
    print(my_shiftling.attack())
    print(my_shiftling.transform())
    print(my_shiftling.attack())
    print(my_shiftling.revert())
    print("evolved:")
    print(my_morphagon.describe())
    print(my_morphagon.attack())
    print(my_morphagon.transform())
    print(my_morphagon.attack())
    print(my_morphagon.revert())


if __name__ == "__main__":
    main()
