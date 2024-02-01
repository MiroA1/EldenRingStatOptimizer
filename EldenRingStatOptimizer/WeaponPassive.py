

class WeaponPassive:
    def __init__(self, passive_type1, passive_type2, rot_mad_sleep1, rot_mad_sleep2,
                 frost_base1, frost_base2, poison_base1, poison_base2, blood_base1, blood_base2):

        self.passive_type1 = passive_type1
        self.passive_type2 = passive_type2
        self.rot_mad_sleep1 = rot_mad_sleep1
        self.rot_mad_sleep2 = rot_mad_sleep2
        self.frost_base1 = frost_base1
        self.frost_base2 = frost_base2
        self.poison_base1 = poison_base1
        self.poison_base2 = poison_base2
        self.blood_base1 = blood_base1
        self.blood_base2 = blood_base2

    def getPassiveType1(self):
        return self.passive_type1

    def getPassiveType2(self):
        return self.passive_type2

    def getRotMadSleepBase1(self):
        return self.rot_mad_sleep1

    def getRotMadSleepBase2(self):
        return self.rot_mad_sleep2

    def getFrostBase1(self):
        return self.frost_base1

    def getFrostBase2(self):
        return self.frost_base2

    def getPoisonBase1(self):
        return self.poison_base1

    def getPoisonBase2(self):
        return self.poison_base2

    def getBloodBase1(self):
        return self.blood_base1

    def getBloodBase2(self):
        return self.blood_base2