#--------------------------------------------------------------------------------
# PROBLEM DOMAIN:
#--------------------------------------------------------------------------------

class NinjaFight(object):
    def __init__(self, with_ninja_level):
        self.with_ninja_level = with_ninja_level 
        self.opponent = None 
    
    def decision(self):
        # Business logic for a Ninja should react to increase his survival rate
        assert self.with_ninja_level is not None
        assert self.opponent is not None
        if self.opponent == "Chuck Norris":
            return "run for his life"
        else:
            return "engage the opponent"