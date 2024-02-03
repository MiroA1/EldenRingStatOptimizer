
class Combination:

    def __init__(self, stats, stat_sum, total_dmg, passive1_type, passive2_type, passive1_value, passive2_value):

        self.stats = stats
        self.stat_sum = stat_sum
        self.total_dmg = total_dmg
        self.passive1_type = passive1_type
        self.passive2_type = passive2_type
        self.passive1_value = passive1_value
        self.passive2_value = passive2_value
        self.total_sum = total_dmg + passive1_value + passive2_value

    def getStats (self):
        return self.stats

    def getStatSum (self):
        return self.stat_sum

    def getTotalDmg (self):
        return self.total_dmg

    def getPassive1Type (self):
        return self.passive1_type

    def getPassive2Type (self):
        return self.passive2_type

    def getPassive1Value (self):
        return self.passive1_value

    def getPassive2Value (self):
        return self.passive2_value

    def getTotalSum (self):
        return self.total_sum

