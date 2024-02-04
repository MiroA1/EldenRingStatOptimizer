
class StartingClass:
    def __init__(self, class_name, min_vigor, min_mind, min_endurance, min_strength, min_dexterity, min_intelligence, min_faith, min_arcane, min_soul_level):

        self.class_name = class_name
        self.min_vigor = min_vigor
        self.min_mind = min_mind
        self.min_endurance = min_endurance
        self.min_str = min_strength
        self.min_dex = min_dexterity
        self.min_int = min_intelligence
        self.min_fai = min_faith
        self.min_arc = min_arcane
        self.min_soul_level = min_soul_level

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
        return self.min_vigor

    def getMinMind(self):
        return self.min_mind

    def getMinEndurance(self):
        return self.min_endurance

    def getMinStr(self):
        return self.min_str

    def getMinDex(self):
        return self.min_dex

    def getMinInt(self):
        return self.min_int

    def getMinFai(self):
        return self.min_fai

    def getMinArc(self):
        return self.min_arc

    def getMinSoulLevel(self):
        return self.min_soul_level

    def getCurrentVigor(self):
        return self.current_vigor

    def getCurrentMind(self):
        return self.current_mind

    def getCurrentEndurance(self):
        return self.current_endurance

    def getCurrentStr(self):
        return self.current_str

    def getCurrentDex(self):
        return self.current_dex

    def getCurrentInt(self):
        return self.current_int

    def getCurrentFai(self):
        return self.current_fai

    def getCurrentArc(self):
        return self.current_arc

    def getCurrentSoulLevel(self):
        return self.current_soul_level

    def setCurrentVigor(self, current_vigor):
        self.current_vigor = current_vigor

    def setCurrentMind(self, current_mind):
        self.current_mind = current_mind

    def setCurrentEndurance(self, current_endurance):
        self.current_endurance = current_endurance

    def setCurrentStr(self, current_str):
        self.current_str = current_str

    def setCurrentDex(self, current_dex):
        self.current_dex = current_dex

    def setCurrentInt(self, current_int):
        self.current_int = current_int

    def setCurrentFai(self, current_fai):
        self.current_fai = current_fai

    def setCurrentArc(self, current_arc):
        self.current_arc = current_arc

    def setCurrentSoulLevel(self, current_soul_level):
        self.current_soul_level = current_soul_level


    def setMinVigor(self, min_vigor):
        self.min_vigor = min_vigor

    def setMinMind(self, min_mind):
        self.min_mind = min_mind

    def setMinEndurance(self, min_endurance):
        self.min_endurance = min_endurance

    def setMinStr(self, min_str):
        self.min_str = min_str

    def setMinDex(self, min_dex):
        self.min_dex = min_dex

    def setMinInt(self, min_int):
        self.min_int = min_int

    def setMinFai(self, min_fai):
        self.min_fai = min_fai

    def setMinArc(self, min_arc):
        self.min_arc = min_arc






