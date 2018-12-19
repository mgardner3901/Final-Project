"""
Author: Morgan Gardner
Credit: 
"""    
    
print('-----------------')
print('   -Adventure-   ')
print('-----------------')

print ("You wake up in a dark room lit only by a single cande. Your eyes adjust and you look around. You seem to be in a cell made from stone and you notice that the door to the cell has been left open. You decide to get up and explore. Do you take the candle with you? ")
ch1 = str(input("Do you take it? [y/n]: "))

if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
    print("You have taken the candle")
    candle = 1

else:
    print("You leave the candle behind")
    candle = 0
    
print ("As you proceed further into the cave, you see a small glowing object")
ch2 = str(input("Do you approach the object? [y/n]"))

if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
    print ("You approach the object...")
    print ("As you draw closer with the help of your candle you begin to make out what the shine is.")
    print ("The eye belongs to a goblin!")
    print("It looks as if he is munching on the arm of what you can only assume to be one of the previous guards of this prison.")
    print("It also looks as if he is holding on to something shiny.")
    ch3 = str(input("Do you try to fight it? [Y/N]"))
