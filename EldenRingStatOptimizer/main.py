import csv
from StartingClass import StartingClass
import Calculator
import DataReader

TOTAL_SKILL_POINTS = 70

# TODO: Morgott's cursed sword | blood affinity
# TODO: pick needed attributes from dict
SCALING_ATTRIBUTES = {"str": "0.27", "dex": "1.08", "arc": "0.54"}
SCALING_COUNT = 3
BASE_DMG = 294
BLOOD_BASE = 60
CALC_ID = 7
STR_SCALING = 0.27
DEX_SCALING = 1.08
ARC_SCALING = 0.54
MIN_STR_WEAPON = 14
MIN_DEX_WEAPON = 35
MIN_ARC_WEAPON = 17


# TODO: Starting class (Hero)
MIN_STR = 16
MIN_DEX = 9
MIN_INT = 7
MIN_FAITH = 8
MIN_ARC = 11



def calcPassiveArc(current_arc):

    if current_arc > 60:
        return (90 + 10 * ((current_arc - 60) / 39)) / 100
    elif current_arc > 45:
        return (75 + 15 * ((current_arc - 45) / 15)) / 100
    elif current_arc > 25:
        return (10 + 65 * ((current_arc - 25) / 20)) / 100
    else:
        return (10 * ((current_arc - 1) / 24)) / 100


def calcBloodloss(current_arc):

    passive_arc = calcPassiveArc(current_arc)

    bloodloss = (ARC_SCALING * (passive_arc * BLOOD_BASE)) + BLOOD_BASE

    bloodloss_floored = int(bloodloss)

    return bloodloss



def tryPoints():

    combination_counter = 0

    value_map = {}

    current_str = 0

    #if SCALING_COUNT == 3 and + TOTAL_SKILL_POINTS <= 99:

    if MIN_STR + TOTAL_SKILL_POINTS <= 99:
        current_str = MIN_STR + TOTAL_SKILL_POINTS

        max_str = current_str
        current_dex = 9
        current_arc = 11

        stat_sum = current_str + current_dex + current_arc
        current_dmg = f"{calculate_dmg(current_str, current_dex, current_arc)} + ({calcBloodloss(current_arc)}) + stat_sum: {stat_sum}"
        attributes = f"str: {current_str}, dex: {current_dex}, arc: {current_arc} "
        value_map[attributes] = current_dmg
        combination_counter += 1

        while current_str > MIN_STR:

            current_str -= 1
            usable_points = max_str - current_str
            usable_points2 = usable_points

            current_dex += usable_points

            comb_count = 0
            while comb_count < usable_points + 1:

                stat_sum = current_str + current_dex + current_arc
                current_dmg = f"{calculate_dmg(current_str, current_dex, current_arc)} + ({calcBloodloss(current_arc)}) + stat_sum: {stat_sum}"
                current_dmg2 = f"{round(calculate_dmg(current_str, current_dex, current_arc) + calcBloodloss(current_arc), 3)} | dmg: {round(calculate_dmg(current_str, current_dex, current_arc), 5)} + ({round(calcBloodloss(current_arc), 3)})"
                attributes = f"str: {current_str}, dex: {current_dex}, arc: {current_arc} "
                value_map[attributes] = current_dmg2
                combination_counter += 1
                comb_count += 1

                current_dex = MIN_DEX

                current_dex += (usable_points2 - 1)
                current_arc += 1
                usable_points2 -= 1

            current_dex = MIN_DEX
            current_arc = MIN_ARC

    elif MIN_STR + TOTAL_SKILL_POINTS > 99:
        current_str = 99
        current_dex = (TOTAL_SKILL_POINTS - (99 - MIN_STR)) + MIN_DEX

    print(f"COMBINATIONS: {combination_counter}")
    return value_map



