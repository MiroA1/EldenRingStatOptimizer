
class WeaponScaling:
    def __init__(self, str_scaling, dex_scaling, int_scaling, fai_scaling, arc_scaling):

        self.str_scaling = str_scaling
        self.dex_scaling = dex_scaling
        self.int_scaling = int_scaling
        self.fai_scaling = fai_scaling
        self.arc_scaling = arc_scaling

    def getStrScaling(self):
        return self.str_scaling

    def getDexScaling(self):
        return self.dex_scaling

    def getIntScaling(self):
        return self.int_scaling

    def getFaiScaling(self):
        return self.fai_scaling

    def getArcScaling(self):
        return self.arc_scaling

