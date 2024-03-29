import SwitchFunctions


def calcPhysArcDamage(optimizer):
    if optimizer.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = optimizer.weapon_correct_id.getPhysCalcId()
        phys_arc_calc_correct = 0

        if optimizer.weapon_element_correct.getPhysScalesOnArc() == 0:
            phys_arc_calc_correct = 0
        elif phys_calc_id == 0:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 1:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 2:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 4:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 7:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 8:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 12:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 14:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 15:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentArc())
        elif phys_calc_id == 16:
            phys_arc_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentArc())

        return optimizer.weapon_attack.getPhysAttack() * optimizer.weapon_scaling.getArcScaling() * (
                phys_arc_calc_correct / 100)
    else:
        return 0


def calcPhysFaiDamage(optimizer):
    if optimizer.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = optimizer.weapon_correct_id.getPhysCalcId()
        phys_fai_calc_correct = 0

        if optimizer.weapon_element_correct.getPhysScalesOnFai() == 0:
            phys_fai_calc_correct = 0
        elif phys_calc_id == 0:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 1:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 2:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 4:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 7:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 8:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 12:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 14:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 15:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentFai())
        elif phys_calc_id == 16:
            phys_fai_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentFai())

        return optimizer.weapon_attack.getPhysAttack() * optimizer.weapon_scaling.getFaiScaling() * (
                phys_fai_calc_correct / 100)
    else:
        return 0


def calcPhysIntDamage(optimizer):
    if optimizer.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = optimizer.weapon_correct_id.getPhysCalcId()
        phys_int_calc_correct = 0

        if optimizer.weapon_element_correct.getPhysScalesOnInt() == 0:
            phys_int_calc_correct = 0
        elif phys_calc_id == 0:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 1:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 2:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 4:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 7:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 8:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 12:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 14:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 15:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentInt())
        elif phys_calc_id == 16:
            phys_int_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentInt())

        return optimizer.weapon_attack.getPhysAttack() * optimizer.weapon_scaling.getIntScaling() * (
                phys_int_calc_correct / 100)
    else:
        return 0


def calcPhysDexDamage(optimizer):
    if optimizer.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = optimizer.weapon_correct_id.getPhysCalcId()
        phys_dex_calc_correct = 0

        if optimizer.weapon_element_correct.getPhysScalesOnDex() == 0:
            phys_dex_calc_correct = 0
        elif phys_calc_id == 0:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 1:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 2:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 4:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 7:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 8:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 12:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 14:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 15:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentDex())
        elif phys_calc_id == 16:
            phys_dex_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentDex())

        return optimizer.weapon_attack.getPhysAttack() * optimizer.weapon_scaling.getDexScaling() * (
                phys_dex_calc_correct / 100)
    else:
        return 0


def calcPhysStrDamage(optimizer):
    if optimizer.weapon_attack.getPhysAttack() > 0:
        phys_calc_id = optimizer.weapon_correct_id.getPhysCalcId()
        phys_str_calc_correct = 0
        
        current_str = optimizer.starting_class.getCurrentStr()
        if optimizer.weapon_extra_data.getIs2Handing() == True:
            current_str = current_str * 1.5

        if optimizer.weapon_element_correct.getPhysScalesOnStr() == 0:
            phys_str_calc_correct = 0
        elif phys_calc_id == 0:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_0(
                current_str)
        elif phys_calc_id == 1:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_1(
                current_str)
        elif phys_calc_id == 2:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_2(
                current_str)
        elif phys_calc_id == 4:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_4(
                current_str)
        elif phys_calc_id == 7:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_7(
                current_str)
        elif phys_calc_id == 8:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_8(
                current_str)
        elif phys_calc_id == 12:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_12(
                current_str)
        elif phys_calc_id == 14:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_14(
                current_str)
        elif phys_calc_id == 15:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_15(
                current_str)
        elif phys_calc_id == 16:
            phys_str_calc_correct = SwitchFunctions.calcCorrectStat_16(
                current_str)

        return optimizer.weapon_attack.getPhysAttack() * optimizer.weapon_scaling.getStrScaling() * (
                phys_str_calc_correct / 100)
    else:
        return 0


