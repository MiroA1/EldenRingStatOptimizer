import Optimizer
import DataReader


def initData():
    class_name = "Hero"
    weapon_name = "Great Stars"
    # weapon_name = "Erdsteel Dagger"
    affinity = "Heavy"
    #affinity = "Blood"
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

    combination_counter = 0

    for key, value in value_map.items():
        combination_counter += 1
        print(f"{key}  |  {value}")

    # TODO:  Sort by damage
    # sorted_values = dict(sorted(value_map.items(), key=lambda item: item[1]))
    # for key, value in sorted_values.items():
    #     combination_counter += 1
    #     print(f"{key}  |  {value}")

    # sorted_value_map = dict(sorted(value_map.items(), key=lambda item: float(item[1].split(":")[1].split()[0]), reverse=True))
    # for key, value in sorted_value_map.items():
    #     combination_counter += 1
    #     print(f"{key}: {value}")

    # TODO: Sort by damage + passive
    # sorted_values = dict(sorted(value_map.items(), key=lambda item: (str(item[1]), item[1])))
    # for key, value in sorted_values.items():
    #     combination_counter += 1
    #     print(f"{key}  |  {value}")

    # TODO: Find best combined, best total dmg, first high passive, stats divided by 10 (soft caps)
    print(f"COMBINATIONS: {combination_counter}")


if __name__ == "__main__":
    main()
