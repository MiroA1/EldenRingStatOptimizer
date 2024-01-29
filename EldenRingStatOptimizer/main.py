from StartingClass import StartingClass
import Calculator
import DataReader

TOTAL_SKILL_POINTS = 70

# def calcBloodloss(current_arc):
#
#     passive_arc = calcPassiveArc(current_arc)
#
#     bloodloss = (ARC_SCALING * (passive_arc * BLOOD_BASE)) + BLOOD_BASE
#
#     bloodloss_floored = int(bloodloss)
#
#     return bloodloss

def calcPassiveArc(current_arc):

    if current_arc > 60:
        return (90 + 10 * ((current_arc - 60) / 39)) / 100
    elif current_arc > 45:
        return (75 + 15 * ((current_arc - 45) / 15)) / 100
    elif current_arc > 25:
        return (10 + 65 * ((current_arc - 25) / 20)) / 100
    else:
        return (10 * ((current_arc - 1) / 24)) / 100


# def optimize(calculator):
#
#     return calculator.tryPoints()




def initData():

    class_name = "Hero"
    weapon_name = "Great Stars"
    affinity = "Heavy"
    is_2handing = False

    max_upgrade_level = DataReader.getWeaponMaxUpgradeLevel(weapon_name)
    weapon_upgrade_level = 25

    if affinity != "":
        weapon = affinity + " " + weapon_name
    else:
        weapon = weapon_name


    starting_class = DataReader.initStartingClass(class_name)
    weapon_extra_data = DataReader.initWeaponExtraData(weapon, weapon_upgrade_level, is_2handing)
    weapon_passive = DataReader.initWeaponPassive(weapon, weapon_upgrade_level)
    weapon_attack = DataReader.initWeaponAttack(weapon, weapon_upgrade_level)
    weapon_scaling = DataReader.initWeaponScaling(weapon, weapon_upgrade_level)
    weapon_correct_id = DataReader.initWeaponCorrectId(weapon)
    weapon_element_correct = DataReader.initWeaponElementCorrect(weapon_correct_id)

    calculator = Calculator.Calculator(starting_class, weapon_extra_data, weapon_passive, weapon_attack,
             weapon_scaling, weapon_correct_id, weapon_element_correct)




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

    return calculator


def main():


    calculator = initData()
    value_map = calculator.optimize()
    #value_map = optimize(calculator)


    #value_map = tryPoints()

    for key, value in value_map.items():
        print(f"{key}: {value}")

    # TODO:  Sort by damage
    # sorted_values = dict(sorted(value_map.items(), key=lambda item: item[1]))
    # for key, value in sorted_values.items():
    #     print(f"{key}: {value}")

    # TODO: Sort by damage + passives
    # sorted_values = dict(sorted(value_map.items(), key=lambda item: (str(item[1]), item[1])))
    # for key, value in sorted_values.items():
    #     print(f"{key}: {value}")

    # TODO: Find best combined, best total dmg, first high passive, stats divided by 10 (soft caps)


if __name__ == "__main__":
    main()