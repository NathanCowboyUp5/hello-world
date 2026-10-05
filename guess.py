"""
Project: guess.py
Author: Nathan Stroup

This project allows a computer to theorize a random number through a series of
guesses. The minimum amount of attempts are outputted by the "math.log" tool when
the higher and lower values are provided.

Program Steps:
1. Imported functions are:
    1. import random
    2. import math

2. The inputs are:
    1. smallerNumber
    2. largerNumber
    
3. Computations:
    1. Predicted minimum guesses = math.log2(larger - smaller +1), which is rounded by "math.ceil" function.
    2. count = count + 1 (Increments in each attempt)
    3. smaller = computer's number prediction + 1 (If mystery number is too small).
    4. larger = computer's number prediction - 1 (If mystery number is too high).

4. The output is:
    1. count (Number of Attempts Computer Took to Find the Mystery Number)
    2. "Unusable item. Please state Please state either 'Yes', 'High', or 'Low' (If neither of these items are entered).
    3. "Your numbers are inconsistent! You are cheating!" (If smaller > larger)
"""

#Imported functions
import random
import math

#User input statements for small and large values.
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
if smaller > larger:
    smaller, larger = larger, smaller
    
#Calculating minimum guesses
predictedMinimumGuesses = math.ceil(math.log2(larger - smaller + 1))
print()
print("The computer has", predictedMinimumGuesses, "attempts to guess your number")
print()

#Calculating the mysterious number
count = 0
while smaller <= larger:
    if count >= predictedMinimumGuesses:
        print("The computer has exceeded its minimum guess limit. Please try again.")
        break
    
    computerPrediction = (larger + smaller) // 2      #This finds the midpoint between the larger and smaller values.
    
    print("The computer thinks", computerPrediction, "is your value.")
    clue = input("Please say 'Yes' if it is correct. If not, please say 'High' for too large, or 'Low' for too small: ")

    #IF-ELSE statement that Determines the User's Value
    if clue == "Yes":
        print("Congratulations! The computer guessed your number in", count + 1, "attempts!")
        break
    elif clue == "High":
        larger = computerPrediction - 1
        print("Too large")
    elif clue == "Low":
        smaller = computerPrediction + 1
        print("Too small")
    else:
        print("Unusable item. Please state either 'Yes', 'High', or 'Low'.")
        count -= 1
    
    #Loop that stops cheaters from entering inconsistent hints.
    if smaller > larger:
        print("Your numbers are inconsistent! You are cheating!")
        break
    count += 1

