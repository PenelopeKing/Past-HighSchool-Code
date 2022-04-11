# King, Penny
# Project 2
# Comp Sci Prin. Period 2
# 2.20.2019
'''
Room Layout:
 6 > 7 > 8
 ^       v
 3 | 4 | 5
 ^   ^   v
*0 | 1 < 2

* start at room 0
'''
print ("WELCOME TO THE QUEST FOR THE HOLY GRAIL")
# init start value for global vaiables
gameOver = False
gameWin = False
roomNum = 0 # this is current room number. start in room 0
inventory = []
rules = '''
HERE ARE THE ACTIONS YOU CAN USE
right = moves right
left = moves left
up = move up
down = move down
quit = ends game
look = describes environment
grab = takes item
inventory = checks your inventory
fight = fights beast
help = shows actions you can use
'''
# allows movements in map
map0 = [False, 'up','shubbery'] # first item stores whether visited room yet
map1 = [False,'up','right']
map2 = [False,'left','up','gem']
map3 = [False,'up','down','shubbery']
map4 = [False,'left']
map5 = [False,'up','down','coconut shell']
map6 = [False,'down','right','holy hand grenade']
map7 = [False,'left','right','sword']
map8 = [False,'left','down']
dungeon = [map0,map1,map2,map3,map4,map5,map6,map7,map8]

monsterlist = ['empty','Knights Who Say Ni','empty','empty','Black Knight',\
'','','','The Killer Rabbit of Caerbannog']

# room descriptions
introroom0 = """You are in a meadow. You are surrounded by lush grass
and pink flowers. You can to smell them but you don't have time for that!!
You must first complete your mission of finding the Holy Grail!!
You are wearing the finest armor... but you lost your sword :( 
There is a forest ahead of you...maybe you could start there?"""
room0 = 'MEADOW: You can move UP ahead towards a forest.'

introroom1 = '''ni ni ni ni ni--- There is a large man in front of you.
His helmet has large antlers with fur hanging down from them.
"The Knights Who Say Ni demand a sacrifice!" he bellows. 
"We shall continue to say NI if you do not appease us."'''
room1 = 'FOREST: UP ahead is deeper into the forest... the air feels uneasy...'

introroom2 = """There is gem in the forest.
There are thick branches everywhere and there are so many you can barely see
what is in front of you. You hear faint sounds in the distance...
it sounds like the voice is saying... "ni"?"""
room2 ='''FOREST: UP the hill is the rocky canyon
and RIGHT goes deeper into the forest.'''

introroom3 = """You have just entered the forest. A man is giving away shubbery.
There is the meadow DOWN the hill, and more forest UP ahead..."""
room3 = """FOREST: It's pretty dark in the forest. There is a town UP ahead
and the meadow is DOWN the hill."""

# room 4 descriptions
introroom4 = """Right in front of you is the famous Black Knight!
You ask him to join your mission of finding the Holy Grail but all he says is,
"NONE SHALL PASS. I MOVE FOR NO MAN"... I guess he's not joining you then?"""
room4 = "EXTRA DARK FOREST: The forest that you came from is behind you."

introroom5 = """You are in a meadow filled with flowers! It's super pretty.
You step on a coconut shell that a swallow probably dropped."""
room5 = "MEADOW: You can go DOWN the hill or UP the road beyond the meadow."

introroom6 = """As you walk past the crowded town.
Everyone's busy trying to kill a witch. Somehow a duck is involved...
While walking you see a priest who offers you the fabled Holy Hand Grenade!"""
room6 = '''TOWN: You can either go RIGHT and walk out of the town
or go DOWN the hill to the forest'''
# room 7 introduction + descriptions
introroom7 = '''As you walk down the rocky road you find your lost sword!
How did it get there?!?'''
room7 ='ROCKY ROAD: To your LEFT is the town and RIGHT is a rocky canyon.'

introroom8 = '''You are at a rocky canyon... You quietly walk down the path
and then you stop. And there... right in that cave...
IS THE KILLER RABBIT OF CAEBANNOG!!!!
It supposedly has a vicious streak a mile wide! (And has sharp pointy teeth!)'''
room8 = 'CAVE: LEFT is the rocky road and DOWN the canyon is a flowery meadow.'
# room descritpions when you first enter the room
description = [introroom0,introroom1,introroom2,introroom3, introroom4,\
introroom5,introroom6,introroom7,introroom8]
# room descriptions for 'look' command
secondD = [room0,room1,room2,room3,room4,room5,room6,room7,room8]

# before start while loop: explain the rules + greet user
# describe movelist with left

print("Here are some basic rules of the game...\n" + rules)


