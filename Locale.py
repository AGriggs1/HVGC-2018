#Anthony Griggs
#HVGC 2018 Game
#Locale class

class Locale:
    #Define the constructor
    def __init__(self, ID, sLongDesc, sShortDesc, sExamineDesc, tItems):
        self.ID = ID
        self.LongDesc = sLongDesc
        self.ShortDesc = sShortDesc
        self.ExamineDesc = sExamineDesc
        self.Visited = False
        self.Examined = False
        #We need to create a new table for the items
        #Doing self.Items = tItems creats a reference
        self.Interactives = []
        for sItem in tItems: self.Interactives.append(sItem)
    #End Constructor

    def UpdateVisited(self):
        if(not self.Visited): self.Visited = True

    def GetDescription(self):
        if self.Visited: return self.ShortDesc
        return self.LongDesc

    #TODO: AddItem, RemoveItem

       
