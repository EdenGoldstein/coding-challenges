
#Poker Dice Challenge - www.101computing.net/fancy-a-game-of-poker-dice/

import random

die1=random.randint(1,6)
print("Die 1: " + str(die1))

die2=random.randint(1,6)
print("Die 2: " + str(die2))

die3=random.randint(1,6)
print("Die 3: " + str(die3))

if die1 == die2 and die2 == die3:
   print("Three of a kind")
   
elif die1 == die2 or die1 ==die3 or die2 == die3:
    print("1 pair!")
    
else:
    print("better luck next time!") 

