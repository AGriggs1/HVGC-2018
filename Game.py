#Anthony Griggs
#HVGC 2018 Game
#Main

from Player import *
from Locale import *

gCont = "continue"
Pan = Player()

#Define Locales
pParkingE = Locale(0, "You finally enter a parking space and get out of your car. You packed lightly, so you don't think you'll be needing the help of bellhop.", "You are in the parking lot", "There doesn't seem many cars here. In fact, the only person around is the man that's talking to you right now. That seems like a good thing, right?", [])
pParkingW = Locale(1, "You begin to make your way towards the hotel entrance.", "You are in the parking lot", "Sunrise Hotel. It gives a nice tropical vibe, doesn't it? Too bad there's no beach nearby!", [])
pEntrance = Locale(2, "You reach the entrance to the hotel. You are eager to check in and officially begin your time off.", "You are at the entrance of the hotel.", "", [])
pLobby = Locale(3, "You enter the hotel lobby. Quaint.", "You are in the hotel lobby.", "Like it's name, the lobby of the hotel is themed with a tropical mindset. It's a bit on the cheesy side, actually.", [])
pFrDesk = Locale(4, "You make your way towards the front desk, the base of which is painted with light-blue wave crests.", "You are at the front desk", "", ["Pen"])
pCafe = Locale(5, "You head into the hotel cafe. The smell of coffee overwhelms you.", "You are in the cafe", "The cafe has a small-town coffee shop vibe. It's a nice change from the tropical one, that's for sure!", [])

#Define the Locations table
#This is used to hook Players, NPCs to the Locale objects
#We can't create a reference to the location from Player, NPC, as Locations have may potentially contain data that is subject to change throughout the game (items, visitation)9
tLocations = [pParkingE,
              pParkingW,
              pEntrance,
              pLobby,
              pFrDesk,
              pCafe]

#Define the Navigation Matrix
mNavigator = [
    #North, South, East, West
    [None, None, None, pParkingW], #------ParkingE
    [pEntrance, None, pParkingE, None], #-ParkingW
    [pLobby, pParkingW, None, None], #----Entrance
    [pFrDesk, pEntrance, pCafe, None], #---Lobby
    [None, pLobby, None, None], #---------FrDesk
    [None, None, None, pLobby] #----------Cafe
        ]
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
#End copyright
#####################
##Prompt
##Used to stop pause the game and wait for the player to continue
#####################
def prompt(sMessage):
    input("Print enter to " + sMessage)
#End prompt

#####################
##move
##Attempts to move the player in passed direction
#####################
def move(iDirection):
    pLocation = mNavigator[Pan.iLocale][iDirection]
    if  pLocation:
        #The player can go here. Do so.
        Pan.iLocale = pLocation.ID
        Pan.Moves += 1
        tLocations[pLocation.ID].UpdateVisited()
    else: print("You cannot go that way.")
#End move

##########
##Init
##Initialization function. Runs at game start
##########
#Initialize the player
def Init():
    copyright(False)
    
    print("\nIt's that time of year again. The sun's rays rain down on you as you as pull into the parking lot, the air endowed with the summer scent. Vacation time.\n")
    prompt(gCont)
    print("You decided to keep things simple this year for once. Nothing too extravagent. Just an out-of town trip at the nice, but humble, the Sunrise Hotel. Ah.\n")
    prompt(gCont)
    print(tLocations[Pan.iLocale].LongDesc)
    move(0) #0 = North
    move(3) #3 = West
    prompt(gCont)
    print(tLocations[Pan.iLocale].LongDesc)

def Game():
    bGame = True;
    
    
Init()

