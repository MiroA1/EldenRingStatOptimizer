
def calcCorrectStat_0(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 18:
        return 25 + 50 * (1 - (1 - (current_stat - 18) / 42) ** 1.2)
    else:
        return 25 * ((current_stat - 1) / 17) ** 1.2


def calcCorrectStat_1(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 20:
        return 35 + 40 * (1 - (1 - (current_stat - 20) / 40) ** 1.2)
    else:
        return 35 * ((current_stat - 1) / 19) ** 1.2


def calcCorrectStat_2(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 20:
        return 35 + 40 * (1 - (1 - (current_stat - 20) / 40) ** 1.2)
    else:
        return 35 * ((current_stat - 1) / 19) ** 1.2


def calcCorrectStat_4(current_stat):

    if current_stat > 80:
        return 95 + 5 * ((current_stat - 80) / 19)
    elif current_stat > 50:
        return 80 + 15 * ((current_stat - 50) / 30)
    elif current_stat > 20:
        return 40 + 40 * ((current_stat - 20) / 30)
    else:
        return 40 * ((current_stat - 1) / 19)


def calcCorrectStat_7(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 20:
        return 35 + 40 * (1 - (1 - (current_stat - 20) / 40) ** 1.2)
    else:
        return 35 * ((current_stat - 1) / 19) ** 1.2


def calcCorrectStat_8(current_stat):

    if current_stat > 80:
        return 90 + 20 * ((current_stat - 80) / 70)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 16:
        return 25 + 50 * (1 - (1 - (current_stat - 16) / 44) ** 1.2)
    else:
        return 25 * ((current_stat - 1) / 15) ** 1.2


def calcCorrectStat_12(current_stat):

    if current_stat > 45:
        return 75 + 25 * ((current_stat - 45) / 54)
    elif current_stat > 30:
        return 55 + 20 * ((current_stat - 30) / 15)
    elif current_stat > 15:
        return 10 + 45 * ((current_stat - 15) / 15)
    else:
        return 10 * ((current_stat - 1) / 14)


def calcCorrectStat_14(current_stat):

    if current_stat > 80:
        return 85 + 15 * ((current_stat - 80) / 19)
    elif current_stat > 40:
        return 60 + 25 * ((current_stat - 40) / 40)
    elif current_stat > 20:
        return 40 + 20 * ((current_stat - 20) / 20)
    else:
        return 40 * ((current_stat - 1) / 19)


def calcCorrectStat_15(current_stat):

    if current_stat > 80:
        return 95 + 5 * ((current_stat - 80) / 19)
    elif current_stat > 60:
        return 65 + 30 * ((current_stat - 60) / 20)
    elif current_stat > 25:
        return 25 + 40 * ((current_stat - 25) / 35)
    else:
        return 25 * ((current_stat - 1) / 24)


def calcCorrectStat_16(current_stat):

    if current_stat > 80:
        return 90 + 10 * ((current_stat - 80) / 19)
    elif current_stat > 60:
        return 75 + 15 * ((current_stat - 60) / 20)
    elif current_stat > 18:
        return 20 + 55 * ((current_stat - 18) / 42)
    else:
        return 20 * ((current_stat - 1) / 17)