while not gameOver:
    # will print the intro description of a room if you have not entered it yet
    if dungeon[roomNum][0] ==  False:
        print(description[roomNum]+'\n')
        dungeon[roomNum][0] = True
    else:
        print (' ')
    # determines if monster is in room
    if 'Knights Who Say Ni' in monsterlist[roomNum] or \
    'Black Knight' in monsterlist[roomNum] or \
    'The Killer Rabbit of Caerbannog' in monsterlist[roomNum]:
        monsterinroom = True
    else:
        monsterinroom = False
    move = input('What do you want to do? >> ') # ask for user's desired action
    if move.lower() == 'help':
        print(rules+'\n')
    elif move.lower() == 'quit':
        print('\nGAME OVER')
        gameOver = True
    elif move.lower() == 'grab':
        whatGrab = input ("What do you want to grab? >> ")
        if whatGrab.lower() in dungeon[roomNum]:
            if whatGrab.lower() == 'up' or whatGrab.lower() == 'down'\
            or whatGrab.lower() == 'right' or whatGrab.lower() == 'left':
                print ('haha very funny...') # can't grab down/up/etc...
            else:
                inventory.append(whatGrab.lower())
                dungeon[roomNum].remove(whatGrab.lower()) # deletes item from room
                print (whatGrab + ' is now in your inventory')
        else:
            print ('huh?')
    # if use wants to move right
    elif move.lower() == 'right':
        if 'right' in dungeon[roomNum]:
            roomNum +=1
            if monsterinroom == True:
                gameOver = True
                print("Uh oh... it attacked you and you died :(")
        else:
            print ("Um... you can't do that...")
    # if user wants to move left
    elif move.lower() == 'left':
        if 'left' in dungeon[roomNum]:
            roomNum -=1
            if monsterinroom == True:
                gameOver = True
                print("Uh oh... it attacked you and you died :(")
        else:
            print ("Um... you can't do that...")
    # if user wants to move up
    elif move.lower() == 'up':
        if 'up' in dungeon[roomNum]:
            roomNum +=3
            if monsterinroom == True:
                gameOver = True
                print("Uh oh... it attacked you and you died :(")
        else:
            print ("Um... you can't do that...")
    # if user wants to down
    elif move.lower() == 'down':
        if 'down' in dungeon[roomNum]:
            roomNum -=3
            if monsterinroom == True:
                gameOver = True
                print("Uh oh... it attacked you and you died :(")
        else:
            print ("Um... you can't do that...")
    # if user wants to fight
    elif move.lower() == 'fight':
        # check if can first!
        if monsterinroom == False:
            print ("There's nothing to fight here!")
        else:
            how_fight = input('What would you like to fight with? >> ')
            if how_fight.lower() in inventory:
                if monsterlist[roomNum] == 'empty':
                    print ('nothing to fight here!')
                else:
                    if monsterlist[roomNum]=='The Killer Rabbit of Caerbannog':
                        if how_fight.lower()=='holy hand grenade':
                            inventory.remove('holy hand grenade')
                            monsterinroom = False
                            monsterlist[roomNum] = 'empty'
                            print('Before using Hold Hand Grenade you pray.\n'+\
                            ' "O lord, bless this thy hand grenade,\n '+\
                            'that with it thou mayest blow thy enemies '+\
                            'to tiny bits, in thy mercy."')
                            print ('You throw the Holy Hand Grenade')
                            print ('The rabbit dies and all is good.')
                        else:
                            print("The Killer Rabbit of Caerbannog killed "+\
                            "you with its sharp and pointy teeth!!")
                            gameOver = True
                    elif monsterlist[roomNum] == 'Knights Who Say Ni':
                        if how_fight.lower() == 'shubbery':#if has right weapon
                            inventory.remove('shubbery')
                            monsterinroom = False
                            monsterlist[roomNum] = 'empty'#'kills' monster
                            print(\
                            'The Knights Who Say Ni'+\
                            'thanked you and walked away')
                        else:
                            print('The Knights Who Say Ni got annoyed that'+\
                            'they did not get their shubbery'+\
                            'and then they killed you')
                            gameOver = True
                    elif monsterlist[roomNum] == 'Black Knight':
                        if how_fight.lower() == 'sword':
                            if 'gem' in inventory: # if you have nec. items
                                inventory.remove('sword')
                                inventory.remove('gem')
                                monsterinroom = False
                                monsterlist[roomNum] = 'empty'
                                print (\
                                "You slice off Black Knight's right arm..."+\
                                "then his left one... \n"+\
                                "He tried to fight you with his legs so you " +\
                                "used your gem and sword to cut those off too")
                                gameWin = True
                                gameOver = True
                        else:
                            print("The Black Knight killed you and you died...")
                            gameOver = True
            else:
                print("you don't have that weapon...")
    # if user wants to observe surroundings
    elif move.lower() == 'look':
        print(secondD[roomNum])
    elif move.lower() == 'inventory':
        if len(inventory) == 0: # if nothing in inventory will say
            print ("There's nothing in your inventory")
        elif len(inventory) == 1:
            print ("In your inventory is: " + inventory[0])
        else:  # prints inventory
            print("In your inventory is", end='')
            for i in range (len(inventory)):
                print(", "+inventory[i], end="")
            print(' ')
    else: # actions not on menu not do anything
        print ("I don't understand that action...")
# when you defeat boss, get a special game win message
if gameWin == True:
    print ("\nYAY!!! You defeated the Black Knight! \n" +\
    "You continue on your journey but then THE POLICE ARRIVES!!\n"+\
    "You are arrested for murder and it looks like your mission ends...")
else:
    print("GAME OVER!")