import Optimizer
import DataReader


def initData():
    class_name = "Hero"
    weapon_name = "Greatsword"
    weapon_name = "Ordovis's Greatsword"
    # weapon_name = "Erdsteel Dagger"
    #affinity = "Heavy"
    affinity = "Blood"
    #affinity = "Cold"
    is_2handing = False


    max_upgrade_level = DataReader.getWeaponMaxUpgradeLevel(weapon_name)
    weapon_upgrade_level = max_upgrade_level

    if max_upgrade_level == 10:
         affinity = "None"

    weapon_full_name = DataReader.getFullWeaponName(weapon_name, affinity)



    starting_class = DataReader.initStartingClass(class_name)
    weapon_extra_data = DataReader.initWeaponExtraData(weapon_full_name, weapon_upgrade_level,
                                                       is_2handing)
    weapon_passive = DataReader.initWeaponPassive(weapon_full_name, weapon_upgrade_level)
    weapon_attack = DataReader.initWeaponAttack(weapon_full_name, weapon_upgrade_level)
    weapon_scaling = DataReader.initWeaponScaling(weapon_full_name, weapon_upgrade_level)
    weapon_correct_id = DataReader.initWeaponCorrectId(weapon_full_name)
    weapon_element_correct = DataReader.initWeaponElementCorrect(weapon_correct_id)

    optimizer = Optimizer.Optimizer(starting_class, weapon_extra_data, weapon_passive,
                                    weapon_attack,
                                    weapon_scaling, weapon_correct_id,
                                    weapon_element_correct)


    return optimizer


def main():

    optimizer = initData()
    value_list = optimizer.optimize()

    #TODO: input all stats (custom min values)

    # for combination in value_list:
    #     print(f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
    #           f"P1: {combination.getPassive1Type()} {combination.getPassive1Value()} | "
    #           f"P2: {combination.getPassive2Type()}: {combination.getPassive2Value()} | "
    #           f"Dmg + passives: {combination.getTotalSum()}")


    # TODO: Sort by damage + passives
    sorted_list = sorted(value_list, key=lambda x: x.getTotalSum())
    #sorted_list = sorted_list[-20:]
    for combination in sorted_list:
        print(f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
              f"P1: {combination.getPassive1Type()} {combination.getPassive1Value()} | "
              f"P2: {combination.getPassive2Type()}: {combination.getPassive2Value()} | "
              f"Dmg + passives: {combination.getTotalSum()}")


    # TODO: Sort by damage
    # sorted_list = sorted(value_list, key=lambda x: x.getTotalDmg())
    # sorted_list = sorted_list[-20:]
    # for combination in sorted_list:
    #     print(f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
    #           f"P1: {combination.getPassive1()}: {combination.getPassive1Value()} | "
    #           f"P2: {combination.getPassive2()}: {combination.getPassive2Value()} | "
    #           f"Dmg + passives: {combination.getTotalSum()}")


    # TODO: Sort by passives
    # sorted_list = sorted(value_list, key=lambda x: x.getPassive1Value() + x.getPassive2Value())
    #  sorted_list = sorted_list[-20:]
    # for combination in sorted_list:
    #     print(
    #         f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
    #         f"P1: {combination.getPassive1()}: {combination.getPassive1Value()} | "
    #         f"P2: {combination.getPassive2()}: {combination.getPassive2Value()} | "
    #         f"Dmg + passives: {combination.getTotalSum()}")

    # TODO: Best Passives where total = highest
    print("")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("")

    # def sorting_key(combination):
    #     return (combination.getPassive1Value() + combination.getPassive2Value(),
    #             combination.getTotalDmg())
    #
    # highest_combination = max(value_list, key=sorting_key)
    # print(
    #     f"Stats: {highest_combination.getStats()} | "
    #     f"Dmg: {highest_combination.getTotalDmg()} | "
    #     f"P1: {highest_combination.getPassive1()}: {highest_combination.getPassive1Value()} | "
    #     f"P2: {highest_combination.getPassive2()}: {highest_combination.getPassive2Value()} | "
    #     f"Dmg + passives: {highest_combination.getTotalSum()}"
    #


    print("")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("")

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

    print(200 - (60 - 14 + 30 - 9 + 60 - 12 + 11-7 + 12-8 + 7))


if __name__ == "__main__":
    main()
