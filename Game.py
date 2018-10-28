#Anthony Griggs
#HVGC 2018 Game
#Main Game File

from Player import *
from Locale import *
from NPC import *

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
pElevator = Locale(8, "It's an elevator. You push the call button and step inside.", "It's an elevator.", "A Latin tune is leaking from the a speaker on the ceiling.", [])
pPool = Locale(9, "You head outside and come to a pool.", "You are at the pool.", "Very fitting, for once.", [])
pHotub = Locale(10, "You walk along the poolside and come to a hot tub.", "You are by the hot tub", "It looks very inviting, actually!", [])
pCabana = Locale(11, "You head towards what looks like a shop themed to be a Beach Cabana.", "You are at the cabana.", "It appears to be made out of straw and bamboo. A familiar Latin tune is blasting from the radio.", [])
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

#Define NPCs
pFamily = NPC(0, "Cranky Family", "You notice what appears to be a family of 4. Looks like they're arguing.", "You see the cranky family.", 1,
              [
                  ["Cranky Family: Honey, where's Jack's binky?",
                     "Cranky Family: It's in his diaper bag.",
                     "Cranky Family: And where's his diaper bag?",
                     "Cranky Family: I'm hungry!",
                     "Cranky Family: Hold on, sweety! I don't know, check the trunk!",
                     "Cranky Family: Don't tell me you left it at the rest stop...",
                     "Cranky Family: Is it not there? How is that my problem? You're the one that changed him!",
                     "Cranky Family: Waaaaaaah!!!",
                     "Cranky Family: Oh, so it's my fault now? Maybe if you helped out for once we're being having this discussion!",
                     "Cranky Family: I gotta go potty!",
                     "Cranky Family: Why does everything have to be an argument with you? Look, you take Anna to the bathroom and check in, I'll get the diaper bag.",
                     "Cranky Family: Yeah, sure, how about YOU take Anna to the bathroom and I'll get the diaper bag? As if I trust you!",
                     "Cranky Family: Here we go again with this! Whyyyy does it matter who does what?!",
                     "It's doesn't seem like they're going to stop anytime soon..."], #0
                  ["They're still going at it. Perhaps you should stay out of this."] #1
                ])
pAngryWoman = NPC(1, "Irritated Lady", "There is a woman standing by the doorway. She looks upset.", "You see the irritated lady.", 2,
                  [
                      ["Irritated Lady: Finally, some service! This hotel is ridiculous!",
                       "Irritated Lady: Do you have any idea how long I've been waiting for someone to help me with my bags? Who do you people think you people are?",
                       "Irritated Lady: The last bell boy refused to help me! What an absolute jerk! I know they probably pay you 'people' minimum wage, but how is that my problem?!",
                       "Irritated Lady: My room is 301. Take my bags and don't even THINK about stealing my stuff with those grubby hands of yours!",
                       "Irritated Lady: And NO! I will not be giving you a tip! Maybe if you'd gotten here 15 miniutes earlier, but it's not my fault that this dump doesn't know to treat its patrons!",
                       "Okay then."], #0
                      ["Irritated Lady: What is taking Becka so long?! I just want to check in already so we can head out..."], #1
                      ["Irritated Lady: Oh so you finally got my bags to my room? Good for you. Look, I already said you weren't getting a tip, so I don't know why you're wasting my time. Go beg the soup kitchen for a meal, or something!"]
                       
                    ])

pBellhop = NPC(2, "Lazy Bellhop", "You notice a bellhop relaxing on a couch.", "You see the lazy bellhop.", 3,
               [
                   ["Lazy Bellhop: If you're looking for help with your bags, don't bother asking.",
                    "Lazy Bellhop: I've got better things to do than deal with idiots who think they're sooooo special."], #0
                   ["Lazy Bellhop: Hahaha! I see that nutjob lady has you dealing with her bags!",
                    "Lazy Bellhop: Where's your self-respect? You're going to let that bat walk all over you?",
                    "Lazy Bellhop: Or maybe you think what you're doing is a good thing. Get over yourself.",
                    "Lazy Bellhop: I almost feel bad for you. Oooooh, man!"], #1
                   ["Lazy Bellhop: I almost feel bad for you. Oooooh, man!"] #2
                   ])

