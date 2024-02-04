import Optimizer
import DataReader
import re


def initData():
    class_name = "Hero"
    #weapon_name = "Scavenger's Curved Sword"
    weapon_name = "Great Stars"
    # weapon_name = "Erdsteel Dagger"
    #affinity = "Heavy"
    affinity = "Blood"
    #affinity = "Cold"
    affinity = "Occult"
    is_2handing = False
    use_custom_min_stats = True

    soul_level = 200
    vigor = 60
    mind = 30
    endurance = 60
    strength = 80
    dexterity = 9
    intelligence = 11
    faith = 12
    arcane = 17

    custom_min_stats = [14, 9, 12, 16, 9, 11, 12, 11]
    current_stats = [200, 60, 30, 60, 22, 12, 11, 12, 72]




    a = (200 - (60-14 + 30-9 + 60-12 + 11-7 + 12-8 + 7))


    max_upgrade_level = DataReader.getWeaponMaxUpgradeLevel(weapon_name)
    weapon_upgrade_level = max_upgrade_level

    if max_upgrade_level == 10:
        affinity = "None"

    weapon_full_name = DataReader.getFullWeaponName(weapon_name, affinity)

    starting_class = DataReader.initStartingClass(class_name)

    b = (200 - (60-14 + 30-9 + 60-12 + 80-16 + 9-9 + 11-7 + 12-8 + 17-11 + 7)) + 80-16 + 9-9 + 17-11
    bmin = (200 - (60-14 + 30-9 + 60-12 + 80-16 + 9-9 + 11-11 + 12-12 + 17-11 + 7)) + 80-16 + 9-9 + 17-11

    #points = soul_level - ((vigor - starting_class.getMinVigor()) + (mind - starting_class.getMinMind()) + (endurance - starting_class.getMinEndurance()) + (strength - starting_class.getMinStr()) + (dexterity - starting_class.getMinDex()) + (intelligence - starting_class.getMinInt()) + (faith - starting_class.getMinFai()) + (arcane - starting_class.getMinArc()) + starting_class.getMinSoul_level())

    #starting_class = DataReader.initStartingClass(class_name)

    weapon_extra_data = DataReader.initWeaponExtraData(weapon_full_name, weapon_upgrade_level, is_2handing)
    weapon_passive = DataReader.initWeaponPassive(weapon_full_name, weapon_upgrade_level)
    weapon_attack = DataReader.initWeaponAttack(weapon_full_name, weapon_upgrade_level)
    weapon_scaling = DataReader.initWeaponScaling(weapon_full_name, weapon_upgrade_level)
    weapon_correct_id = DataReader.initWeaponCorrectId(weapon_full_name)
    weapon_element_correct = DataReader.initWeaponElementCorrect(weapon_correct_id)

    optimizer = Optimizer.Optimizer(starting_class, weapon_extra_data, weapon_passive,
                                    weapon_attack, weapon_scaling,
                                    weapon_correct_id, weapon_element_correct,
                                    use_custom_min_stats, custom_min_stats, current_stats)


    return optimizer


def main():

    optimizer = initData()
    value_list = optimizer.optimize()

    # TODO: input all stats (custom min values) and calc allocated points

    # for combination in value_list:
    #     print(f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
    #           f"P1: {combination.getPassive1Type()} {combination.getPassive1Value()} | "
    #           f"P2: {combination.getPassive2Type()}: {combination.getPassive2Value()} | "
    #           f"Dmg + passives: {combination.getTotalSum()}")


    # TODO: Sort by damage + passives
    sorted_list = sorted(value_list, key=lambda x: x.getTotalSum())
    #sorted_list = sorted_list[-20:]
    for combination in sorted_list:
        print(f"Stats: {combination.getStats()} Rest ({combination.getRestStats()}) | "
              f"Dmg: {combination.getTotalDmg()} | "
              f"P1: {combination.getPassive1Type()}: {combination.getPassive1Value()} | "
              f"P2: {combination.getPassive2Type()}: {combination.getPassive2Value()} | "
              f"Dmg + passives: {combination.getTotalSum()}")


    # TODO: Sort by damage
    # sorted_list = sorted(value_list, key=lambda x: x.getTotalDmg())
    # sorted_list = sorted_list[-50:]
    # for combination in sorted_list:
    #     print(f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
    #           f"P1: {combination.getPassive1Type()}: {combination.getPassive1Value()} | "
    #           f"P2: {combination.getPassive2Type()}: {combination.getPassive2Value()} | "
    #           f"Dmg + passives: {combination.getTotalSum()}")


    # TODO: Sort by passives
    # sorted_list = sorted(value_list, key=lambda x: x.getPassive1Value() + x.getPassive2Value())
    # for combination in sorted_list:
    #     print(
    #         f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
    #         f"P1: {combination.getPassive1Type()}: {combination.getPassive1Value()} | "
    #         f"P2: {combination.getPassive2Type()}: {combination.getPassive2Value()} | "
    #         f"Dmg + passives: {combination.getTotalSum()}")


    print("")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("")

    # TODO: Best Passives where where min reqs met
    # def sorting_key(combination):
    #     return (combination.getPassive1Value() + combination.getPassive2Value(),
    #             combination.getTotalDmg())
    #
    # highest_combination = max(value_list, key=sorting_key)
    #
    #
    #
    # print(
    #     f"Stats: {highest_combination.getStats()} | "
    #     f"Dmg: {highest_combination.getTotalDmg()} | "
    #     f"P1: {highest_combination.getPassive1Type()}: {highest_combination.getPassive1Value()} | "
    #     f"P2: {highest_combination.getPassive2Type()}: {highest_combination.getPassive2Value()} | "
    #     f"Dmg + passives: {highest_combination.getTotalSum()}")



    # print("")
    # print("------------------------------------------------------------------------------------------------------------------------------")
    # print("")

    print(f"COMBINATIONS: {len(value_list)}")

    print(f"Starting class: {optimizer.starting_class.getName()}")
    print(f"Weapon name: {optimizer.weapon_extra_data.getName()}")
    print(f"weapon_type: {optimizer.weapon_extra_data.getWeaponType()}")
    print(f"weapon max_upgrades: {optimizer.weapon_extra_data.getUpgradeLevel()}")
    print(f"upgrade_level: {optimizer.weapon_extra_data.getUpgradeLevel()}")
    print(f"2h bonus?: {optimizer.weapon_extra_data.getTwoHandBonus()}")
    print(f"required_str: {optimizer.weapon_extra_data.getRequiredStr()}")
    print(f"passive1: {optimizer.weapon_passive.getPassiveType1()}")
    print(f"passive2: {optimizer.weapon_passive.getPassiveType2()}")
    print(f"Base Phys att: {optimizer.weapon_attack.getPhysAttack()}")

    print(f"Usable points: {200 - (60 - 14 + 30 - 9 + 60 - 12 + 11 - 7 + 12 - 8 + 7)}")


if __name__ == "__main__":
    main()
