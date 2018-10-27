#Anthony Griggs
#HVGC 2018 Game
#Main Game File

from Player import *
from Locale import *

gCont = "continue"
Pan = Player()

#Define Locales
pParkingE = Locale(0, "You finally enter a parking space and get out of your car. You packed lightly, so you don't think you'll be needing the help of bellhop.", "You are in the parking lot", "There doesn't seem many cars here. In fact, the only person around is the man that's talking to you right now. That seems like a good thing, right?", [])
pParkingW = Locale(1, "You begin to make your way towards the hotel entrance.", "You are in the parking lot", "Sunrise Hotel. It gives a nice tropical vibe, doesn't it? Too bad there's no beach nearby!", [])
pEntrance = Locale(2, "You reach the entrance to the hotel. You are eager to check in and officially begin your time off.", "You are at the entrance of the hotel.", "", [])
pLobby = Locale(3, "You enter the hotel lobby. Quaint.", "You are in the hotel lobby.", "Like it's name, the lobby of the hotel is themed with a tropical mindset. It's a bit on the cheesy side, actually.", [])
pFrDesk = Locale(4, "You make your way towards the front desk, the base of which is painted with light-blue wave crests.", "You are at the front desk", "", [])
pCafe = Locale(5, "You head into the hotel cafe. The smell of coffee overwhelms you.", "You are in the cafe", "The cafe has a small-town coffee shop vibe. It's a nice change from the tropical one, that's for sure!", [])
pHallway = Locale(6, "You head down a hallway.", "You are in a hallway.", "There are doors to rooms on each end. Further down the hallway is a door leading outside.", [])
pRecRoom = Locale(7, "You enter what looks like to be rec room.", "You are in a rec room.", "Arcade machines line the wall. There is a pool table and lounge chairs litter the room. Cozy.", [])
pElevator = Locale(8, "It's an elevator. You push the call button and step inside.", "It's an elevator.", "A latin tune is leaking from the a speaker on the ceiling.", [])
pPool = Locale(9, "You head outside and come to a pool.", "You are at the pool.", "Very fitting, for once.", [])
pHotub = Locale(10, "You walk along the poolside and come to a hot tub.", "You are by the hot tub", "It looks very inviting, actually!", [])
pCabana = Locale(11, "You head towards what looks like a shop themed to be a Beach Cabana.", "You are at the cabana.", "It appears to be made out of straw and bamboo.", [])
pHallway2 = Locale(12, "You enter a hallway", "You are in a hallway",  "", [])
pHallway3 = Locale(13, "You continue down the hallway", "You are in a hallway", "", [])
pHallway4 = Locale(14, "You continue down the hallway", "You are in a hallway", "", [])
pBedroom = Locale(15, "You open the door and enter your room.", "You are in your room.", "Not too bad. Two queen-sized beds, a nightstand, a bathroom, and a TV. You even have a balcony!", [])
pBalcony = Locale(16, "You head out onto the balcony.", "You are at your room's balcony", "The view's pretty nice. You needed this, you tell yourself.", [])
#Define the Locations table
#This is used to hook Players, NPCs to the Locale objects
#We can't create a reference to the location from Player, NPC, as Locations have may potentially contain data that is subject to change throughout the game (items, visitation)
tLocations = [pParkingE,
              pParkingW,
              pEntrance,
              pLobby,
              pFrDesk,
              pCafe,
              pHallway,
              pRecRoom,
              pElevator,
              pPool,
              pHotub,
              pCabana,
              pHallway2,
              pHallway3,
              pHallway4,
              pBedroom,
              pBalcony]

