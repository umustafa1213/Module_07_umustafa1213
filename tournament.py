import ex0
import ex1
import ex2


def battle(opponent_list: list[tuple[ex0.CreatureFactory,
           ex2.BattleStrategy]]) -> None:
    num_of_opponents = len(opponent_list)
    print("*** Tournament ***")
    print(f"{num_of_opponents} opponents involved")
    for i in range(0, num_of_opponents):
        for j in range(i + 1, num_of_opponents):
            creature_a = opponent_list[i][0].create_base()
            creature_b = opponent_list[j][0].create_base()
            print()
            print("* Battle *")
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")
            try:
                opponent_list[i][1].act(creature_a)
                opponent_list[j][1].act(creature_b)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                print()
                return


def main() -> None:
    flamefactory = ex0.FlameFactory()
    aquafactory = ex0.AquaFactory()
    healingfactory = ex1.HealingCreatureFactory()
    transformfactory = ex1.TransformCreatureFactory()
    normalstrategy = ex2.NormalStrategy()
    aggressivestrategy = ex2.AggressiveStrategy()
    defensivestrategy = ex2.DefensiveStrategy()
    first_list = [(flamefactory, normalstrategy),
                  (healingfactory, defensivestrategy)]
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(first_list)
    second_list = [(flamefactory, aggressivestrategy),
                   (healingfactory, defensivestrategy)]
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(second_list)
    third_list = [(aquafactory, normalstrategy),
                  (healingfactory, defensivestrategy),
                  (transformfactory, aggressivestrategy)]
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(third_list)


if __name__ == "__main__":
    main()
