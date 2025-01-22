#Higher or Lower Number Game - www.101computing.net/higher-or-lower-number-game/

from random import randint

numberToGuess = randint(1,100)

userGuess = -1

while (userGuess != numberToGuess):
    userGuess = int(input("guess the number: "))
    if numberToGuess > userGuess:
       print("the number to geuss is higher")
    elif numberToGuess < userGuess:
        print("the number to geuss is lower")
        
print("you won!")