#Define the Navigation Matrix
mNavigator = [
    #North, South, East, West
    [None, None, None, pParkingW], #---------ParkingE
    [pEntrance, None, pParkingE, None], #----ParkingW
    [pLobby, pParkingW, None, None], #-------Entrance
    [pFrDesk, pEntrance, pCafe, pHallway], #-Lobby
    [None, pLobby, None, None], #------------FrDesk
    [None, None, None, pLobby], #------------Cafe
    [pElevator, pRecRoom, pLobby, pPool], #--Hallway
    [pHallway, None, None, None], #----------RecRoom
    [None, pHallway, None, None], #----------Elevator
    [pHotub, pCabana, pHallway, None], #-----Pool
    [None, pPool, None, None], #-------------Hotub
    [pPool, None, None, None], #-------------Cabana
    [pElevator, None, pHallway3, None], #----Hallway2
    [None, None, pHallway4, pHallway2], #----Hallway3
    [pBedroom, None, None, pHallway3], #-----Hallway4
    [pBalcony, pHallway4, None, None], #-----Bedroom
    [None, pBedroom, None, None], #----------Balcony
        ]
#To make the methods a bit easier to read, I will define constants to be used as directions
NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
tDirections = {0:"North", 1:"South", 2:"East", 3:"West"}
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
##NPC movement, if it exists, will be entirely scripted. Therefore, this is only for the Player
#####################
def move(iDirection):
    pLocation = mNavigator[Pan.iLocale][iDirection]
    if  pLocation:
        #The player can go here. Do so.
        Pan.iLocale = pLocation.ID
        Pan.Moves += 1
    else: print("You cannot go that way.")
#End move

def examine(iLocale):
    pLocation = tLocations[iLocale]
    print(pLocation.ExamineDesc)
    #TODO: List NPCs at this location
    #TODO: List interactives at this location
    #List the directions the player can go from here
    for i in range(len(mNavigator[0])):
        if mNavigator[iLocale][i]: print("Looks like you can go " + tDirections[i] + " from here.")
    #End for 
#End examine
        
##########
##Init
##Initialization function. Runs at game start
##########
#Initialize the player
def Init():
    copyright(False)
    prompt("begin")
    print("\nIt's that time of year again. The sun's rays rain down on you as you as pull into the parking lot, the air endowed with the summer scent. Vacation time.\n")
    prompt(gCont)
    print("You decided to keep things simple this year for once. Nothing too extravagent. Just an out-of town trip at the nice, but humble, the Sunrise Hotel. Ah.\n")
    prompt(gCont)
    
    Game()
#End Init
###########
##Game
##Code related to actual gameplay. Handles most of io
###########
sHelp = ("List of commands\n"
        "North: moves the player up laterally.\n"
        "South: moves the player down laterally.\n"
        "East: moves the player left laterally.\n"
        "West: moves the player right laterally.\n"
        "Examine: provides a better description of the area you are at, and what directions you may head in from there.\n"
        "Help: Provides a list of valid commands. A dictionary must define a dictionary, right?\n"
        "Moves: List the amount of moves you have made so far. A move is generally defined as changing from one location to another, but it is not limited to that.\n"
        "Talk to: Used to interact with any people who may be in the area.\n"
        "Use: Used to interact with things in the environment you are at.\n"
        "Inventory: Lists any items you may be holding.\n")
def Game():
    bGame = True;
    while(bGame):
        #print the location description, get a command from the player
        sInput = input(tLocations[Pan.iLocale].GetDescription() + "\n").lower()
        tLocations[Pan.iLocale].UpdateVisited()
        #navigation commands
        if sInput == "north": move(NORTH)
        elif sInput == "south": move(SOUTH)
        elif sInput == "east": move(EAST)
        elif sInput == "west": move(WEST)
        #
        elif sInput == "examine": examine(Pan.iLocale)
        elif sInput == "help": print(sHelp) #Define this as a variable to keep this portion clean
        elif sInput == "moves": print(Pan.Name + " has made", Pan.Moves, "moves.\n")
        elif sInput == "talk to": pass #This code will be more advanced. Be careful, love.
        elif sInput == "use": pass #This one will take a lot to make sure it's done right. Depends on items used
        elif sInput == "inventory":
            print("You have: ")
            for s in Pan.Inventory: print(s)
            print()
        #end elif
        elif sInput == "quit": bGame = False
        

        
        
    
Init()

