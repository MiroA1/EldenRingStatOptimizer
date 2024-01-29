import CalcModule
import math
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




    def optimize(self):
        combination_counter = 0
        value_map = {}
        allocated_points = 3
        max_stat_value = 99

        scaling_list = self.getScalingCount()







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