def calcPhysDamage(optimizer, str_req_met, dex_req_met, int_req_met, fai_req_met,
                   arc_req_met):
    if optimizer.weapon_element_correct.getPhysScalesOnStr() == 1 and str_req_met == 0:
        phys_str_req_met = 0
    else:
        phys_str_req_met = 1

    if optimizer.weapon_element_correct.getPhysScalesOnDex() == 1 and dex_req_met == 0:
        phys_dex_req_met = 0
    else:
        phys_dex_req_met = 1

    if optimizer.weapon_element_correct.getPhysScalesOnInt() == 1 and int_req_met == 0:
        phys_int_req_met = 0
    else:
        phys_int_req_met = 1

    if optimizer.weapon_element_correct.getPhysScalesOnFai() == 1 and fai_req_met == 0:
        phys_fai_req_met = 0
    else:
        phys_fai_req_met = 1

    if optimizer.weapon_element_correct.getPhysScalesOnArc() == 1 and arc_req_met == 0:
        phys_arc_req_met = 0
    else:
        phys_arc_req_met = 1

    if phys_str_req_met + phys_dex_req_met + phys_int_req_met + phys_fai_req_met + phys_arc_req_met == 5:
        phys_req_met = 1
    else:
        phys_req_met = 0

    if phys_req_met == 0:
        return optimizer.weapon_attack.getPhysAttack() * (-0.4)
    else:
        return (calcPhysStrDamage(optimizer) +
                calcPhysDexDamage(optimizer) +
                calcPhysIntDamage(optimizer) +
                calcPhysFaiDamage(optimizer) +
                calcPhysArcDamage(optimizer))


def calcMagArcDamage(optimizer):
    if optimizer.weapon_attack.getMagAttack() > 0:
        mag_calc_id = optimizer.weapon_correct_id.getMagCalcId()
        mag_arc_calc_correct = 0

        if optimizer.weapon_element_correct.getMagScalesOnArc() == 0:
            mag_arc_calc_correct = 0
        elif mag_calc_id == 0:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 1:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 2:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 4:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 7:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 8:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 12:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 14:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 15:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentArc())
        elif mag_calc_id == 16:
            mag_arc_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentArc())

        return optimizer.weapon_attack.getMagAttack() * optimizer.weapon_scaling.getArcScaling() * (
                mag_arc_calc_correct / 100)
    else:
        return 0


def calcMagFaiDamage(optimizer):
    if optimizer.weapon_attack.getMagAttack() > 0:
        mag_calc_id = optimizer.weapon_correct_id.getMagCalcId()
        mag_fai_calc_correct = 0

        if optimizer.weapon_element_correct.getMagScalesOnFai() == 0:
            mag_fai_calc_correct = 0
        elif mag_calc_id == 0:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 1:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 2:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 4:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 7:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 8:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 12:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 14:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 15:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentFai())
        elif mag_calc_id == 16:
            mag_fai_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentFai())

        return optimizer.weapon_attack.getMagAttack() * optimizer.weapon_scaling.getFaiScaling() * (
                mag_fai_calc_correct / 100)
    else:
        return 0


def calcMagIntDamage(optimizer):
    if optimizer.weapon_attack.getMagAttack() > 0:
        mag_calc_id = optimizer.weapon_correct_id.getMagCalcId()
        mag_int_calc_correct = 0

        if optimizer.weapon_element_correct.getMagScalesOnInt() == 0:
            mag_int_calc_correct = 0
        elif mag_calc_id == 0:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 1:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 2:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 4:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 7:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 8:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 12:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 14:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 15:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentInt())
        elif mag_calc_id == 16:
            mag_int_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentInt())

        return optimizer.weapon_attack.getMagAttack() * optimizer.weapon_scaling.getIntScaling() * (
                mag_int_calc_correct / 100)
    else:
        return 0


def calcMagDexDamage(optimizer):
    if optimizer.weapon_attack.getMagAttack() > 0:
        mag_calc_id = optimizer.weapon_correct_id.getMagCalcId()
        mag_dex_calc_correct = 0

        if optimizer.weapon_element_correct.getMagScalesOnDex() == 0:
            mag_dex_calc_correct = 0
        elif mag_calc_id == 0:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 1:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 2:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 4:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 7:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 8:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 12:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 14:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 15:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentDex())
        elif mag_calc_id == 16:
            mag_dex_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentDex())

        return optimizer.weapon_attack.getMagAttack() * optimizer.weapon_scaling.getDexScaling() * (
                mag_dex_calc_correct / 100)
    else:
        return 0


