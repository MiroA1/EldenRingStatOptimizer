
class WeaponAttack:
    def __init__(self, phys_attack, mag_attack, fire_attack, ligh_attack, holy_attack):

        self.phys_attack = phys_attack
        self.mag_attack = mag_attack
        self.fire_attack = fire_attack
        self.ligh_attack = ligh_attack
        self.holy_attack = holy_attack

    def getPhysAttack(self):
        return self.phys_attack

    def getMagAttack(self):
        return self.mag_attack

    def getFireAttack(self):
        return self.fire_attack

    def getLighAttack(self):
        return self.ligh_attack

    def getHolyAttack(self):
        return self.holy_attack

