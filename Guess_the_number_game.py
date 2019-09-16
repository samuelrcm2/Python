# using codeSkulpter

import simplegui
import random

global sortedValue;

def new_game():
    print("new game")

def range_of_100():
    sortedValue = random.randrange(0,100)
    print("your range is 0-100")

def range_of_1000():
    sortedValue = random.randrange(0,1000)
    print("range is 0-1000")

def compareGuess(guess):
    num1 = int(guess)
    if num1 == sortedValue:
        return "Correct";
    elif num1 > sortedValue:
        return "Greater";
    elif num1 < sortedGues:
        return "Lower";

def printGuess(guess):
    print("Your Guess is " , guess)
    answer = compareGuess(guess)
    print(answer)

frame = simplegui.create_frame("Guess The Number",200,200)
frame.add_button("range[0-1000)",range1000)
frame.add_button("range[0-100)",range100)
frame.add_input("enter your guess",input_guess,200)
frame.start()
new_game()