def calcMagStrDamage(optimizer):
    if optimizer.weapon_attack.getMagAttack() > 0:
        mag_calc_id = optimizer.weapon_correct_id.getMagCalcId()
        mag_str_calc_correct = 0

        current_str = optimizer.starting_class.getCurrentStr()
        if optimizer.weapon_extra_data.getIs2Handing() == True:
            current_str = current_str * 1.5

        if optimizer.weapon_element_correct.getMagScalesOnStr() == 0:
            mag_str_calc_correct = 0
        elif mag_calc_id == 0:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_0(
                current_str)
        elif mag_calc_id == 1:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_1(
                current_str)
        elif mag_calc_id == 2:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_2(
                current_str)
        elif mag_calc_id == 4:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_4(
                current_str)
        elif mag_calc_id == 7:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_7(
                current_str)
        elif mag_calc_id == 8:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_8(
                current_str)
        elif mag_calc_id == 12:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_12(
                current_str)
        elif mag_calc_id == 14:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_14(
                current_str)
        elif mag_calc_id == 15:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_15(
                current_str)
        elif mag_calc_id == 16:
            mag_str_calc_correct = SwitchFunctions.calcCorrectStat_16(
                current_str)

        return optimizer.weapon_attack.getMagAttack() * optimizer.weapon_scaling.getStrScaling() * (
                mag_str_calc_correct / 100)
    else:
        return 0


def calcMagDamage(optimizer, str_req_met, dex_req_met, int_req_met, fai_req_met,
                  arc_req_met):

    if optimizer.weapon_element_correct.getMagScalesOnStr() == 1 and str_req_met == 0:
        mag_str_req_met = 0
    else:
        mag_str_req_met = 1

    if optimizer.weapon_element_correct.getMagScalesOnDex() == 1 and dex_req_met == 0:
        mag_dex_req_met = 0
    else:
        mag_dex_req_met = 1

    if optimizer.weapon_element_correct.getMagScalesOnInt() == 1 and int_req_met == 0:
        mag_int_req_met = 0
    else:
        mag_int_req_met = 1

    if optimizer.weapon_element_correct.getMagScalesOnFai() == 1 and fai_req_met == 0:
        mag_fai_req_met = 0
    else:
        mag_fai_req_met = 1

    if optimizer.weapon_element_correct.getMagScalesOnArc() == 1 and arc_req_met == 0:
        mag_arc_req_met = 0
    else:
        mag_arc_req_met = 1

    if mag_str_req_met + mag_dex_req_met + mag_int_req_met + mag_fai_req_met + mag_arc_req_met == 5:
        mag_req_met = 1
    else:
        mag_req_met = 0

    if mag_req_met == 0:
        return optimizer.weapon_attack.getMagAttack() * (-0.4)
    else:
        return (calcMagStrDamage(optimizer) +
                calcMagDexDamage(optimizer) +
                calcMagIntDamage(optimizer) +
                calcMagFaiDamage(optimizer) +
                calcMagArcDamage(optimizer))


def calcFireArcDamage(optimizer):
    if optimizer.weapon_attack.getFireAttack() > 0:
        fire_calc_id = optimizer.weapon_correct_id.getFireCalcId()
        fire_arc_calc_correct = 0

        if optimizer.weapon_element_correct.getFireScalesOnArc() == 0:
            fire_arc_calc_correct = 0
        elif fire_calc_id == 0:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 1:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 2:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 4:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 7:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 8:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 12:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 14:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 15:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentArc())
        elif fire_calc_id == 16:
            fire_arc_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentArc())

        return optimizer.weapon_attack.getFireAttack() * optimizer.weapon_scaling.getArcScaling() * (
                fire_arc_calc_correct / 100)
    else:
        return 0


