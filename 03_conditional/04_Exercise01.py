# Exercise number guessing game
# Make a variable , like winning_number and assign any number to it.
# Ask user to guess a number
# if user gussed correctly then print "YOU WIN !!!!"
# If user did't guessed correctly then:
    #if user guessed lower than actual number then print "too low"
    #if user guessed higher than actual number than print "too high"

# google "how to generate random number in python " to generate random 
#  Winning number
import random

winnning_number = random.randint(1,5)
guess_Number = int(input("Enter a number"))
if guess_Number == winnning_number:
    print("YOU WIN !!!")
else:
    if(guess_Number < winnning_number):
        print("To low")
    else:
        print("too high")     

        #    nested if else concept is applied here