pOldLady = NPC(3, "Elderly Woman", "There is an old woman relaxing in a chair.", "You see the elderly woman", 3,
                [
                    ["Elderly Woman: Oh, hello deary! What brings you out here to a place like this?",
                     "Elderly Woman: Me, I'm just relaxing, taking a staycation, if you will. It's been a tradition to come here with my dearest Bernie.",
                     "Elderly Woman: I remember the first time Bernie took me out here. It was way back in '55, I believe.",
                     "Elderly Woman: Bernie, young and dashing tells me about this hotel he wants to spend the weekend with me. Says it's called Sasperella Hotel.",
                     "Elderly Woman: I never really understood why it was called that. Times were different, mind you. That just means things have changed.",
                     "Elderly Woman: You're still young, who knows what they'll call this place 50 years from now?",
                     "Elderly Woman: I still remember when the daggerbee was the talk of town! Those were different times, they were.",
                     "Elderly Woman: I loved that dance. I used to dance my little heart out, but my poor, poor, Bernie just couldn't keep up!",
                     "Elderly Woman: Oh, but this old body can't either, now.",
                     "Elderly Woman: I remember asking Bernie why in God's name he wanted to stay at a hotel when we had a perfectly good home",
                     "Elderly Woman: You've seen this place, right? It's not exactly luxurious, is it? It wasn't back then either!",
                     "Elderly Woman: This building goes way back. I don't think it was always a hotel, but who knows?",
                     "Elderly Woman: Why would anyone stay here when they're not out-of town? I just could not figure it out!",
                     "Elderly Woman: And my Bernie, charming as he always was, he says,",
                     "Elderly Woman: What was it? He says, 'Benny', it ain't where you go, it's who you go with!'",
                     "Elderly Woman: And I go: 'Yeah, whatever!' and, well, here we are now!",
                     "Elderly Woman: Bernie was just that kind of man. Always looking to do something, even if that something seemed like a waste of time and money.",
                     "Elderly Woman: He truly believed that it wasn't where you went or what you did, but who you were with.",
                     "Elderly Woman: And in a way, he was right. He was absolutely right.",
                     "Elderly Woman: Deary, could you do me a favor and get me some chamomile tea from the cafe? It helps me relax! Thank you, dear!"], #0
                    ["Elderly Woman: Hello dear, did you get me my tea? These old bones need nourishment!"], #1 - repeat this will waiting for tea
                    ["Elderly Woman: Hello dear, did you get me my tea?",
                     "Elderly Woman: Thank you, honey!",
                     "Elderly Woman: Such a youngling, aren't you?",
                     "Elderly Woman: Are you here with anyone? Well, they must be a lucky soul to have someone as well mannered as you!",
                     "Elderly Woman: Remember to keep those who matter in life close. You never know when they'll move on to the next life.",
                     "Elderly Woman: I still come here every so often, even though my Bernie is no longer with me.",
                     "Elderly Woman: I'm just so fond of the memories here. This place means a lot to me and Bernie.",
                     "Elderly Woman: I hope you can say the same about something in your life.",
                     "Elderly Woman: You may be young, but one day you'll be as old as I before you even know it!",
                     "Elderly Woman: You tend to spend a lot of time reflecting on your life as you get older.",
                     "Elderly Woman: Not in a sort regretting, fashion, oh no! Just in a sort of fond way.",
                     "Elderly Woman: When your bones get as brittle as mine, what else are you to do?",
                     "Elderly Woman: I remember a time when I could dance the night away. Now, not so much.",
                     "Elderly Woman: That's just life for you. Spend your young days having fun, so you have something to look back on when you get old.",
                     "Elderly Woman: Oh, honey, this isn't chamomile tea at all! Could you take this back and get me my tea? Thank you!"], #2
                    ["Elderly Woman: Oh, you're  back! And I see you got me my tea! You're such a good dear!",
                     "Elderly Woman: We need more people like you out there in the world. I don't mean to tell you how to live your life, but do you do any volunteer work?",
                     "Elderly Woman: You should consider it. There is always someone out there that could use the helping hand of another, and unfortunately some people don't have anyone they can rely on.",
                     "Elderly Woman: Be grateful for what you have. Recognize that others are not so lucky!",
                     "Elderly Woman: It seems to me that some people have lost their manners these days. I remember when people left their front doors unlocked.",
                     "Elderly Woman: Times are different, but I'm still the same old woman I was way back when. There used to be this one song I adored, but it drove my Bernie mad!",
                     "Elderly Woman: Oh, what was it called again? I don't remember. It was waaaay back!",
                     "Elderly Woman: This old brain can problems remember the details of things. Faces, however, are forever.",
                     "Elderly Woman: I remeber an individual who stayed here, what was it, 10 years ago? Must of have been.",
                     "Elderly Woman: This one man stayed for about a year. He would be holed up in his room for most of the time. Rarely talked to anyone, wouldn't let the maids clean his room.",
                     "Elderly Woman: He was an odd fellow for sure. I wonder what ever happended to him...",
                     "Elderly Woman: Dear, could you get me more sugar for my tea? Thank you!"], #3
                    ["Elderly Woman: Thank you, dear! You've been a big help!",
                     "You're a good listener, you know that? I've been rambling for a while, so I think I'll just leave you to your business. It was nice getting to know you!"], #4
                    ["She seems to be preoccupied with a novel she's reading."] #5
                    ])
    
