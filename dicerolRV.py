#python dice roll
import random # for rolling dice with random numbers each time


print("Are you ready to roll the dice!!!") #prints out string statement
print("Welcome to the dice roll game..")   #print out the string statement
print("win with double on you dices")
roll_dice = input("play now!!, Enter y to play or n to quit.").lower() #calls the user to play or not
while roll_dice == "y":       #loop that allows the continous of game player
    print("dice will now roll")
    print("dice rolling...") #print out the staments
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6) #A random that will call a dice to roll between the min and max values chosen to be 1-6
    print("you rolled for>>") #Prints out string statement
    print("Roll1=" ,roll1 ,"\nRoll2=" ,roll2)
    if roll1 == roll2: # if what you rolled in either side is the same
        print("hooray!!, is a doble you win") #print string statements
    else:                         #if the values in both sides are different
        print("oops!try again") # print python statement
    roll_dice = input("continue playing? enter y to play or n to quit").lower() # this calls for user after the dice has been rolled to either quit or continue playing
    print("see you soon !!!bye")#prints string statement if user quits playing