def calcFireFaiDamage(optimizer):
    if optimizer.weapon_attack.getFireAttack() > 0:
        fire_calc_id = optimizer.weapon_correct_id.getFireCalcId()
        fire_fai_calc_correct = 0

        if optimizer.weapon_element_correct.getFireScalesOnFai() == 0:
            fire_fai_calc_correct = 0
        elif fire_calc_id == 0:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 1:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 2:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 4:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 7:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 8:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 12:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 14:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 15:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentFai())
        elif fire_calc_id == 16:
            fire_fai_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentFai())

        return optimizer.weapon_attack.getFireAttack() * optimizer.weapon_scaling.getFaiScaling() * (
                fire_fai_calc_correct / 100)
    else:
        return 0


def calcFireIntDamage(optimizer):
    if optimizer.weapon_attack.getFireAttack() > 0:
        fire_calc_id = optimizer.weapon_correct_id.getFireCalcId()
        fire_int_calc_correct = 0

        if optimizer.weapon_element_correct.getFireScalesOnInt() == 0:
            fire_int_calc_correct = 0
        elif fire_calc_id == 0:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 1:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 2:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 4:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 7:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 8:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 12:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 14:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 15:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentInt())
        elif fire_calc_id == 16:
            fire_int_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentInt())

        return optimizer.weapon_attack.getFireAttack() * optimizer.weapon_scaling.getIntScaling() * (
                fire_int_calc_correct / 100)
    else:
        return 0


def calcFireDexDamage(optimizer):
    if optimizer.weapon_attack.getFireAttack() > 0:
        fire_calc_id = optimizer.weapon_correct_id.getFireCalcId()
        fire_dex_calc_correct = 0

        if optimizer.weapon_element_correct.getFireScalesOnDex() == 0:
            fire_dex_calc_correct = 0
        elif fire_calc_id == 0:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 1:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 2:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 4:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 7:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 8:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 12:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 14:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 15:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentDex())
        elif fire_calc_id == 16:
            fire_dex_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentDex())

        return optimizer.weapon_attack.getFireAttack() * optimizer.weapon_scaling.getDexScaling() * (
                fire_dex_calc_correct / 100)
    else:
        return 0


def calcFireStrDamage(optimizer):
    if optimizer.weapon_attack.getFireAttack() > 0:
        fire_calc_id = optimizer.weapon_correct_id.getFireCalcId()
        fire_str_calc_correct = 0

        current_str = optimizer.starting_class.getCurrentStr()
        if optimizer.weapon_extra_data.getIs2Handing() == True:
            current_str = current_str * 1.5

        if optimizer.weapon_element_correct.getFireScalesOnStr() == 0:
            fire_str_calc_correct = 0
        elif fire_calc_id == 0:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_0(
                current_str)
        elif fire_calc_id == 1:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_1(
                current_str)
        elif fire_calc_id == 2:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_2(
                current_str)
        elif fire_calc_id == 4:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_4(
                current_str)
        elif fire_calc_id == 7:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_7(
                current_str)
        elif fire_calc_id == 8:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_8(
                current_str)
        elif fire_calc_id == 12:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_12(
                current_str)
        elif fire_calc_id == 14:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_14(
                current_str)
        elif fire_calc_id == 15:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_15(
                current_str)
        elif fire_calc_id == 16:
            fire_str_calc_correct = SwitchFunctions.calcCorrectStat_16(
                current_str)

        return optimizer.weapon_attack.getFireAttack() * optimizer.weapon_scaling.getStrScaling() * (
                fire_str_calc_correct / 100)
    else:
        return 0


def calcFireDamage(optimizer, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met):

    if optimizer.weapon_element_correct.getFireScalesOnStr() == 1 and str_req_met == 0:
        fire_str_req_met = 0
    else:
        fire_str_req_met = 1

    if optimizer.weapon_element_correct.getFireScalesOnDex() == 1 and dex_req_met == 0:
        fire_dex_req_met = 0
    else:
        fire_dex_req_met = 1

    if optimizer.weapon_element_correct.getFireScalesOnInt() == 1 and int_req_met == 0:
        fire_int_req_met = 0
    else:
        fire_int_req_met = 1

    if optimizer.weapon_element_correct.getFireScalesOnFai() == 1 and fai_req_met == 0:
        fire_fai_req_met = 0
    else:
        fire_fai_req_met = 1

    if optimizer.weapon_element_correct.getFireScalesOnArc() == 1 and arc_req_met == 0:
        fire_arc_req_met = 0
    else:
        fire_arc_req_met = 1

    if fire_str_req_met + fire_dex_req_met + fire_int_req_met + fire_fai_req_met + fire_arc_req_met == 5:
        fire_req_met = 1
    else:
        fire_req_met = 0

    if fire_req_met == 0:
        return optimizer.weapon_attack.getFireAttack() * (-0.4)
    else:
        return (calcFireStrDamage(optimizer) +
                calcFireDexDamage(optimizer) +
                calcFireIntDamage(optimizer) +
                calcFireFaiDamage(optimizer) +
                calcFireArcDamage(optimizer))


