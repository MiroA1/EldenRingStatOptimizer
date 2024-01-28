import csv
import StartingClass
import WeaponAttack
import WeaponCorrectId
import WeaponElementCorrect
import WeaponExtraData
import WeaponPassive
import WeaponScaling


# class FileOperations:
#     def __init__(self, starting_class, weapon):
#         self.starting_class = starting_class
#         self.weapon = weapon


def initStartingClass(class_name):

    with open("Data/StartingClasses.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Class'] == class_name:
                min_vigor = int(row["Vigor"])
                min_mind = int(row["Mind"])
                min_endurance = int(row["Endurance"])
                min_strength = int(row["Strength"])
                min_dexterity = int(row["Dexterity"])
                min_intelligence = int(row["Intelligence"])
                min_faith = int(row["Faith"])
                min_arcane = int(row["Arcane"])
                soul_level = int(row["Level"])
                break

    return StartingClass.StartingClass(class_name, min_vigor, min_mind, min_endurance,
                                       min_strength, min_dexterity, min_intelligence, min_faith, min_arcane, soul_level)


def getWeaponMaxUpgradeLevel(weapon_name):

    with open("Data/ExtraData.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon_name:
                max_upgrade_level = row["Max Upgrade"]
                break

    return max_upgrade_level


def initWeaponExtraData(weapon_name, weapon_upgrade_level, is_2handing):

    with open("Data/ExtraData.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon_name:
                required_str = int(row["Required (Str)"])
                required_dex = int(row["Required (Dex)"])
                required_int = int(row["Required (Int)"])
                required_fai = int(row["Required (Fai)"])
                required_arc = int(row["Required (Arc)"])
                weapon_type = row['Weapon Type']
                two_hand_bonus = row['2H Str Bonus']
                break

    return WeaponExtraData.Weapon(weapon_name, weapon_upgrade_level,
                              required_str, required_dex, required_int, required_fai, required_arc,
                                  two_hand_bonus, weapon_type, is_2handing)


def initWeaponPassive(weapon_name, weapon_upgrade_level):

    passive_type1 = ""
    passive_type2 = ""

    rot_mad_sleep1 = 0
    frost_base1 = 0
    poison_base1 = 0
    blood_base1 = 0

    rot_mad_sleep2 = 0
    frost_base2 = 0
    poison_base2 = 0
    blood_base2 = 0

    with open("Data/Passive.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon_name:
                passive_type1 = row["Type 1"]
                passive_type2 = row["Type 2"]

                if passive_type1 == "Scarlet Rot":
                    rot_mad_sleep1 = row["Scarlet Rot +0"]
                elif passive_type1 == "Madness":
                    rot_mad_sleep1 = row["Madness +0"]
                elif passive_type1 == "Sleep":
                    rot_mad_sleep1 = row["Sleep +0"]
                elif passive_type1 == "Frost":
                    frost_base1 = row[f"Frost +{weapon_upgrade_level}"]
                elif passive_type1 == "Poison":
                    poison_base1 = row[f"Poison +{weapon_upgrade_level}"]
                elif passive_type1 == "Blood":
                    blood_base1 = row[f"Blood +{weapon_upgrade_level}"]

                if passive_type2 == "Scarlet Rot":
                    rot_mad_sleep2 = row["Scarlet Rot +0"]
                elif passive_type2 == "Madness":
                    rot_mad_sleep2 = row["Madness +0"]
                elif passive_type2 == "Sleep":
                    rot_mad_sleep2 = row["Sleep +0"]
                elif passive_type2 == "Frost":
                    frost_base2 = row[f"Frost +{weapon_upgrade_level}"]
                elif passive_type2 == "Poison":
                    poison_base2 = row[f"Poison +{weapon_upgrade_level}"]
                elif passive_type2 == "Blood":
                    blood_base2 = row[f"Blood +{weapon_upgrade_level}"]



    return WeaponPassive.WeaponPassive(passive_type1, passive_type2, rot_mad_sleep1, rot_mad_sleep2,
                                       frost_base1, frost_base2, poison_base1, poison_base2, blood_base1, blood_base2)


def initWeaponAttack(weapon_name, weapon_upgrade_level):

        phys_attack = 0
        mag_attack = 0
        fire_attack = 0
        ligh_attack = 0
        holy_attack = 0

        with open("Data/Attack.csv", 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['Name'] == weapon_name:
                    phys_attack = float(row[f"Phys +{str(weapon_upgrade_level)}"])
                    mag_attack = float(row[f"Mag +{weapon_upgrade_level}"])
                    fire_attack = float(row[f"Fire +{weapon_upgrade_level}"])
                    ligh_attack = float(row[f"Ligh +{weapon_upgrade_level}"])
                    holy_attack = float(row[f"Holy +{weapon_upgrade_level}"])


        return WeaponAttack.WeaponAttack(phys_attack, mag_attack, fire_attack, ligh_attack, holy_attack)


def initWeaponScaling(weapon_name, weapon_upgrade_level):

    with open("Data/Scaling.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon_name:
                str_scaling = float(row[f"Str +{weapon_upgrade_level}"])
                dex_scaling = float(row[f"Dex +{weapon_upgrade_level}"])
                int_scaling = float(row[f"Int +{weapon_upgrade_level}"])
                fai_scaling = float(row[f"Fai +{weapon_upgrade_level}"])
                arc_scaling = float(row[f"Arc +{weapon_upgrade_level}"])

    return WeaponScaling.WeaponScaling(str_scaling, dex_scaling, int_scaling, fai_scaling, arc_scaling)


def initWeaponCorrectId(weapon_name):

    with open("Data/CalcCorrectGraph_ID.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon_name:
                phys_calc_id = int(row["Physical"])
                mag_calc_id = int(row["Magic"])
                fire_calc_id = int(row["Fire"])
                ligh_calc_id = int(row["Lightning"])
                holy_calc_id = int(row["Holy"])
                attack_element_id = int(row["AttackElementCorrect ID"])

    return WeaponCorrectId.WeaponCorrectId(phys_calc_id, mag_calc_id, fire_calc_id, ligh_calc_id, holy_calc_id, attack_element_id)


def initWeaponElementCorrect(weapon_correct_id):

    phys_scales_on_str = 0
    phys_scales_on_dex = 0
    phys_scales_on_int = 0
    phys_scales_on_fai = 0
    phys_scales_on_arc = 0
    mag_scales_on_str = 0
    mag_scales_on_dex = 0
    mag_scales_on_int = 0
    mag_scales_on_fai = 0
    mag_scales_on_arc = 0
    fire_scales_on_str = 0
    fire_scales_on_dex = 0
    fire_scales_on_int = 0
    fire_scales_on_fai = 0
    fire_scales_on_arc = 0
    ligh_scales_on_str = 0
    ligh_scales_on_dex = 0
    ligh_scales_on_int = 0
    ligh_scales_on_fai = 0
    ligh_scales_on_arc = 0
    holy_scales_on_str = 0
    holy_scales_on_dex = 0
    holy_scales_on_int = 0
    holy_scales_on_fai = 0
    holy_scales_on_arc = 0


    with open("Data/AttackElementCorrectParam.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['ID'] == weapon_correct_id:
                phys_scales_on_str = int(row["isStrengthCorrect_byPhysics"])
                phys_scales_on_dex = int(row["isDexterityCorrect_byPhysics"])
                phys_scales_on_int = int(row["isMagicCorrect_byPhysics"])
                phys_scales_on_fai = int(row["isFaithCorrect_byPhysics"])
                phys_scales_on_arc = int(row["isLuckCorrect_byPhysics"])

                mag_scales_on_str = int(row["isStrengthCorrect_byMagic"])
                mag_scales_on_dex = int(row["isDexterityCorrect_byMagic"])
                mag_scales_on_int = int(row["isMagicCorrect_byMagic"])
                mag_scales_on_fai = int(row["isFaithCorrect_byMagic"])
                mag_scales_on_arc = int(row["isLuckCorrect_byMagic"])

                fire_scales_on_str = int(row["isStrengthCorrect_byFire"])
                fire_scales_on_dex = int(row["isDexterityCorrect_byFire"])
                fire_scales_on_int = int(row["isMagicCorrect_byFire"])
                fire_scales_on_fai = int(row["isFaithCorrect_byFire"])
                fire_scales_on_arc = int(row["isLuckCorrect_byFire"])

                ligh_scales_on_str = int(row["isStrengthCorrect_byThunder"])
                ligh_scales_on_dex = int(row["isDexterityCorrect_byThunder"])
                ligh_scales_on_int = int(row["isMagicCorrect_byThunder"])
                ligh_scales_on_fai = int(row["isFaithCorrect_byThunder"])
                ligh_scales_on_arc = int(row["isLuckCorrect_byThunder"])

                holy_scales_on_str = int(row["isStrengthCorrect_byDark"])
                holy_scales_on_dex = int(row["isDexterityCorrect_byDark"])
                holy_scales_on_int = int(row["isMagicCorrect_byDark"])
                holy_scales_on_fai = int(row["isFaithCorrect_byDark"])
                holy_scales_on_arc = int(row["isLuckCorrect_byDark"])


    return WeaponElementCorrect.WeaponElementCorrect(phys_scales_on_str, phys_scales_on_dex, phys_scales_on_int, phys_scales_on_fai, phys_scales_on_arc,
                                             mag_scales_on_str, mag_scales_on_dex, mag_scales_on_int, mag_scales_on_fai, mag_scales_on_arc,
                                             fire_scales_on_str, fire_scales_on_dex, fire_scales_on_int, fire_scales_on_fai, fire_scales_on_arc,
                                             ligh_scales_on_str, ligh_scales_on_dex, ligh_scales_on_int, ligh_scales_on_fai, ligh_scales_on_arc,
                                             holy_scales_on_str, holy_scales_on_dex, holy_scales_on_int, holy_scales_on_fai, holy_scales_on_arc)






