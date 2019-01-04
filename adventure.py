"""
Author: Morgan Gardner
Credit: codereview.stackexchange.com
"""    
    
print('-----------------')
print('   -Adventure-   ')
print('-----------------')

import random

print ("You wake up in a dark room lit only by a single cande. Your eyes adjust and you look around. You seem to be in a cell made from stone and you notice that the door to the cell has been left open. You decide to get up and explore. Do you take the candle with you? ")
ch1 = str(input("Do you take it? [Yes or No]: "))

if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
    print("You have taken the candle")
    candle = 1

else:
    print("You leave the candle behind")
    candle = 0
    
print ("As you proceed further into the cave, you see a small glowing object")
ch2 = str(input("Do you approach the object? [Yes or No]"))

if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
     print ("You approach the object...")
     print ("As you draw closer with the help of your candle you begin to make out what the shine is.")
     print ("The eye belongs to a goblin!")
     print("It looks as if he is munching on the arm of what you can only assume to be one of the previous guards of this prison.")
     print("It also looks as if he is holding on to something shiny.")
   
ch3 = str(input("Do you try to fight it? [Yes or No]"))
 
 
if ch3 in ['y', 'Y', 'Yes', 'YES', 'yes']:

        #with candle
        if candle == 1:
            print ("You only have a candle to fight with!")
            print ("You wave the flame at the goblin and it screeches and cowers")
            print ("------------------------------------------------")
            print ("                     COMBAT                     ")
            print ("   YOU MUST HIT ABOVE A 5 TO KILL THE GOBLIN    ")
            print ("IF THE GOBLIN HITS HIGHER THAN YOU, YOU WILL DIE")
            print ("------------------------------------------------")
            fdmg1 = int(random.randint(3, 9))
            edmg1 = int(random.randint(1, 5))
            print ("you hit a", fdmg1)
            print ("the goblin hits a", edmg1)

            if edmg1 > fdmg1:
                print ("The goblin has dealt more damage than you!")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the goblin, but you manage to fend it off")
                complete = 1
                return complete

            else:
                print ("You killed the goblin!")
                complete = 1
                return complete    
                
        #without candle
        else:
            print ("You don't have anything to fight with!")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("                  Fighting...                   ")
            print ("   YOU MUST HIT ABOVE A 5 TO KILL THE GOBLIN    ")
            print ("IF THE GOBLIN HITS HIGHER THAN YOU, YOU WILL DIE")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            fdmg1 = int(random.randint(1, 7))
            edmg1 = int(random.randint(1, 5))
            print ("you hit a", fdmg1)
            print ("the goblin hits a", edmg1)

            if edmg1 > fdmg1:
                print ("The goblin has dealt more damage than you!")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the goblin, but you manage to escape")
                complete = 1
                return complete

            else:
                print ("You killed the goblin!")
                complete = 1
                return complete
                
#dont fight
print ("You choose not to fight the goblin.")
print ("As you turn to run away it rushes you and stabs you with it's dagger!")
complete = 0
return complete


else:
        print ("You turn away from the glowing object, and attempt to leave the cave...")
        print ("But something won't let you....")
        complete = 0
        return complete

    
    





    




