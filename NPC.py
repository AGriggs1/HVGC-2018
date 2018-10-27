#Anthony Griggs
#HVGC 2018 Game
#NPC class
from copy import *

class NPC:
    def __init__(self, ID, sName, sLongDesc, sShortDesc, iLocale, mDialogue):
        self.ID = ID
        self.Name = sName
        self.LongDesc = sLongDesc
        self.ShortDesc = sShortDesc
        self.iLocale = iLocale
        self.Progress = 0 #Used for mDialogue
        #mDialogue[Progress]["Message", ...]
        #deepcopy the matrix
        self.Dialogue = deepcopy(mDialogue)
    #end constructor
            
        
