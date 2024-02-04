import Calculator
import Combination


class Optimizer:
    def __init__(self, starting_class, weapon_extra_data, weapon_passive, weapon_attack,
                 weapon_scaling, weapon_correct_id, weapon_element_correct,
                 use_custom_min_stats, custom_min_stats, current_stats):

        self.starting_class = starting_class
        self.weapon_extra_data = weapon_extra_data
        self.weapon_passive = weapon_passive
        self.weapon_attack = weapon_attack
        self.weapon_scaling = weapon_scaling
        self.weapon_correct_id = weapon_correct_id
        self.weapon_element_correct = weapon_element_correct
        self.use_custom_min_stats = use_custom_min_stats
        self.custom_min_stats = custom_min_stats
        self.current_stats = current_stats


    def getRestStats(self):

        rest_stats = []

        if self.weapon_scaling.getStrScaling() == 0:
            rest_stats.append("Str")
        if self.weapon_scaling.getDexScaling() == 0:
            rest_stats.append("Dex")
        if self.weapon_scaling.getIntScaling() == 0:
            rest_stats.append("Int")
        if self.weapon_scaling.getFaiScaling() == 0:
            rest_stats.append("Fai")
        if self.weapon_scaling.getArcScaling() == 0:
            rest_stats.append("Arc")

        return rest_stats


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
        rest_stats = self.getRestStats()
        rest_stat_string = ', '.join(f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
                         for stat in rest_stats)

        combination = Combination.Combination(stat_string,
                                              stat_sum, rest_stat_string,
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

        rest_stats = self.getRestStats()
        rest_stat_string = ', '.join(
            f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
            for stat in rest_stats)

        combination = Combination.Combination(stat_string,
                                              stat_sum, rest_stat_string,
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

        rest_stats = self.getRestStats()
        rest_stat_string = ', '.join(
            f"{stat}: {getattr(self.starting_class, f'getCurrent{stat}')()}"
            for stat in rest_stats)

        combination = Combination.Combination(stat_string,
                                              stat_sum, rest_stat_string,
                                              Calculator.calculateTotalDmg(self),
                                              self.weapon_passive.getPassiveType1(),
                                              self.weapon_passive.getPassiveType2(),
                                              Calculator.calcPassive1(self),
                                              Calculator.calcPassive2(self))

        return combination


    def getUsablePoints(self):


        scaling_points = (
                    self.current_stats[4] - self.starting_class.getMinStr() +
                    self.current_stats[5] - self.starting_class.getMinDex() +
                    self.current_stats[6] - self.starting_class.getMinInt() +
                    self.current_stats[7] - self.starting_class.getMinFai() +
                    self.current_stats[8] - self.starting_class.getMinArc())

        return (self.current_stats[0] -
                (self.current_stats[1] - self.starting_class.getMinVigor() +
                 self.current_stats[2] - self.starting_class.getMinMind() +
                 self.current_stats[3] - self.starting_class.getMinEndurance() +
                 self.current_stats[4] - self.starting_class.getMinStr() +
                 self.current_stats[5] - self.starting_class.getMinDex() +
                 self.current_stats[6] - self.starting_class.getMinInt() +
                 self.current_stats[7] - self.starting_class.getMinFai() +
                 self.current_stats[8] - self.starting_class.getMinArc()
                 + self.starting_class.getMinSoulLevel())
                 + scaling_points)





    def setCustomMinStats(self):

        a = (self.custom_min_stats[0] - self.starting_class.getMinVigor() +
             self.custom_min_stats[1] - self.starting_class.getMinMind() +
             self.custom_min_stats[2] - self.starting_class.getMinEndurance() +
             self.custom_min_stats[3] - self.starting_class.getMinStr() +
             self.custom_min_stats[4] - self.starting_class.getMinDex() +
             self.custom_min_stats[5] - self.starting_class.getMinInt() +
             self.custom_min_stats[6] - self.starting_class.getMinFai() +
             self.custom_min_stats[7] - self.starting_class.getMinArc())


        self.starting_class.setMinVigor(self.custom_min_stats[0])
        self.starting_class.setMinMind(self.custom_min_stats[1])
        self.starting_class.setMinEndurance(self.custom_min_stats[2])
        self.starting_class.setMinStr(self.custom_min_stats[3])
        self.starting_class.setMinDex(self.custom_min_stats[4])
        self.starting_class.setMinInt(self.custom_min_stats[5])
        self.starting_class.setMinFai(self.custom_min_stats[6])
        self.starting_class.setMinArc(self.custom_min_stats[7])

        return a

    def setCustomCurrentStats(self):

        self.starting_class.setCurrentVigor(self.custom_min_stats[0])
        self.starting_class.setCurrentMind(self.custom_min_stats[1])
        self.starting_class.setCurrentEndurance(self.custom_min_stats[2])
        self.starting_class.setCurrentStr(self.custom_min_stats[3])
        self.starting_class.setCurrentDex(self.custom_min_stats[4])
        self.starting_class.setCurrentInt(self.custom_min_stats[5])
        self.starting_class.setCurrentFai(self.custom_min_stats[6])
        self.starting_class.setCurrentArc(self.custom_min_stats[7])


    # def setCustomCurrentStats2(self):
    #
    #     self.starting_class.setCurrentSoulLevel(self.current_stats[0])
    #     self.starting_class.setCurrentVigor(self.current_stats[1])
    #     self.starting_class.setCurrentMind(self.current_stats[2])
    #     self.starting_class.setCurrentEndurance(self.current_stats[3])
    #     self.starting_class.setCurrentStr(self.current_stats[4])
    #     self.starting_class.setCurrentDex(self.current_stats[5])
    #     self.starting_class.setCurrentInt(self.current_stats[6])
    #     self.starting_class.setCurrentFai(self.current_stats[7])
    #     self.starting_class.setCurrentArc(self.current_stats[8])


    def optimize(self):

        diff = 0
        if self.use_custom_min_stats:
            diff = self.setCustomMinStats()



        value_list = []
        scaling_list = self.getScalingStats()
        #allocated_points = 70
        #self.setCustomCurrentStats()
        allocated_points = self.getUsablePoints() - diff

        if self.use_custom_min_stats:
            self.setCustomCurrentStats()


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
            value_list.append(self.createNewComb1(scaling_list))
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
            value_list.append(self.createNewComb1(scaling_list))
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
