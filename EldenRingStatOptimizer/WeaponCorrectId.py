
class WeaponCorrectId:
    def __init__(self, phys_calc_id, mag_calc_id, fire_calc_id, ligh_calc_id, holy_calc_id, attack_element_id):

        self.phys_calc_id = phys_calc_id
        self.mag_calc_id = mag_calc_id
        self.fire_calc_id = fire_calc_id
        self.ligh_calc_id = ligh_calc_id
        self.holy_calc_id = holy_calc_id
        self.attack_element_id = attack_element_id

    def getPhysCalcId(self):
        return self.phys_calc_id

    def getMagCalcId(self):
        return self.mag_calc_id

    def getFireCalcId(self):
        return self.fire_calc_id

    def getLighCalcId(self):
        return self.ligh_calc_id

    def getHolyCalcId(self):
        return self.holy_calc_id

    def getAttackElementId(self):
        return self.attack_element_id



