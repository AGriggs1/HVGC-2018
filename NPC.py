#Anthony Griggs
#HVGC 2018 Game
#NPC class

class NPC
    def __init(self, ID, sName, sLongDesc, sShortDesc, iLocale, mDialogue):
        self.ID = ID
        self.Name = sName
        self.LongDesc = sLongDesc
        self.ShortDesc = sShortDialogue
        self.iLocale = iLocale
        self.Progress = 0 #Used for mDialogue
        #mDialogue[Progress]["Message", ...]
        #deepcopy the matrix
        self.Dialogue = [][]
        for r in mDialogue:
            for c in r: self.Dialogue[r] = c
        #end for
    #end constructor
            
        
