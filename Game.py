#Anthony Griggs
#HVGC 2018 Game
#Main

from Player import *
from Locale import *
####################
##UTILITY FUNCTIONS
####################

########################
##copyright
##Prints a small blurb for the game
##Also used on game overs. Allows the player to decide if they want to restart or not
########################
def copyright(bEndGame):
    sMessage = "Made for the Hudson Valley Games Coference by Anthony Griggs.\nAnthony.Griggs1@marist.edu"
    if bEndGame:
        #The player has quit, or the game is over
        print("Game over! Thanks for playing!")
        #Ask if they want to play again, if not then terminate the program. Otherwise, the game will start over
        sInput = input(sMessage + "\nPlay again? ").lower()
        if "y" in sInput: return True
        return False
    print(sMessage)
        

##########
##Init
##Initialization function. Runs at game start
##########
def Init():
    copyright(False)
    Pan = Player()
    print(Pan.Name)
    
Init()

