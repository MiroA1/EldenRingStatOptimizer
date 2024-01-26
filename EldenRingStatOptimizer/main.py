import csv
from StartingClass import StartingClass

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


def main():


    starting_class = "Hero"
    weapon_name = "Great Stars"
    max_upgrade_level = 0
    upgrade_level = 0

    file_path = "StartingClasses.csv"
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row["Class"] == starting_class:
                min_vigor = int(row["Vigor"])
                min_mind = int(row["Mind"])
                min_endurance = row["Endurance"]
                min_strength = row["Strength"]
                min_dexterity = row["Dexterity"]
                min_intelligence = row["Intelligence"]
                min_faith = row["Faith"]
                min_arcane = row["Arcane"]
                soul_level = row["Level"]
                break

    current_vigor = min_vigor
    current_mind = min_mind
    current_endurance = min_endurance
    current_str = min_strength
    current_dex = min_dexterity
    current_int = min_intelligence
    current_fai = min_faith
    current_arc = min_arcane
    current_soul_level = soul_level

    starting_class = StartingClass(starting_class, min_vigor, min_mind, min_endurance, min_strength, min_dexterity, min_intelligence, min_faith, min_arcane, soul_level)
    print(f"object test {starting_class.name}")

    current_str = 60
    current_dex = 20
    current_int = 20
    current_fai = 15
    current_arc = 30

    #print(f"Starting class: {starting_class}")
    print(f"Vigor: {min_vigor}")
    print(f"Mind: {min_mind}")
    print(f"Endurance: {min_endurance}")
    print(f"Strength: {min_strength}")
    print(f"Dexterity: {min_dexterity}")
    print(f"Intelligence: {min_intelligence}")
    print(f"Faith: {min_faith}")
    print(f"Arcane: {min_arcane}")
    print(f"Soul Level: {soul_level}")

    file_path = "Extra_Data.csv"

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon_name:
                max_upgrade_level = row["Max Upgrade"]
                break

    print(f"max_upgrades {max_upgrade_level}")
    upgrade_level = max_upgrade_level

    # TODO: make affinity list
    affinity = "Blood"


    weapon = affinity + " " + weapon_name
    print(weapon)

    #TODO: checkbox

    is_2handing = False

    required_str = 0
    required_dex = 0
    required_int = 0
    required_faith = 0
    required_arc = 0
    weapon_type = None

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon:
                required_str = int(row["Required (Str)"])
                required_dex = int(row.get('Required (Dex)', 0))
                required_int = int(row.get('Required (Int)', 0))
                required_fai = int(row["Required (Fai)"])
                required_arc = int(row.get('Required (Arc)', 0))
                weapon_type = str(row['Weapon Type'])
                break

    print(required_str)
    print(required_dex)
    print(required_int)
    print(required_fai)
    print(required_arc)
    print(weapon_type)

    str_req_met = 0
    dex_req_met = 0
    int_req_met = 0
    fai_req_met = 0
    arc_req_met = 0

    if current_str >= required_str:
        str_req_met = 1
    if current_dex >= required_dex:
        dex_req_met = 1
    if current_int >= required_int:
        int_req_met = 1
    if current_fai >= required_fai:
        faith_req_met = 1
    if current_arc >= required_arc:
        arc_req_met = 1


    has_affinity = False

    with open("Extra_Data.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon:
                if row['Affinity'] != "-":
                    has_affinity = True
                break

    print(has_affinity)

    has_2hbonus = False

    with open("Extra_Data.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon:
                if row['2H Str Bonus'] == "Yes":
                    has_2hbonus = True
                break

    print(has_2hbonus)
















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