def calcLighArcDamage(optimizer):
    if optimizer.weapon_attack.getLighAttack() > 0:
        ligh_calc_id = optimizer.weapon_correct_id.getLighCalcId()
        ligh_arc_calc_correct = 0

        if optimizer.weapon_element_correct.getLighScalesOnArc() == 0:
            ligh_arc_calc_correct = 0
        elif ligh_calc_id == 0:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 1:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 2:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 4:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 7:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 8:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 12:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 14:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 15:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentArc())
        elif ligh_calc_id == 16:
            ligh_arc_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentArc())

        return optimizer.weapon_attack.getLighAttack() * optimizer.weapon_scaling.getArcScaling() * (
                ligh_arc_calc_correct / 100)
    else:
        return 0


def calcLighFaiDamage(optimizer):
    if optimizer.weapon_attack.getLighAttack() > 0:
        ligh_calc_id = optimizer.weapon_correct_id.getLighCalcId()
        ligh_fai_calc_correct = 0

        if optimizer.weapon_element_correct.getLighScalesOnFai() == 0:
            ligh_fai_calc_correct = 0
        elif ligh_calc_id == 0:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 1:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 2:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 4:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 7:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 8:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 12:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 14:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 15:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentFai())
        elif ligh_calc_id == 16:
            ligh_fai_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentFai())

        return optimizer.weapon_attack.getLighAttack() * optimizer.weapon_scaling.getFaiScaling() * (
                ligh_fai_calc_correct / 100)
    else:
        return 0


def calcLighIntDamage(optimizer):
    if optimizer.weapon_attack.getLighAttack() > 0:
        ligh_calc_id = optimizer.weapon_correct_id.getLighCalcId()
        ligh_int_calc_correct = 0

        if optimizer.weapon_element_correct.getLighScalesOnInt() == 0:
            ligh_int_calc_correct = 0
        elif ligh_calc_id == 0:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 1:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 2:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 4:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 7:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 8:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 12:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 14:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 15:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentInt())
        elif ligh_calc_id == 16:
            ligh_int_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentInt())

        return optimizer.weapon_attack.getLighAttack() * optimizer.weapon_scaling.getIntScaling() * (
                ligh_int_calc_correct / 100)
    else:
        return 0


def calcLighDexDamage(optimizer):
    if optimizer.weapon_attack.getLighAttack() > 0:
        ligh_calc_id = optimizer.weapon_correct_id.getLighCalcId()
        ligh_dex_calc_correct = 0

        if optimizer.weapon_element_correct.getLighScalesOnDex() == 0:
            ligh_dex_calc_correct = 0
        elif ligh_calc_id == 0:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 1:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 2:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 4:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 7:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 8:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 12:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 14:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 15:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentDex())
        elif ligh_calc_id == 16:
            ligh_dex_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentDex())

        return optimizer.weapon_attack.getLighAttack() * optimizer.weapon_scaling.getDexScaling() * (
                ligh_dex_calc_correct / 100)
    else:
        return 0


def calcLighStrDamage(optimizer):
    if optimizer.weapon_attack.getLighAttack() > 0:
        ligh_calc_id = optimizer.weapon_correct_id.getLighCalcId()
        ligh_str_calc_correct = 0

        current_str = optimizer.starting_class.getCurrentStr()
        if optimizer.weapon_extra_data.getIs2Handing() == True:
            current_str = current_str * 1.5

        if optimizer.weapon_element_correct.getLighScalesOnStr() == 0:
            ligh_str_calc_correct = 0
        elif ligh_calc_id == 0:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_0(
                current_str)
        elif ligh_calc_id == 1:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_1(
                current_str)
        elif ligh_calc_id == 2:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_2(
                current_str)
        elif ligh_calc_id == 4:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_4(
                current_str)
        elif ligh_calc_id == 7:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_7(
                current_str)
        elif ligh_calc_id == 8:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_8(
                current_str)
        elif ligh_calc_id == 12:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_12(
                current_str)
        elif ligh_calc_id == 14:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_14(
                current_str)
        elif ligh_calc_id == 15:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_15(
                current_str)
        elif ligh_calc_id == 16:
            ligh_str_calc_correct = SwitchFunctions.calcCorrectStat_16(
                current_str)

        return optimizer.weapon_attack.getLighAttack() * optimizer.weapon_scaling.getStrScaling() * (
                ligh_str_calc_correct / 100)
    else:
        return 0