def calcCorrectStat_0(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 18:
        return 25 + 50 * (1 - (1 - (current_stat - 18) / 42) ** 1.2)
    else:
        return 25 * ((current_stat - 1) / 17) ** 1.2


def calcCorrectStat_1(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 20:
        return 35 + 40 * (1 - (1 - (current_stat - 20) / 40) ** 1.2)
    else:
        return 35 * ((current_stat - 1) / 19) ** 1.2


def calcCorrectStat_7(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 20:
        return 35 + 40 * (1 - (1 - (current_stat - 20) / 40) ** 1.2)
    else:
        return 35 * ((current_stat - 1) / 19) ** 1.2


def calculate_dmg(current_str, current_dex, current_arc):

    true_base_dmg = BASE_DMG

    if CALC_ID == 0:
        str_scale = calcCorrectStat_0(current_str)
        dex_scale = calcCorrectStat_0(current_dex)
        arc_scale = calcCorrectStat_0(current_arc)

    elif CALC_ID == 1:
        str_scale = calcCorrectStat_1(current_str)
        dex_scale = calcCorrectStat_1(current_dex)
        arc_scale = calcCorrectStat_1(current_arc)

    elif CALC_ID == 7:
        str_scale = calcCorrectStat_7(current_str)
        dex_scale = calcCorrectStat_7(current_dex)
        arc_scale = calcCorrectStat_7(current_arc)

    if (current_str < MIN_STR_WEAPON) or (current_dex < MIN_DEX_WEAPON) or (current_arc < MIN_ARC_WEAPON):
        true_base_dmg = BASE_DMG * (-0.4)
        total_dmg = BASE_DMG + true_base_dmg
    else:
        # TODO: Add int and faith
        total_phys_dmg = (true_base_dmg * STR_SCALING * (str_scale / 100)
                          + true_base_dmg * DEX_SCALING * (dex_scale / 100)
                          + true_base_dmg * ARC_SCALING * (arc_scale / 100))
        total_dmg = total_phys_dmg + true_base_dmg

    total_dmg_floored = int(total_dmg)

    return total_dmg

def optimize():
    return






def initData():

    class_name = "Hero"
    weapon_name = "Great Stars"
    affinity = "Occult"

    max_upgrade_level = DataReader.getWeaponMaxUpgradeLevel(weapon_name)
    weapon_upgrade_level = 25

    if affinity != "":
        weapon = affinity + " " + weapon_name
    else:
        weapon = weapon_name

    #is_2handing = False

    starting_class = DataReader.initStartingClass(class_name)
    weapon_extra_data = DataReader.initWeaponExtraData(weapon, weapon_upgrade_level)
    weapon_passive = DataReader.initWeaponPassive(weapon, weapon_upgrade_level)
    weapon_attack = DataReader.initWeaponAttack(weapon, weapon_upgrade_level)
    weapon_scaling = DataReader.initWeaponScaling(weapon, weapon_upgrade_level)
    weapon_correct_id = DataReader.initWeaponCorrectId(weapon)
    weapon_element_correct = DataReader.initWeaponElementCorrect(weapon_correct_id)

    optimize()




    print(f"Starting class: {starting_class.getName()}")
    print(f"min Vigor: {starting_class.getMinVigor()}")
    print(f"min Strength: {starting_class.getMinStrength()}")
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


def main():

    initData()


    #value_map = tryPoints()

    # for key, value in value_map.items():
    #     print(f"{key}: {value}")

    # TODO:  Sort by damage
    # sorted_values = dict(sorted(value_map.items(), key=lambda item: item[1]))
    # for key, value in sorted_values.items():
    #     print(f"{key}: {value}")

    # TODO: Sort by damage + bloodloss
    # sorted_values = dict(sorted(value_map.items(), key=lambda item: (str(item[1]), item[1])))
    # for key, value in sorted_values.items():
    #     print(f"{key}: {value}")

    # TODO: Find best combined, best phys dmg, first high bloodloss, stats divided by 10 (soft caps)


if __name__ == "__main__":
    main()