import CalcModule
from itertools import product
from collections import OrderedDict

class Calculator:
    def __init__(self, starting_class, weapon_extra_data, weapon_passive, weapon_attack,
             weapon_scaling, weapon_correct_id, weapon_element_correct):

        self.starting_class = starting_class
        self.weapon_extra_data = weapon_extra_data
        self.weapon_passive = weapon_passive
        self.weapon_attack = weapon_attack
        self.weapon_scaling = weapon_scaling
        self.weapon_correct_id = weapon_correct_id
        self.weapon_element_correct = weapon_element_correct

    # def getScalingCount(self):
    #     scaling_attributes = ["Str", "Dex", "Int", "Fai", "Arc"]
    #     scaling_list = []
    #
    #     for attribute in scaling_attributes:
    #         scaling_value = getattr(self.weapon_scaling, f'get{attribute}Scaling')()
    #         if scaling_value > 0:
    #             scaling_list.append(attribute)
    #
    #     return scaling_list

    def getScalingCount(self):

        scaling_count = 0
        scaling_list = []

        if self.weapon_scaling.getStrScaling() > 0 or self.weapon_extra_data.getRequiredStr() > 0:
            scaling_count += 1
            scaling_list.append("Str")
        if self.weapon_scaling.getDexScaling() > 0 or self.weapon_extra_data.getRequiredDex() > 0:
            scaling_count += 1
            scaling_list.append("Dex")
        if self.weapon_scaling.getIntScaling() > 0 or self.weapon_extra_data.getRequiredInt() > 0:
            scaling_count += 1
            scaling_list.append("Int")
        if self.weapon_scaling.getFaiScaling() > 0 or self.weapon_extra_data.getRequiredFai() > 0:
            scaling_count += 1
            scaling_list.append("Fai")
        if self.weapon_scaling.getArcScaling() > 0 or self.weapon_extra_data.getRequiredArc() > 0:
            scaling_count += 1
            scaling_list.append("Arc")

        return scaling_list



    def calculate_dmg(self):

        if self.starting_class.getCurrentStr() < self.weapon_extra_data.getRequiredStr():
            str_req_met = 0
        else:
            str_req_met = 1

        if self.starting_class.getCurrentDex() < self.weapon_extra_data.getRequiredDex():
            dex_req_met = 0
        else:
            dex_req_met = 1

        if self.starting_class.getCurrentInt() < self.weapon_extra_data.getRequiredInt():
            int_req_met = 0
        else:
            int_req_met = 1

        if self.starting_class.getCurrentFai() < self.weapon_extra_data.getRequiredFai():
            fai_req_met = 0
        else:
            fai_req_met = 1

        if self.starting_class.getCurrentArc() < self.weapon_extra_data.getRequiredArc():
            arc_req_met = 0
        else:
            arc_req_met = 1

        total_dmg = (CalcModule.calcPhysDamage(self, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met) + self.weapon_attack.getPhysAttack() +
                     CalcModule.calcMagDamage(self, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met) + self.weapon_attack.getMagAttack() +
                     CalcModule.calcFireDamage(self, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met) + self.weapon_attack.getFireAttack() +
                     CalcModule.calcLighDamage(self, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met) + self.weapon_attack.getLighAttack() +
                     CalcModule.calcHolyDamage(self, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met) + self.weapon_attack.getHolyAttack())

        #print(self.starting_class.getCurrentStr())
        return round(total_dmg, 5)

    # def generate_combinations(self, scaling_list, allocated_points, max_stat_value):
    #     return product(range(min(allocated_points + 1, max_stat_value + 1)),
    #                    repeat=len(scaling_list))

    def calculate_stat_diff_sum(self, stats_dict):
        return sum(
            stats_dict[stat] - getattr(self.starting_class, f"getMin{stat}")()
            for stat in stats_dict
        )

    def is_valid_combination(self, stats_dict, allocated_points):
        return self.calculate_stat_diff_sum(stats_dict) == allocated_points

    def optimize(self):
        combination_counter = 0
        value_map = {}
        allocated_points = 3
        max_stat_value = 99

        scaling_list = self.getScalingCount()

        for allocated_value in range(allocated_points + 1):
            print(f"allocated points = {allocated_value}")
            print("combinations:")

            for combination in product(range(min(allocated_value + 1, max_stat_value + 1)),
                                       repeat=len(scaling_list)):
                stats_dict = OrderedDict(zip(scaling_list, combination))

                if self.is_valid_combination(stats_dict, allocated_value):
                    print(', '.join(
                        f"{stat}: {value}" for stat, value in stats_dict.items()))
                    combination_counter += 1
                    current_dmg = self.calculate_dmg()  # Replace with your actual calculation
                    stats = ', '.join(
                        f"{stat}: {value}" for stat, value in stats_dict.items())
                    value_map[stats] = current_dmg

        print(f"Total combinations: {combination_counter}")

    # def optimize(self):
    #
    #     combination_counter = 0
    #     value_map = {}
    #     allocated_points = 1
    #     max_stat_value = 99
    #
    #     scaling_list = self.getScalingCount()
    #     #print(scaling_list)
    #     #scaling_count = len(scaling_list)
    #
    #     for combination in self.generate_combinations(scaling_list, allocated_points,
    #                                                   max_stat_value):
    #
    #         if self.is_valid_combination(combination, allocated_points, max_stat_value):
    #             stats_dict = OrderedDict(zip(scaling_list, combination))
    #
    #             for stat, stat_value in stats_dict.items():
    #                 print(stats_dict)
    #                 #setattr(self.starting_class, f'setCurrent{stat}', value)
    #                 if stat == "Str":
    #                     self.starting_class.setCurrentStr(stat_value)
    #                 elif stat == "Dex":
    #                     self.starting_class.setCurrentDex(stat_value)
    #                 elif stat == "Int":
    #                     self.starting_class.setCurrentInt(stat_value)
    #                 elif stat == "Fai":
    #                     self.starting_class.setCurrentFai(stat_value)
    #                 elif stat == "Arc":
    #                     self.starting_class.setCurrentArc(stat_value)
    #
    #             current_dmg = self.calculate_dmg()
    #             combination_counter += 1
    #             stats = ', '.join(
    #                 f"{stat}: {stat_value}" for stat, stat_value in stats_dict.items())
    #             value_map[stats] = current_dmg


        # for combination in product(range(min(allocated_points + 1, max_stat_value + 1)),
        #                            repeat=len(scaling_list)):
        #     if sum(combination) == allocated_points:
        #         stats_dict = dict(zip(scaling_list, combination))
        #
        #         # Check if the combination satisfies the minimum value condition for each stat
        #         if all(
        #                 combination[idx] >= getattr(self.starting_class,
        #                                             f'getCurrent{stat}')()
        #                 for idx, stat in enumerate(scaling_list)
        #         ):
        #             print("Condition Passed!")
        #             combination_counter += 1
        #
        #             # Adjust stats dynamically based on the combination
        #             for stat, value in stats_dict.items():
        #                 current_value = getattr(self.starting_class,
        #                                         f'getCurrent{stat}')()
        #
        #                 setattr(self.starting_class, f'setCurrent{stat}',
        #                         current_value + value)
        #
        #             current_dmg = self.calculate_dmg()
        #             key = ', '.join(
        #                 f"{stat}: {value}" for stat, value in stats_dict.items())
        #             value_map[key] = current_dmg
        #
        #             # Reset stats to their original values after calculating damage
        #             for stat, value in stats_dict.items():
        #                 current_value = getattr(self.starting_class,
        #                                         f'getCurrent{stat}')()
        #                 setattr(self.starting_class, f'setCurrent{stat}',
        #                         current_value - value)

        # for combination in product(range(min(allocated_points + 1, max_stat_value + 1)),
        #                            repeat=len(scaling_list)):
        #     if sum(combination) == allocated_points:
        #         stats_dict = dict(zip(scaling_list, combination))
        #
        #         # Check if the combination satisfies the minimum value condition for each stat
        #         if all(
        #                 combination[idx] >= getattr(self.starting_class,
        #                                             f'getMin{stat}')()
        #                 for idx, stat in enumerate(scaling_list)
        #         ):
        #             combination_counter += 1
        #             current_dmg = self.calculate_dmg()
        #             key = ', '.join(
        #                 f"{stat}: {value}" for stat, value in stats_dict.items())
        #             value_map[key] = current_dmg

        #MAX WWORKS
        # for combination in product(range(min(allocated_points + 1, max_stat_value + 1)),
        #                            repeat=len(scaling_list)):
        #     if sum(combination) == allocated_points and all(
        #             value <= max_stat_value for value in combination):
        #         stats_dict = dict(zip(scaling_list, combination))
        #         combination_counter += 1
        #         current_dmg = self.calculate_dmg()
        #         key = ', '.join(
        #             f"{stat}: {value}" for stat, value in stats_dict.items())
        #         value_map[key] = current_dmg


        # for combination in product(range(allocated_points + 1), repeat=len(scaling_list)):
        #     if sum(combination) == allocated_points:
        #         stats_dict = dict(zip(scaling_list, combination))
        #         combination_counter += 1
        #         current_dmg = self.calculate_dmg()
        #         key = ', '.join(
        #             f"{stat}: {value}" for stat, value in stats_dict.items())
        #         value_map[key] = current_dmg

        # TODO: väärä approach, ei toimi pitää testata että requirementit täyttyy
        # if scaling_count == 1:
        #     attribute = scaling_list[0]
        #     min_value = getattr(self.starting_class, f'getMin{attribute}')()
        #     current_value = min(min_value + allocated_points, 99)
        #     setattr(self.starting_class, f'setCurrent{attribute}', current_value)
        #
        #     current_dmg = self.calculate_dmg()
        #     attributes = f"{scaling_list[0]}: {current_value}"
        #     value_map[attributes] = current_dmg
        #     combination_counter += 1
        #     print(f"COMBINATIONS: {combination_counter}")
        #     return value_map




        # if MIN_STR + TOTAL_SKILL_POINTS <= 99:
        #     current_str = MIN_STR + TOTAL_SKILL_POINTS
        #
        #     max_str = current_str
        #     current_dex = 9
        #     current_arc = 11
        #
        #     stat_sum = current_str + current_dex + current_arc
        #     current_dmg = f"{calculate_dmg(current_str, current_dex, current_arc)} + ({calcBloodloss(current_arc)}) + stat_sum: {stat_sum}"
        #     attributes = f"str: {current_str}, dex: {current_dex}, arc: {current_arc} "
        #     value_map[attributes] = current_dmg
        #     combination_counter += 1
        #
        #     while current_str > MIN_STR:
        #
        #         current_str -= 1
        #         usable_points = max_str - current_str
        #         usable_points2 = usable_points
        #
        #         current_dex += usable_points
        #
        #         comb_count = 0
        #         while comb_count < usable_points + 1:
        #             stat_sum = current_str + current_dex + current_arc
        #             current_dmg = f"{calculate_dmg(current_str, current_dex, current_arc)} + ({calcBloodloss(current_arc)}) + stat_sum: {stat_sum}"
        #             current_dmg2 = f"{round(calculate_dmg(current_str, current_dex, current_arc) + calcBloodloss(current_arc), 3)} | dmg: {round(calculate_dmg(current_str, current_dex, current_arc), 5)} + ({round(calcBloodloss(current_arc), 3)})"
        #             attributes = f"str: {current_str}, dex: {current_dex}, arc: {current_arc} "
        #             value_map[attributes] = current_dmg2
        #             combination_counter += 1
        #             comb_count += 1
        #
        #             current_dex = MIN_DEX
        #
        #             current_dex += (usable_points2 - 1)
        #             current_arc += 1
        #             usable_points2 -= 1
        #
        #         current_dex = MIN_DEX
        #         current_arc = MIN_ARC
        #
        # elif MIN_STR + TOTAL_SKILL_POINTS > 99:
        #     current_str = 99
        #     current_dex = (TOTAL_SKILL_POINTS - (99 - MIN_STR)) + MIN_DEX

        print(f"COMBINATIONS: {combination_counter}")
        return value_map






