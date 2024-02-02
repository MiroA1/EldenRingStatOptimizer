import Calculator
import Combination


class Optimizer:
    def __init__(self, starting_class, weapon_extra_data, weapon_passive, weapon_attack,
                 weapon_scaling, weapon_correct_id, weapon_element_correct):

        self.starting_class = starting_class
        self.weapon_extra_data = weapon_extra_data
        self.weapon_passive = weapon_passive
        self.weapon_attack = weapon_attack
        self.weapon_scaling = weapon_scaling
        self.weapon_correct_id = weapon_correct_id
        self.weapon_element_correct = weapon_element_correct


    def getScalingStats(self):

        scaling_list = []

        if self.weapon_scaling.getStrScaling() > 0 or self.weapon_extra_data.getRequiredStr() > 0:
            scaling_list.append("Str")
        if self.weapon_scaling.getDexScaling() > 0 or self.weapon_extra_data.getRequiredDex() > 0:
            scaling_list.append("Dex")
        if self.weapon_scaling.getIntScaling() > 0 or self.weapon_extra_data.getRequiredInt() > 0:
            scaling_list.append("Int")
        if self.weapon_scaling.getFaiScaling() > 0 or self.weapon_extra_data.getRequiredFai() > 0:
            scaling_list.append("Fai")
        if self.weapon_scaling.getArcScaling() > 0 or self.weapon_extra_data.getRequiredArc() > 0:
            scaling_list.append("Arc")

        return scaling_list


    def getStatString(self, scaling_list):

        return ', '.join(f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
                         for stat in scaling_list)

    def createNewComb1(self, scaling_list):

        stat_string = self.getStatString(scaling_list)
        stat_sum = getattr(self.starting_class, f'getCurrent{scaling_list[0]}')()

        combination = Combination.Combination(stat_string,
                                              stat_sum,
                                              Calculator.calculateTotalDmg(self),
                                              self.weapon_passive.getPassiveType1(),
                                              self.weapon_passive.getPassiveType2(),
                                              Calculator.calcPassive1(self),
                                              Calculator.calcPassive2(self))

        return combination

    def createNewComb2(self, scaling_list, dec_index, inc_index):


        stat_string = self.getStatString(scaling_list)

        stat_sum = (getattr(self.starting_class, f'getCurrent{scaling_list[dec_index]}')()
                    + getattr(self.starting_class,f'getCurrent{scaling_list[inc_index]}')())

        combination = Combination.Combination(stat_string,
                                              stat_sum,
                                              Calculator.calculateTotalDmg(self),
                                              self.weapon_passive.getPassiveType1(),
                                              self.weapon_passive.getPassiveType2(),
                                              Calculator.calcPassive1(self),
                                              Calculator.calcPassive2(self))

        return combination

    def createNewComb3(self, scaling_list, dec_index, inc_index, start_index):


        stat_string = self.getStatString(scaling_list)

        stat_sum = (getattr(self.starting_class, f'getCurrent{scaling_list[dec_index]}')()
                    + getattr(self.starting_class,f'getCurrent{scaling_list[inc_index]}')()
                    + getattr(self.starting_class, f'getCurrent{scaling_list[start_index]}')())

        combination = Combination.Combination(stat_string,
                                              stat_sum,
                                              Calculator.calculateTotalDmg(self),
                                              self.weapon_passive.getPassiveType1(),
                                              self.weapon_passive.getPassiveType2(),
                                              Calculator.calcPassive1(self),
                                              Calculator.calcPassive2(self))

        return combination


    def optimize(self):

        value_list = []
        scaling_list = self.getScalingStats()
        allocated_points = 70

        attribute_setters = {
            "Str": self.starting_class.setCurrentStr,
            "Dex": self.starting_class.setCurrentDex,
            "Int": self.starting_class.setCurrentInt,
            "Fai": self.starting_class.setCurrentFai,
            "Arc": self.starting_class.setCurrentArc,
        }

        # for stat in scaling_list:
        #     print(f"Start of loop {stat}: {getattr(self.starting_class, f'getMin{stat}')()}")

        # Use all points starting from the first (str)
        alloc_temp = allocated_points
        index = 0

        while alloc_temp > 0 and index < len(scaling_list):
            if getattr(self.starting_class, f'getCurrent{scaling_list[index]}')() == 99:
                index += 1
                continue
            elif getattr(self.starting_class,
                         f'getCurrent{scaling_list[index]}')() + alloc_temp > 99:

                attribute_setters[scaling_list[index]](99)
                difference = 99 - getattr(self.starting_class,
                                          f'getMin{scaling_list[index]}')()
                alloc_temp = alloc_temp - difference

                if index + 1 < len(scaling_list):
                    if getattr(self.starting_class,
                               f'getCurrent{scaling_list[index + 1]}')() + alloc_temp > 99:
                        attribute_setters[scaling_list[index + 1]](99)
                        difference = 99 - getattr(self.starting_class,
                                                  f'getMin{scaling_list[index + 1]}')()
                        alloc_temp = alloc_temp - difference
                    else:
                        attribute_setters[scaling_list[index + 1]](
                            getattr(self.starting_class,
                                    f'getCurrent{scaling_list[index + 1]}')() + alloc_temp)
                        difference = getattr(self.starting_class,
                                             f'getCurrent{scaling_list[index + 1]}')() - getattr(
                            self.starting_class, f'getMin{scaling_list[index + 1]}')()
                        alloc_temp = alloc_temp - difference
            else:
                attribute_setters[scaling_list[index]](getattr(self.starting_class,
                                                               f'getCurrent{scaling_list[index]}')() + alloc_temp)
                difference = getattr(self.starting_class,
                                     f'getCurrent{scaling_list[index]}')() - getattr(
                    self.starting_class, f'getMin{scaling_list[index]}')()
                alloc_temp = alloc_temp - difference

            index += 1


        # for stat in scaling_list:
        #     print(
        #         f"End of loop {stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}")
        #
        # print(f"Excess points: {alloc_temp}")





        # stat_string = ', '.join(
        #     f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
        #     for stat in scaling_list)
        # value_map[stat_string] = Calculator.calculateTotalDmg(self)
        # combination = Combination.Combination(stat_string,
        #                                       Calculator.calculateTotalDmg(self),
        #                                       self.weapon_passive.getPassiveType1(),
        #                                       self.weapon_passive.getPassiveType2(),
        #                                       Calculator.calcPassive1(self),
        #                                       Calculator.calcPassive2(self))
        #value_list.append(combination)
        #value_list.append(self.createNewComb(scaling_list, dec_index, inc_index, start_index))



        if len(scaling_list) == 1:
            if getattr(self.starting_class, f'getCurrent{scaling_list[0]}')() + allocated_points > 99:
                attribute_setters[scaling_list[index]](99)
            else:
                attribute_setters[scaling_list[index]](getattr(self.starting_class, f'getCurrent{scaling_list[0]}')() + allocated_points)
            # stat_string = ', '.join(
            #     f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
            #     for stat in scaling_list)
            # value_map[stat_string] = Calculator.calculateTotalDmg(self)
            value_list.append(self.createNewComb1(scaling_list))



        elif len(scaling_list) == 2:
            while (getattr(self.starting_class, f'getCurrent{scaling_list[0]}')() > getattr(self.starting_class, f'getMin{scaling_list[0]}')()
                   and getattr(self.starting_class,f'getCurrent{scaling_list[1]}')() < 99):

                attribute_setters[scaling_list[0]](getattr(self.starting_class, f'getCurrent{scaling_list[0]}')() - 1)
                attribute_setters[scaling_list[1]](getattr(self.starting_class, f'getCurrent{scaling_list[1]}')() + 1)
                # stat_string = ', '.join(
                #     f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
                #     for stat in scaling_list)
                # value_map[stat_string] = (
                #     f"Dmg: {Calculator.calculateTotalDmg(self)}  |  "
                #     f"P1: {self.weapon_passive.getPassiveType1()}: {Calculator.calcPassive1(self)}  |  "
                #     f"P2: {self.weapon_passive.getPassiveType2()}: {Calculator.calcPassive2(self)}")
                value_list.append(self.createNewComb2(scaling_list, 0, 1))



        elif len(scaling_list) == 3:

            save_stats = []
            for stat in scaling_list:
                save_stats.append(getattr(self.starting_class, f'getCurrent{stat}')())
            all_99 = False
            difference = 0
            start_index = 0
            dec_index = 1
            inc_index = 2

            # Initial combination
            value_list.append(self.createNewComb3(scaling_list, dec_index, inc_index, start_index))

            while (getattr(self.starting_class, f'getCurrent{scaling_list[dec_index]}')() > getattr(self.starting_class, f'getMin{scaling_list[dec_index]}')()
                   and getattr(self.starting_class, f'getCurrent{scaling_list[inc_index]}')() < 99):

                attribute_setters[scaling_list[dec_index]](getattr(self.starting_class, f'getCurrent{scaling_list[dec_index]}')() - 1)
                attribute_setters[scaling_list[inc_index]](getattr(self.starting_class, f'getCurrent{scaling_list[inc_index]}')() + 1)
                # stat_string = ', '.join(
                #     f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
                #     for stat in scaling_list)

                # value_map[stat_string] = Calculator.calculateTotalDmg(self)
                # combination = Combination.Combination(stat_string,
                #                                       Calculator.calculateTotalDmg(
                #                                           self),
                #                                       self.weapon_passive.getPassiveType1(),
                #                                       self.weapon_passive.getPassiveType2(),
                #                                       Calculator.calcPassive1(self),
                #                                       Calculator.calcPassive2(self))
                # value_list.append(combination)
                value_list.append(self.createNewComb3(scaling_list, dec_index, inc_index, start_index))

            attribute_setters[scaling_list[dec_index]](save_stats[dec_index])
            attribute_setters[scaling_list[inc_index]](save_stats[inc_index])


            while getattr(self.starting_class,
                          f'getCurrent{scaling_list[start_index]}')() > getattr(
                    self.starting_class, f'getMin{scaling_list[start_index]}')():
                attribute_setters[scaling_list[start_index]](
                    getattr(self.starting_class,
                            f'getCurrent{scaling_list[start_index]}')() - 1)
                difference += 1
                usable_points = difference
                while usable_points > 0:
                    if getattr(self.starting_class,
                               f'getCurrent{scaling_list[dec_index]}')() + 1 <= 99:
                        attribute_setters[scaling_list[dec_index]](
                            getattr(self.starting_class,
                                    f'getCurrent{scaling_list[dec_index]}')() + 1)
                        usable_points -= 1
                    else:
                        if getattr(self.starting_class,
                                   f'getCurrent{scaling_list[inc_index]}')() + 1 <= 99:
                            attribute_setters[scaling_list[inc_index]](
                                getattr(self.starting_class,
                                        f'getCurrent{scaling_list[inc_index]}')() + 1)
                            usable_points -= 1
                        else:
                            all_99 = True
                            break

                if all_99:
                    break

                # stat_string = ', '.join(
                #     f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
                #     for stat in scaling_list)
                # value_map[stat_string] = Calculator.calculateTotalDmg(self)
                # combination = Combination.Combination(stat_string,
                #                                       Calculator.calculateTotalDmg(
                #                                           self),
                #                                       self.weapon_passive.getPassiveType1(),
                #                                       self.weapon_passive.getPassiveType2(),
                #                                       Calculator.calcPassive1(self),
                #                                       Calculator.calcPassive2(self))
                #value_list.append(combination)
                value_list.append(self.createNewComb3(scaling_list, dec_index, inc_index, start_index))

                while getattr(self.starting_class,
                              f'getCurrent{scaling_list[dec_index]}')() > getattr(
                        self.starting_class,
                        f'getMin{scaling_list[dec_index]}')() and getattr(
                        self.starting_class,
                        f'getCurrent{scaling_list[inc_index]}')() < 99:
                    attribute_setters[scaling_list[dec_index]](
                        getattr(self.starting_class,
                                f'getCurrent{scaling_list[dec_index]}')() - 1)
                    attribute_setters[scaling_list[inc_index]](
                        getattr(self.starting_class,
                                f'getCurrent{scaling_list[inc_index]}')() + 1)
                    # stat_sum = getattr(self.starting_class,
                    #                    f'getCurrent{scaling_list[dec_index]}')() + getattr(
                    #     self.starting_class,
                    #     f'getCurrent{scaling_list[inc_index]}')() + getattr(
                    #     self.starting_class, f'getCurrent{scaling_list[start_index]}')()
                    # stat_string = ', '.join(
                    #     f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
                    #     for stat in scaling_list)
                    #stat_string = stat_string + f" | stat_sum: {stat_sum}"
                    # value_map[stat_string] = (f"Dmg: {Calculator.calculateTotalDmg(self)}  |  "
                    #                           f"P1: {self.weapon_passive.getPassiveType1()}: {Calculator.calcPassive1(self)}  |  "
                    #                           f"P2: {self.weapon_passive.getPassiveType2()}: {Calculator.calcPassive2(self)}  |  "
                    #                           f"All sum: {Calculator.calculateTotalDmg(self) + Calculator.calcPassive1(self) + Calculator.calcPassive2(self)}")
                    # combination = Combination.Combination(stat_string, stat_sum, Calculator.calculateTotalDmg(self), self.weapon_passive.getPassiveType1(),
                    #                                       self.weapon_passive.getPassiveType2(), Calculator.calcPassive1(self), Calculator.calcPassive2(self))

                    value_list.append(self.createNewComb3(scaling_list, dec_index, inc_index, start_index))

                # Reset values
                attribute_setters[scaling_list[dec_index]](save_stats[dec_index])
                attribute_setters[scaling_list[inc_index]](save_stats[inc_index])



        return value_list
        #return value_map
