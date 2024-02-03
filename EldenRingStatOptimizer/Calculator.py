import AttackTypes


def calcPassiveArc(optimizer):
    if optimizer.starting_class.getCurrentArc() > 60:
        return (90 + 10 * ((optimizer.starting_class.getCurrentArc() - 60) / 39)) / 100
    elif optimizer.starting_class.getCurrentArc() > 45:
        return (75 + 15 * ((optimizer.starting_class.getCurrentArc() - 45) / 15)) / 100
    elif optimizer.starting_class.getCurrentArc() > 25:
        return (10 + 65 * ((optimizer.starting_class.getCurrentArc() - 25) / 20)) / 100
    else:
        return (10 * ((optimizer.starting_class.getCurrentArc() - 1) / 24)) / 100
    
    
def calcPassive2(optimizer):
    current_arc = optimizer.starting_class.getCurrentArc()
    required_arc = optimizer.weapon_extra_data.getRequiredArc()

    if current_arc >= required_arc:
        arc_req_met = 1
    else:
        arc_req_met = 0

    passive_type = optimizer.weapon_passive.getPassiveType2()
    passive_rotmadsleep_value = optimizer.weapon_passive.getRotMadSleepBase2()

    if optimizer.weapon_passive.getPassiveType2() == "":
        return 0

    if optimizer.weapon_scaling.getArcScaling() == 0:
        if passive_type in ["Scarlet Rot", "Madness", "Sleep"]:
            return passive_rotmadsleep_value
        else:
            return round(getattr(optimizer.weapon_passive, f'get{passive_type}Base2')(), 5)

    if arc_req_met == 0:
        if passive_type in ["Scarlet Rot", "Madness", "Sleep"]:
            passive2_value = passive_rotmadsleep_value * 0.6
        elif passive_type == "Frost":
            passive2_value = optimizer.weapon_passive.getFrostBase2() * 0.6
        elif passive_type == "Poison":
            passive2_value = optimizer.weapon_passive.getPoisonBase2() * 0.6
        elif passive_type == "Blood":
            passive2_value = optimizer.weapon_passive.getBloodBase2() * 0.6
        else:
            return 0

    else:
        if passive_type in ["Scarlet Rot", "Madness", "Sleep"]:
            passive2_value = passive_rotmadsleep_value
        elif passive_type == "Frost":
            passive2_value = optimizer.weapon_passive.getFrostBase1()
        elif passive_type == "Poison":
            if optimizer.weapon_scaling.getArcScaling() > 0:
                passive2_value = optimizer.weapon_scaling.getArcScaling() * calcPassiveArc(optimizer) * optimizer.weapon_passive.getPoisonBase2() + optimizer.weapon_passive.getPoisonBase2()
            else:
                passive2_value = optimizer.weapon_passive.getPoisonBase2()
        elif passive_type == "Blood":
            if optimizer.weapon_scaling.getArcScaling() > 0:
                passive2_value = optimizer.weapon_scaling.getArcScaling() * calcPassiveArc(optimizer) * optimizer.weapon_passive.getBloodBase2() + optimizer.weapon_passive.getBloodBase2()
            else:
                passive2_value = optimizer.weapon_passive.getBloodBase2()
        else:
            return 0

    return round(passive2_value, 5)


