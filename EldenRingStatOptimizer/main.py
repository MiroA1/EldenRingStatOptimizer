import Optimizer
import DataReader


def initData():
    class_name = "Hero"
    weapon_name = "Great Stars"
    # weapon_name = "Erdsteel Dagger"
    #affinity = "Heavy"
    affinity = "Blood"
    #affinity = "Cold"
    is_2handing = False

    max_upgrade_level = DataReader.getWeaponMaxUpgradeLevel(weapon_name)
    weapon_upgrade_level = 25

    if affinity != "":
        weapon = affinity + " " + weapon_name
    else:
        weapon = weapon_name

    starting_class = DataReader.initStartingClass(class_name)
    weapon_extra_data = DataReader.initWeaponExtraData(weapon, weapon_upgrade_level,
                                                       is_2handing)
    weapon_passive = DataReader.initWeaponPassive(weapon, weapon_upgrade_level)
    weapon_attack = DataReader.initWeaponAttack(weapon, weapon_upgrade_level)
    weapon_scaling = DataReader.initWeaponScaling(weapon, weapon_upgrade_level)
    weapon_correct_id = DataReader.initWeaponCorrectId(weapon)
    weapon_element_correct = DataReader.initWeaponElementCorrect(weapon_correct_id)

    optimizer = Optimizer.Optimizer(starting_class, weapon_extra_data, weapon_passive,
                                    weapon_attack,
                                    weapon_scaling, weapon_correct_id,
                                    weapon_element_correct)

    print(f"Starting class: {starting_class.getName()}")
    print(f"min Vigor: {starting_class.getMinVigor()}")
    print(f"min Strength: {starting_class.getMinStr()}")
    print(f"min Soul Level: {starting_class.getMinSoul_level()}")
    print(f"Weapon name: {weapon_extra_data.getName()}")
    print(f"weapon max_upgrades: {max_upgrade_level}")
    print(f"upgrade_level: {weapon_extra_data.getUpgradeLevel()}")
    print(f"2h bonus?: {weapon_extra_data.getTwoHandBonus()}")
    print(f"required_str: {weapon_extra_data.getRequiredStr()}")
    print(f"weapon_type: {weapon_extra_data.getWeaponType()}")
    print(f"passive1: {weapon_passive.getPassiveType1()}")
    print(f"passive2: {weapon_passive.getPassiveType2()}")
    print(f"blood value: {weapon_passive.getBloodBase1()}")
    print(f"Phys att: {weapon_attack.getPhysAttack()}")
    print(f"str scaling: {weapon_scaling.getStrScaling()}")
    print(f"weapon id: {weapon_correct_id.getAttackElementId()}")

    return optimizer


def main():
    optimizer = initData()
    value_map = optimizer.optimize()
    value_list = optimizer.optimize()

    combination_counter = 0
    #TODO: 2h hand and input all stats

    # for key, value in value_map.items():
    #     combination_counter += 1
    #     print(f"{key}  |  {value}")
    #print(value_list)

    # TODO: Sort by damage + passives
    sorted_list = sorted(value_list, key=lambda x: x.getTotalSum())
    for combination in sorted_list:
        print(f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | "
              f"P1: {combination.getPassive1()} {combination.getPassive1Value()} | "
              f"P2: {combination.getPassive1()}: {combination.getPassive2Value()} | "
              f"Dmg + passives: {combination.getTotalSum()}")
        combination_counter += 1


    # # TODO: Sort by damage
    # sorted_list = sorted(value_list, key=lambda x: x.getTotalDmg())
    # for combination in sorted_list:
    #     print(
    #         f"Stats: {combination.getStats()} | Dmg: {combination.getTotalDmg()} | Passive 1: {combination.getPassive1Value()} | Passive 2: {combination.getPassive2Value()}| Total Sum: {combination.getTotalSum()}")
    #     combination_counter += 1




    # TODO: Find best combined, best total dmg, first high passive, stats divided by 10 (soft caps)
    print(f"COMBINATIONS: {combination_counter}")


if __name__ == "__main__":
    main()
