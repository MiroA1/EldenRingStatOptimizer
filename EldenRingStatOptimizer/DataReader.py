import csv
import StartingClass
import WeaponExtraData
import WeaponPassive

# class FileOperations:
#     def __init__(self, starting_class, weapon):
#         self.starting_class = starting_class
#         self.weapon = weapon


def initStartingClass(class_name):

    with open("StartingClasses.csv", 'r') as csv_file:
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

    with open("Extra_Data.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['Name'] == weapon_name:
                max_upgrade_level = row["Max Upgrade"]
                break

    return max_upgrade_level


def initWeaponExtraData(weapon_name, weapon_upgrade_level):

    with open("Extra_Data.csv", 'r') as csv_file:
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
                              required_str, required_dex, required_int, required_fai, required_arc, two_hand_bonus, weapon_type)


def initWeaponPassive(weapon_name, weapon_upgrade_level):

    rot_mad_sleep1 = 0
    frost_base1 = 0
    poison_base1 = 0
    blood_base1 = 0

    rot_mad_sleep2 = 0
    frost_base2 = 0
    poison_base2 = 0
    blood_base2 = 0

    with open("Passive.csv", 'r') as csv_file:
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