def calcPassive1(optimizer):
    current_arc = optimizer.starting_class.getCurrentArc()
    required_arc = optimizer.weapon_extra_data.getRequiredArc()

    if current_arc >= required_arc:
        arc_req_met = 1
    else:
        arc_req_met = 0

    passive_type = optimizer.weapon_passive.getPassiveType1()
    passive_rotmadsleep_value = optimizer.weapon_passive.getRotMadSleepBase1()

    if optimizer.weapon_passive.getPassiveType1() == "":
        return 0

    if optimizer.weapon_scaling.getArcScaling() == 0:
        if passive_type in ["Scarlet Rot", "Madness", "Sleep"]:
            return passive_rotmadsleep_value
        else:
            return round(getattr(optimizer.weapon_passive, f'get{passive_type}Base1')(), 5)

    if optimizer.weapon_extra_data.getName() in ["Poison Fingerprint Stone Shield", "Blood Fingerprint Stone Shield"]:
        if optimizer.weapon_scaling.getArcScaling() > 0:
            passive1_value = optimizer.weapon_scaling.getArcScaling() * calcPassiveArc(optimizer) * passive_rotmadsleep_value + passive_rotmadsleep_value
        else:
            passive1_value = passive_rotmadsleep_value, 5

    elif arc_req_met == 0:
        if passive_type in ["Scarlet Rot", "Madness", "Sleep"]:
            passive1_value = passive_rotmadsleep_value * 0.6
        elif passive_type == "Frost":
            passive1_value = optimizer.weapon_passive.getFrostBase1() * 0.6
        elif passive_type == "Poison":
            passive1_value = optimizer.weapon_passive.getPoisonBase1() * 0.6
        elif passive_type == "Blood":
            passive1_value = optimizer.weapon_passive.getBloodBase1() * 0.6
        else:
            return 0

    else:
        if passive_type in ["Scarlet Rot", "Madness", "Sleep"]:
            passive1_value = passive_rotmadsleep_value
        elif passive_type == "Frost":
            passive1_value = optimizer.weapon_passive.getFrostBase1()
        elif passive_type == "Poison":
            if optimizer.weapon_scaling.getArcScaling() > 0:
                passive1_value = optimizer.weapon_scaling.getArcScaling() * calcPassiveArc(optimizer) * optimizer.weapon_passive.getPoisonBase1() + optimizer.weapon_passive.getPoisonBase1()
            else:
                passive1_value = optimizer.weapon_passive.getPoisonBase1()
        elif passive_type == "Blood":
            if optimizer.weapon_scaling.getArcScaling() > 0:
                passive1_value = optimizer.weapon_scaling.getArcScaling() * calcPassiveArc(optimizer) * optimizer.weapon_passive.getBloodBase1() + optimizer.weapon_passive.getBloodBase1()
            else:
                passive1_value = optimizer.weapon_passive.getBloodBase1()
        else:
            return 0

    return round(passive1_value, 5)


def calculateTotalDmg(optimizer):
    str_req_met = int(
        optimizer.starting_class.getCurrentStr() >= optimizer.weapon_extra_data.getRequiredStr())
    dex_req_met = int(
        optimizer.starting_class.getCurrentDex() >= optimizer.weapon_extra_data.getRequiredDex())
    int_req_met = int(
        optimizer.starting_class.getCurrentInt() >= optimizer.weapon_extra_data.getRequiredInt())
    fai_req_met = int(
        optimizer.starting_class.getCurrentFai() >= optimizer.weapon_extra_data.getRequiredFai())
    arc_req_met = int(
        optimizer.starting_class.getCurrentArc() >= optimizer.weapon_extra_data.getRequiredArc())

    total_dmg = (AttackTypes.calcPhysDamage(optimizer, str_req_met, dex_req_met,
                                            int_req_met, fai_req_met,
                                            arc_req_met) + optimizer.weapon_attack.getPhysAttack() +
                 AttackTypes.calcMagDamage(optimizer, str_req_met, dex_req_met,
                                           int_req_met, fai_req_met,
                                           arc_req_met) + optimizer.weapon_attack.getMagAttack() +
                 AttackTypes.calcFireDamage(optimizer, str_req_met, dex_req_met,
                                            int_req_met, fai_req_met,
                                            arc_req_met) + optimizer.weapon_attack.getFireAttack() +
                 AttackTypes.calcLighDamage(optimizer, str_req_met, dex_req_met,
                                            int_req_met, fai_req_met,
                                            arc_req_met) + optimizer.weapon_attack.getLighAttack() +
                 AttackTypes.calcHolyDamage(optimizer, str_req_met, dex_req_met,
                                            int_req_met, fai_req_met,
                                            arc_req_met) + optimizer.weapon_attack.getHolyAttack())

    return round(total_dmg, 5)