def calcLighDamage(optimizer, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met):

    if optimizer.weapon_element_correct.getLighScalesOnStr() == 1 and str_req_met == 0:
        ligh_str_req_met = 0
    else:
        ligh_str_req_met = 1

    if optimizer.weapon_element_correct.getLighScalesOnDex() == 1 and dex_req_met == 0:
        ligh_dex_req_met = 0
    else:
        ligh_dex_req_met = 1

    if optimizer.weapon_element_correct.getLighScalesOnInt() == 1 and int_req_met == 0:
        ligh_int_req_met = 0
    else:
        ligh_int_req_met = 1

    if optimizer.weapon_element_correct.getLighScalesOnFai() == 1 and fai_req_met == 0:
        ligh_fai_req_met = 0
    else:
        ligh_fai_req_met = 1

    if optimizer.weapon_element_correct.getLighScalesOnArc() == 1 and arc_req_met == 0:
        ligh_arc_req_met = 0
    else:
        ligh_arc_req_met = 1

    if ligh_str_req_met + ligh_dex_req_met + ligh_int_req_met + ligh_fai_req_met + ligh_arc_req_met == 5:
        ligh_req_met = 1
    else:
        ligh_req_met = 0

    if ligh_req_met == 0:
        return optimizer.weapon_attack.getLighAttack() * (-0.4)
    else:
        return (calcLighStrDamage(optimizer) +
                calcLighDexDamage(optimizer) +
                calcLighIntDamage(optimizer) +
                calcLighFaiDamage(optimizer) +
                calcLighArcDamage(optimizer))


def calcHolyArcDamage(optimizer):
    if optimizer.weapon_attack.getHolyAttack() > 0:
        holy_calc_id = optimizer.weapon_correct_id.getHolyCalcId()
        holy_arc_calc_correct = 0

        if optimizer.weapon_element_correct.getHolyScalesOnArc() == 0:
            holy_arc_calc_correct = 0
        elif holy_calc_id == 0:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 1:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 2:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 4:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 7:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 8:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 12:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 14:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 15:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentArc())
        elif holy_calc_id == 16:
            holy_arc_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentArc())

        return optimizer.weapon_attack.getHolyAttack() * optimizer.weapon_scaling.getArcScaling() * (
                holy_arc_calc_correct / 100)
    else:
        return 0


def calcHolyFaiDamage(optimizer):
    if optimizer.weapon_attack.getHolyAttack() > 0:
        holy_calc_id = optimizer.weapon_correct_id.getHolyCalcId()
        holy_fai_calc_correct = 0

        if optimizer.weapon_element_correct.getHolyScalesOnFai() == 0:
            holy_fai_calc_correct = 0
        elif holy_calc_id == 0:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 1:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 2:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 4:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 7:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 8:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 12:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 14:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 15:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentFai())
        elif holy_calc_id == 16:
            holy_fai_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentFai())

        return optimizer.weapon_attack.getHolyAttack() * optimizer.weapon_scaling.getFaiScaling() * (
                holy_fai_calc_correct / 100)
    else:
        return 0


def calcHolyIntDamage(optimizer):
    if optimizer.weapon_attack.getHolyAttack() > 0:
        holy_calc_id = optimizer.weapon_correct_id.getHolyCalcId()
        holy_int_calc_correct = 0

        if optimizer.weapon_element_correct.getHolyScalesOnInt() == 0:
            holy_int_calc_correct = 0
        elif holy_calc_id == 0:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 1:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 2:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 4:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 7:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 8:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 12:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 14:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 15:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentInt())
        elif holy_calc_id == 16:
            holy_int_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentInt())

        return optimizer.weapon_attack.getHolyAttack() * optimizer.weapon_scaling.getIntScaling() * (
                holy_int_calc_correct / 100)
    else:
        return 0


