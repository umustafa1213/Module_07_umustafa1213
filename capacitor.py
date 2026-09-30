import ex1


def main() -> None:
    my_healingcreaturefactory = ex1.HealingCreatureFactory()
    my_sproutling = my_healingcreaturefactory.create_base()
    my_bloomelle = my_healingcreaturefactory.create_evolved()
    print("Testing Creature with healing capability")
    print("base:")
    print(my_sproutling.describe())
    print(my_sproutling.attack())
    print(my_sproutling.heal(my_sproutling))
    print("evolved:")
    print(my_bloomelle.describe())
    print(my_bloomelle.attack())
    print(my_bloomelle.heal(my_bloomelle))
    print()
    my_transformfactory = ex1.TransformCreatureFactory()
    my_shiftling = my_transformfactory.create_base()
    my_morphafon = my_transformfactory.create_evolved()
    print("Testing Creature with transform capability")
    print("base:")
    print(my_shiftling.describe())
    print(my_shiftling.attack())
    print(my_shiftling.transform())
    print(my_shiftling.attack())
    print(my_shiftling.revert())
    print("evolved:")
    print(my_morphafon.describe())
    print(my_morphafon.attack())
    print(my_morphafon.transform())
    print(my_morphafon.attack())
    print(my_morphafon.revert())


if __name__ == "__main__":
    main()
