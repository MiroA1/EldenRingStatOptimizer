
class Weapon:
    def __init__(self, name, upgrade_level, required_str, required_dex, required_int, required_fai, required_arc,
                 two_hand_bonus, weapon_type, is_2handing):

        self.name = name
        self.upgrade_level = upgrade_level
        self.required_str = required_str
        self.required_dex = required_dex
        self.required_int = required_int
        self.required_fai = required_fai
        self.required_arc = required_arc
        self.two_hand_bonus = two_hand_bonus
        self.weapon_type = weapon_type
        self.is_2handing = is_2handing


    def getName(self):
        return self.name

    def getUpgradeLevel(self):
        return self.upgrade_level

    def getRequiredStr(self):
        return self.required_str

    def getRequiredDex(self):
        return self.required_dex

    def getRequiredInt(self):
        return self.required_int

    def getRequiredFai(self):
        return self.required_fai

    def getRequiredArc(self):
        return self.required_arc

    def getTwoHandBonus(self):
        return self.two_hand_bonus

    def getWeaponType(self):
        return self.weapon_type

    def getIs2handing(self):
        return self.is_2handing