def calcHolyDexDamage(optimizer):
    if optimizer.weapon_attack.getHolyAttack() > 0:
        holy_calc_id = optimizer.weapon_correct_id.getHolyCalcId()
        holy_dex_calc_correct = 0

        if optimizer.weapon_element_correct.getHolyScalesOnDex() == 0:
            holy_dex_calc_correct = 0
        elif holy_calc_id == 0:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_0(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 1:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_1(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 2:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_2(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 4:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_4(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 7:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_7(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 8:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_8(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 12:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_12(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 14:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_14(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 15:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_15(
                optimizer.starting_class.getCurrentDex())
        elif holy_calc_id == 16:
            holy_dex_calc_correct = SwitchFunctions.calcCorrectStat_16(
                optimizer.starting_class.getCurrentDex())

        return optimizer.weapon_attack.getHolyAttack() * optimizer.weapon_scaling.getDexScaling() * (
                holy_dex_calc_correct / 100)
    else:
        return 0


def calcHolyStrDamage(optimizer):
    if optimizer.weapon_attack.getHolyAttack() > 0:
        holy_calc_id = optimizer.weapon_correct_id.getHolyCalcId()
        holy_str_calc_correct = 0

        current_str = optimizer.starting_class.getCurrentStr()
        if optimizer.weapon_extra_data.getIs2Handing() == True:
            current_str = current_str * 1.5

        if optimizer.weapon_element_correct.getHolyScalesOnStr() == 0:
            holy_str_calc_correct = 0
        elif holy_calc_id == 0:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_0(
                current_str)
        elif holy_calc_id == 1:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_1(
                current_str)
        elif holy_calc_id == 2:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_2(
                current_str)
        elif holy_calc_id == 4:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_4(
                current_str)
        elif holy_calc_id == 7:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_7(
                current_str)
        elif holy_calc_id == 8:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_8(
                current_str)
        elif holy_calc_id == 12:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_12(
                current_str)
        elif holy_calc_id == 14:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_14(
                current_str)
        elif holy_calc_id == 15:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_15(
                current_str)
        elif holy_calc_id == 16:
            holy_str_calc_correct = SwitchFunctions.calcCorrectStat_16(
                current_str)

        return optimizer.weapon_attack.getHolyAttack() * optimizer.weapon_scaling.getStrScaling() * (
                holy_str_calc_correct / 100)
    else:
        return 0


def calcHolyDamage(optimizer, str_req_met, dex_req_met, int_req_met, fai_req_met, arc_req_met):

    if optimizer.weapon_element_correct.getHolyScalesOnStr() == 1 and str_req_met == 0:
        holy_str_req_met = 0
    else:
        holy_str_req_met = 1

    if optimizer.weapon_element_correct.getHolyScalesOnDex() == 1 and dex_req_met == 0:
        holy_dex_req_met = 0
    else:
        holy_dex_req_met = 1

    if optimizer.weapon_element_correct.getHolyScalesOnInt() == 1 and int_req_met == 0:
        holy_int_req_met = 0
    else:
        holy_int_req_met = 1

    if optimizer.weapon_element_correct.getHolyScalesOnFai() == 1 and fai_req_met == 0:
        holy_fai_req_met = 0
    else:
        holy_fai_req_met = 1

    if optimizer.weapon_element_correct.getHolyScalesOnArc() == 1 and arc_req_met == 0:
        holy_arc_req_met = 0
    else:
        holy_arc_req_met = 1

    if holy_str_req_met + holy_dex_req_met + holy_int_req_met + holy_fai_req_met + holy_arc_req_met == 5:
        holy_req_met = 1
    else:
        holy_req_met = 0

    if holy_req_met == 0:
        return optimizer.weapon_attack.getHolyAttack() * (-0.4)
    else:
        return (calcHolyStrDamage(optimizer) +
                calcHolyDexDamage(optimizer) +
                calcHolyIntDamage(optimizer) +
                calcHolyFaiDamage(optimizer) +
                calcHolyArcDamage(optimizer))
