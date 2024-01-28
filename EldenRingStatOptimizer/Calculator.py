import CalcModule
import SwitchFunctions
import WeaponCorrectId


class Calculator:
    def __init__(self, starting_class, weapon_extra_data, weapon_passive, weapon_attack,
             weapon_scaling, weapon_correct_id, weapon_element_correct):

        self.starting_class = starting_class
        self.weapon = weapon_extra_data
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

        if self.weapon_scaling.getStrScaling() > 0:
            scaling_count += 1
            scaling_list.append("Str")
        if self.weapon_scaling.getDexScaling() > 0:
            scaling_count += 1
            scaling_list.append("Dex")
        if self.weapon_scaling.getIntScaling() > 0:
            scaling_count += 1
            scaling_list.append("Int")
        if self.weapon_scaling.getFaiScaling() > 0:
            scaling_count += 1
            scaling_list.append("Fai")
        if self.weapon_scaling.getArcScaling() > 0:
            scaling_count += 1
            scaling_list.append("Arc")

        return scaling_list



    def calculate_dmg(self):

        # true_base_dmg = self.weapon_attack.getPhysAttack()
        #
        # if self.weapon_correct_id.getPhysCalcId() == 1:
        #     str_scale = calcCorrectStat_0(self.starting_class.getCurrentStr())
        #     dex_scale = calcCorrectStat_0(current_dex)
        #     arc_scale = calcCorrectStat_0(current_arc)
        #
        # elif CALC_ID == 1:
        #     str_scale = calcCorrectStat_1(current_str)
        #     dex_scale = calcCorrectStat_1(current_dex)
        #     arc_scale = calcCorrectStat_1(current_arc)


        # if self.starting_class.getCurrentStr() < self.weapon.getRequiredStr():
        #
        #     true_base_dmg = self.weapon_attack.getPhysAttack() * (-0.4)
        #     total_dmg = round(self.weapon_attack.getPhysAttack() + true_base_dmg, 5)
        # else:
        #     total_phys_dmg = (true_base_dmg * self.weapon_scaling.getStrScaling() * (str_scale / 100))
        #                       # + true_base_dmg * DEX_SCALING * (dex_scale / 100)
        #                       # + true_base_dmg * ARC_SCALING * (arc_scale / 100))
        #     total_dmg = round(total_phys_dmg + true_base_dmg, 5)


        total_dmg = (CalcModule.calcPhysDamage(self) + self.weapon_attack.getPhysAttack() +
                     self.calcMagDamage() + self.weapon_attack.getMagAttack() +
                     self.calcFireDamage() + self.weapon_attack.getFireAttack() +
                     self.calcLighDamage() + self.weapon_attack.getLighAttack() +
                     self.calcHolyDamage() + self.weapon_attack.getHolyAttack())

        return total_dmg

    def optimize(self):

        combination_counter = 0
        value_map = {}
        allocated_points = 90

        scaling_list = self.getScalingCount()
        scaling_count = len(scaling_list)

        # if scaling_count == 1:
        #     if scaling_list[0] == "Str":
        #         if self.starting_class.getMinStr() + allocated_points > 99:
        #             self.starting_class.setCurrentStr(99)
        #         else:
        #             self.starting_class.setCurrentStr(self.starting_class.getMinStr() + allocated_points)
        #     elif scaling_list[0] == "Dex":
        #         if self.starting_class.getMinDex() + allocated_points > 99:
        #             self.starting_class.setCurrentDex(99)
        #         else:
        #             self.starting_class.setCurrentDex(self.starting_class.getMinDex() + allocated_points)
        #     elif scaling_list[0] == "Int":
        #         if self.starting_class.getMinInt() + allocated_points > 99:
        #             self.starting_class.setCurrentInt(99)
        #         else:
        #             self.starting_class.setCurrentInt(self.starting_class.getMinInt() + allocated_points)
        #     elif scaling_list[0] == "Fai":
        #         if self.starting_class.getMinFai() + allocated_points > 99:
        #             self.starting_class.setCurrentFai(99)
        #         else:
        #             self.starting_class.setCurrentFai(self.starting_class.getMinFai() + allocated_points)
        #     elif scaling_list[0] == "Arc":
        #         if self.starting_class.getMinArc() + allocated_points > 99:
        #             self.starting_class.setCurrentArc(99)
        #         else:
        #             self.starting_class.setCurrentArc(self.starting_class.getMinArc() + allocated_points)

        if scaling_count == 1:
            attribute = scaling_list[0]
            min_value = getattr(self.starting_class, f'getMin{attribute}')()
            current_value = min(min_value + allocated_points, 99)
            setattr(self.starting_class, f'setCurrent{attribute}', current_value)

            current_dmg = self.calculate_dmg()
            attributes = f"{scaling_list[0]}: {current_value}"
            value_map[attributes] = current_dmg
            combination_counter += 1
            print(f"COMBINATIONS: {combination_counter}")
            return value_map

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






