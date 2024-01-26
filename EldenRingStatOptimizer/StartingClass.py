
class StartingClass:
    def __init__(self, class_name, min_vigor, min_mind, min_endurance, min_strength, min_dexterity, min_intelligence, min_faith, min_arcane, min_soul_level):

        self.class_name = class_name
        self.vigor = min_vigor
        self.mind = min_mind
        self.endurance = min_endurance
        self.strength = min_strength
        self.dexterity = min_dexterity
        self.intelligence = min_intelligence
        self.faith = min_faith
        self.arcane = min_arcane
        self.soul_level = min_soul_level

        #Current Stats
        self.current_vigor = min_vigor
        self.current_mind = min_mind
        self.current_endurance = min_endurance
        self.current_str = min_strength
        self.current_dex = min_dexterity
        self.current_int = min_intelligence
        self.current_fai = min_faith
        self.current_arc = min_arcane
        self.current_soul_level = min_soul_level



    def getName(self):
        return self.class_name

    def getMinVigor(self):
        return self.vigor

    def getMinMind(self):
        return self.mind

    def getMinEndurance(self):
        return self.endurance

    def getMinStrength(self):
        return self.strength

    def getMinDexterity(self):
        return self.dexterity

    def getMinIntelligence(self):
        return self.intelligence

    def getMinFaith(self):
        return self.faith

    def getMinArcane(self):
        return self.arcane

    def getMinSoul_level(self):
        return self.soul_level

    def getCurrentVigor(self):
        return self.current_vigor

    def getCurrentMind(self):
        return self.current_mind

    def getCurrentEndurance(self):
        return self.current_endurance

    def getCurrentStrength(self):
        return self.current_str

    def getCurrentDexterity(self):
        return self.current_dex

    def getCurrentIntelligence(self):
        return self.current_int

    def getCurrentFaith(self):
        return self.current_fai

    def getCurrentArcane(self):
        return self.current_arc

    def getCurrentSoul_level(self):
        return self.current_soul_level



