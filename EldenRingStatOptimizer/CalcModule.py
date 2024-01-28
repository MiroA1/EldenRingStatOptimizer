import SwitchFunctions


def calcPhysArcDamage(self):
    
    if self.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = self.weapon_correct_id.getPhysCalcId()
        phys_arc_calc_correct = 0

        if self.weapon_element_correct.getPhysScalesOnArc() == 0:
            phys_arc_calc_correct = 0
        elif phys_calc_id == 0:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_0(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 1:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_1(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 2:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_2(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 4:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_4(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 7:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_7(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 8:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_8(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 12:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_12(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 14:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_14(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 15:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_15(
                self.starting_class.getCurrentArc())
        elif phys_calc_id == 16:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_16(
                self.starting_class.getCurrentArc())

        return self.weapon_attack.getPhysAttack() * self.weapon_scaling.getArcScaling() * (
                phys_arc_calc_correct / 100)
    else:
        return 0


def calcPhysFaithDamage(self):

    if self.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = self.weapon_correct_id.getPhysCalcId()
        phys_fai_calc_correct = 0

        if self.weapon_element_correct.getPhysScalesOnFai() == 0:
            phys_fai_calc_correct = 0
        elif phys_calc_id == 0:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_0(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 1:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_1(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 2:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_2(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 4:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_4(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 7:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_7(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 8:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_8(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 12:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_12(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 14:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_14(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 15:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_15(
                self.starting_class.getCurrentFai())
        elif phys_calc_id == 16:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_16(
                self.starting_class.getCurrentFai())

        return self.weapon_attack.getPhysAttack() * self.weapon_scaling.getFaiScaling() * (
                phys_fai_calc_correct / 100)
    else:
        return 0


def calcPhysIntDamage(self):
    if self.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = self.weapon_correct_id.getPhysCalcId()
        phys_int_calc_correct = 0

        if self.weapon_element_correct.getPhysScalesOnInt() == 0:
            phys_int_calc_correct = 0
        elif phys_calc_id == 0:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_0(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 1:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_1(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 2:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_2(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 4:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_4(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 7:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_7(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 8:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_8(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 12:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_12(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 14:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_14(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 15:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_15(
                self.starting_class.getCurrentInt())
        elif phys_calc_id == 16:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_16(
                self.starting_class.getCurrentInt())

        return self.weapon_attack.getPhysAttack() * self.weapon_scaling.getIntScaling() * (
                phys_int_calc_correct / 100)
    else:
        return 0


def calcPhysDexDamage(self):
    if self.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = self.weapon_correct_id.getPhysCalcId()
        phys_dex_calc_correct = 0

        if self.weapon_element_correct.getPhysScalesOnDex() == 0:
            phys_dex_calc_correct = 0
        elif phys_calc_id == 0:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_0(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 1:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_1(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 2:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_2(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 4:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_4(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 7:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_7(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 8:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_8(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 12:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_12(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 14:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_14(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 15:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_15(
                self.starting_class.getCurrentDex())
        elif phys_calc_id == 16:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_16(
                self.starting_class.getCurrentDex())

        return self.weapon_attack.getPhysAttack() * self.weapon_scaling.getDexScaling() * (
                phys_dex_calc_correct / 100)
    else:
        return 0


def calcPhysStrDamage(self):
    if self.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = self.weapon_correct_id.getPhysCalcId()
        phys_str_calc_correct = 0

        if self.weapon_element_correct.getPhysScalesOnStr() == 0:
            phys_str_calc_correct = 0
        elif phys_calc_id == 0:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_0(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 1:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_1(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 2:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_2(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 4:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_4(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 7:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_7(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 8:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_8(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 12:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_12(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 14:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_14(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 15:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_15(
                self.starting_class.getCurrentStr())
        elif phys_calc_id == 16:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_16(
                self.starting_class.getCurrentStr())

        return self.weapon_attack.getPhysAttack() * self.weapon_scaling.getStrScaling() * (
                phys_str_calc_correct / 100)
    else:
        return 0


def calcPhysDamage(self):
    if self.starting_class.getCurrentStr() < self.weapon.required_str():
        str_req_met = 0
    else:
        str_req_met = 1

    if self.starting_class.getCurrentDex() < self.weapon.required_dex():
        dex_req_met = 0
    else:
        dex_req_met = 1

    if self.starting_class.getCurrentInt() < self.weapon.required_int():
        int_req_met = 0
    else:
        int_req_met = 1

    if self.starting_class.getCurrentFai() < self.weapon.required_fai():
        fai_req_met = 0
    else:
        fai_req_met = 1

    if self.starting_class.getCurrentArc() < self.weapon.required_arc():
        arc_req_met = 0
    else:
        arc_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnStr() == 1 and str_req_met == 0:
        phys_str_req_met = 0
    else:
        phys_str_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnDex() == 1 and dex_req_met == 0:
        phys_dex_req_met = 0
    else:
        phys_dex_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnInt() == 1 and int_req_met == 0:
        phys_int_req_met = 0
    else:
        phys_int_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnFai() == 1 and fai_req_met == 0:
        phys_fai_req_met = 0
    else:
        phys_fai_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnArc() == 1 and arc_req_met == 0:
        phys_arc_req_met = 0
    else:
        phys_arc_req_met = 1

    if phys_str_req_met + phys_dex_req_met + phys_int_req_met + phys_fai_req_met + phys_arc_req_met == 5:
        phys_req_met = 1
    else:
        phys_req_met = 0

    if phys_req_met == 0:
        return self.weapon_attack.getPhysAttack() * (-0.4)
    else:
        return (self.calcPhysStrDamage() +
                self.calcPhysDexDamage() +
                self.calcPhysIntDamage() +
                self.calcPhysFaiDamage() +
                self.calcPhysArcDamage())


def calcMagStrDamage(self):
    phys_calc_id = self.weapon_correct_id.getPhysCalcId()
    str_scale = 0

    if self.weapon_element_correct.getPhysScalesOnStr() == 0:
        return 0
    elif phys_calc_id == 0:
        str_scale = SwitchFunctions.calcCorrectStat_0(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 1:
        str_scale = SwitchFunctions.calcCorrectStat_1(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 2:
        str_scale = SwitchFunctions.calcCorrectStat_2(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 4:
        str_scale = SwitchFunctions.calcCorrectStat_4(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 7:
        str_scale = SwitchFunctions.calcCorrectStat_7(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 8:
        str_scale = SwitchFunctions.calcCorrectStat_8(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 12:
        str_scale = SwitchFunctions.calcCorrectStat_12(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 14:
        str_scale = SwitchFunctions.calcCorrectStat_14(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 15:
        str_scale = SwitchFunctions.calcCorrectStat_15(
            self.starting_class.getCurrentStr())
    elif phys_calc_id == 16:
        str_scale = SwitchFunctions.calcCorrectStat_16(
            self.starting_class.getCurrentStr())

    self.weapon_attack.getPhysAttack() * self.weapon_scaling.getStrScaling() * (
            str_scale / 100)


def calcMagDamage(self):
    if self.starting_class.getCurrentStr() < self.weapon.required_str():
        str_req_met = 0
    else:
        str_req_met = 1

    if self.starting_class.getCurrentDex() < self.weapon.required_dex():
        dex_req_met = 0
    else:
        dex_req_met = 1

    if self.starting_class.getCurrentInt() < self.weapon.required_int():
        int_req_met = 0
    else:
        int_req_met = 1

    if self.starting_class.getCurrentFai() < self.weapon.required_fai():
        fai_req_met = 0
    else:
        fai_req_met = 1

    if self.starting_class.getCurrentArc() < self.weapon.required_arc():
        arc_req_met = 0
    else:
        arc_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnStr() == 1 and str_req_met == 0:
        phys_str_req_met = 0
    else:
        phys_str_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnDex() == 1 and dex_req_met == 0:
        phys_dex_req_met = 0
    else:
        phys_dex_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnInt() == 1 and int_req_met == 0:
        phys_int_req_met = 0
    else:
        phys_int_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnFai() == 1 and fai_req_met == 0:
        phys_fai_req_met = 0
    else:
        phys_fai_req_met = 1

    if self.weapon_element_correct.getPhysScalesOnArc() == 1 and arc_req_met == 0:
        phys_arc_req_met = 0
    else:
        phys_arc_req_met = 1

    if phys_str_req_met + phys_dex_req_met + phys_int_req_met + phys_fai_req_met + phys_arc_req_met == 5:
        phys_req_met = 1
    else:
        phys_req_met = 0

    if phys_req_met == 0:
        return self.weapon_attack.getPhysAttack() * (-0.4)
    else:
        return (self.calcPhysStrDamage() +
                self.calcPhysDexDamage() +
                self.calcPhysIntDamage() +
                self.calcPhysFaiDamage() +
                self.calcPhysArcDamage())
