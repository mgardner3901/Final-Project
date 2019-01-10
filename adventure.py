"""
Author: Morgan Gardner
Credit: codereview.stackexchange.com
"""    

def game():

import random


print('                                         -----Adventure-----   ')


print ("You wake up in a dark room lit only by a single cande. Your eyes adjust and you look around. You seem to be in a cell made from stone and you notice that the door to the cell has been left open. You decide to get up and explore. Do you take the candle with you? ")
case1 = str(input("Do you take it? [Yes or No]: "))

if case1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
    print("-+-You have taken the candle-+-")
    candle = 1

else:
    print("-+-You leave the candle behind-+-")
    candle = 0
    
print ("As you proceed further into the cave, you see a small glowing object")
case2 = str(input("Do you approach the object? [Yes or No]"))

if case2 in ['n', 'N', 'No', 'NO', 'No']:
    print('You attempt to tuen and go in the opposite direction of the object but whatever it is its alive! It leaps at you!')

if case2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
     print ("You approach the object...")
     print ("As you draw closer you begin to make out what the glow is.")
     print ("Its an eye! And it belongs to a goblin! It looks as if he is munching on the arm of what you can only assume to be one of the previous guards of this prison.")
     print("It also looks as if he is holding on to something shiny.")
     
case3 = str(input("Do you try to fight it? [Yes or No]"))
 
 
if case3 in ['y', 'Y', 'Yes', 'YES', 'yes']:

        #fight with the candle
        if candle == 1:
            print ("You only have a candle to fight with!")
            print ("You wave the flame at the goblin and it screeches and cowers")
            print ("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")
            print ("                      COMBAT                    ")
            print ("    YOU MUST HIT ABOVE A 5 TO KILL THE GOBLIN   ")
            print ("IF THE GOBLIN HITS HIGHER THAN YOU, YOU WILL DIE")
            print ("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")
            fdmg1 = int(random.randint(3, 9))
            edmg1 = int(random.randint(1, 5))
            print ("you hit a", fdmg1)
            print ("the goblin hits a", edmg1)

            if edmg1 > fdmg1:
                print ("The goblin has dealt more damage than you, but you manage to escape safely!")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the goblin, but you manage to fend it off and escape")
                complete = 1
                return complete

            else:
                print ("You killed the goblin!")
                complete = 1
                return complete    
                
        #fight without the candle
        else:
            print ("You don't have anything to fight with!")
            print ("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")
            print ("                    COMBAT                      ")
            print ("    YOU MUST HIT ABOVE A 5 TO KILL THE GOBLIN   ")
            print ("IF THE GOBLIN HITS HIGHER THAN YOU, YOU WILL DIE")
            print ("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")
            fdmg1 = int(random.randint(1, 7))
            edmg1 = int(random.randint(1, 5))
            print ("you hit a", fdmg1)
            print ("the goblin hits a", edmg1)

            if edmg1 > fdmg1:
                print ("The goblin has dealt more damage than you!")
                complete = 0
                return complete

            elif fdmg1 < 5:
                print ("You didn't do enough damage to kill the goblin, but you manage to get away")
                complete = 1
                return complete

            else:
                print ("You killed the goblin!")
                complete = 1
                return complete
                
#dont approach the object               
if case3 in ['n', 'N', 'No', 'NO', 'no']:
    print ("You run and attempt to leave the cave...")
    print ("But something won't let you....")
    complete = 0
    return complete
    

# game complete and loop
alive = True
while alive:
    
    complete = game()
    if complete == 1:
        alive = input('You managed to escape the prison unharmed! But who brought you there? And why? Would you like to play again? [y/n]: ')
    if alive in ['y', 'Y', 'YES', 'yes', 'Yes',]:
        alive

    
    

    
#Notes --The return statement allows you to terminate the execution of a 
#        function before you reach the end.The flow of execution 
#        immediately returns to the caller.
#
#
    

                