tNPCs = [pFamily,
         pAngryWoman,
         pBellhop,
         pOldLady]
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
        sInput = input(sMessage + "\nPlay again? Y|N").lower()
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
#####################
##examine
##Prints out various information about the given location, including
## NPCs at the location
## Things the player can do at the location
    
def examine(iLocale):
    pLocation = tLocations[iLocale]
    print(pLocation.ExamineDesc)
    for p in tNPCs:
        if p.iLocale == iLocale: print(p.LongDesc)
    #TODO: List interactives at this location
    #List the directions the player can go from here
    for i in range(len(mNavigator[0])):
        if mNavigator[iLocale][i]: print("Looks like you can go " + tDirections[i] + " from here.")
    #End for
    tLocations[iLocale].Examined = True
#End examine
####################
##talkTo
##Attempts to talk to the person with passed name
####################
def talkTo(sPerson):
    #find the person the player requested - they must be at the same location as the player!
    bFound = False
    for p in tNPCs:
        if p.Name.lower() == sPerson and p.iLocale == Pan.iLocale:
            bFound = True
            for s in p.Dialogue[p.Progress]: input(s)
            onDialogueEnd(p.ID)
        #end if
    #end for
    if(not bFound): print("There is no " + sPerson)
#end talkTo
########################
##onDialogue
##Runs whenever the player is done talking to an NPC.
########################
def onDialogueEnd(iNPC):
    pNPC = tNPCs[iNPC]
    #Cranky Family
    if iNPC == 0:
        pNPC.Progress = 1
    #Angry Woman
    elif iNPC == 1:
        if pNPC.Progress == 0: pNPC.Progress = 1
        #TODO: Logic for once player drops off luggage at NPC's room. We'll need a hook for that.
    #Lazy Bellhop
    elif iNPC == 2:
        #if pNPC.Progress != 2: pNPC.Progress += 1
        if pNPC.Progress == 0 tNPCs[1].Progress == 1: pNPC.Progress = 1
        elif pNPC.Progress == 1: pNPC.Progress = 2
    #Old Lady
    elif iNPC == 3:
        if pNPC.Progress != 1 or pNPC.Progress != 5:
            #She has requested the player get something. Set to 1
            pNPC.Progress = 1
        elif pNPC.Progress == 1:
               pass #TODO: rely on logic for Barista to set Progress here
        else:
            pNPC.Progress = 5
    
############
##reset
##Used to initialize data
############
def reset():
    for p in tLocations:
        p.Visited = False
        p.Examined = False
    for p in tNPCs:
        p.Progress = 0
    Pan.Name = "Pan"
    Pan.Score = 0
    Pan.Moves = 0
    Pan.iLocale = 0
    Pan.Inventory = []
#End reset
    
##########
##Init
##Initialization function. Runs at game start
##########
#Initialize the player
def Init():
    reset()
    prompt("begin")
    print("\nIt's that time of year again. The sun's rays rain down on you as you as pull into the parking lot, the air endowed with the summer scent. Vacation time.\n")
    prompt(gCont)
    print("You decided to keep things simple this year for once. Nothing too extravagent. Just an out-of town trip at the nice, but humble, Sunrise Hotel. Ah.\n")
    prompt(gCont)
    
    Game()
    return copyright(True)
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
        elif sInput == "talk to":
            #print all of the NPCs at this location IF the player examined the location
            print("Talk to?")
            if tLocations[Pan.iLocale].Examined:
                for p in tNPCs:
                    print(p.iLocale)
                    print(Pan.iLocale)
                    if p.iLocale == Pan.iLocale: print(p.Name)
                #end for
                sInput = input().lower
                talkTo(sInput)
            #end if
        elif sInput == "use": pass #This one will take a lot to make sure it's done right. Depends on items used
        elif sInput == "inventory":
            print("You have: ")
            for s in Pan.Inventory: print(s)
            print()
        #end elif
        elif sInput == "quit": bGame = False
        

        
        
copyright(False)
while Init(): Init()

