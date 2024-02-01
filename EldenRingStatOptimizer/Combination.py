
class Combination:

    def __init__(self, stats, total_dmg, passive1, passive2, passive1_value, passive2_value):

        self.stats = stats
        self.total_dmg = total_dmg
        self.passive1 = passive1
        self.passive2 = passive2
        self.passive1_value = passive1_value
        self.passive2_value = passive2_value
        self.total_sum = total_dmg + passive1_value + passive2_value

    def getStats (self):
        return self.stats

    def getTotalDmg (self):
        return self.total_dmg

    def getPassive1 (self):
        return self.passive1

    def getPassive2 (self):
        return self.passive2

    def getPassive1Value (self):
        return self.passive1_value

    def getPassive2Value (self):
        return self.passive2_value

    def getTotalSum (self):
        return self.total_sum

