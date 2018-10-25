#Anthony Griggs
#HVGC 2018 Game
#Locale class

class Locale:
    #Define the constructor
    def __init__(self, ID, sLongDesc, sShortDesc, sExamineDesc, tItems):
        self.ID = ID
        self.LongDesc = sLongDesc
        self.ShortDesc = sShortDesc
        self.Visited = False
        #We need to create a new table for the items
        #Doing self.Items = tItems creats a reference
        self.Items = []
        for sItem in tItems: self.Items.append(sItem)
    #End Constructor

    #TODO: AddItem, RemoveItem

       
