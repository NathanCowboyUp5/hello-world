"""
Project: bouncy.py
Author: Nathan Stroup

This program computes a ball's traveled distance inside a FOR loop
based on a its provided original height and how many times it bounces.

Program Steps:
1. The inputs are a ball's height value and how long it can bounce for.
    1. ballHeightValue
    2. ballBounceValue
    
2. Crucial variables include:
    1. ballBounceIndexNumber = 0.6
    2. ballTotalDistanceTraveledValue = ballHeightValue
    3. ballCurrentHeight = ballHeightValue
    
3. Computations (inside a FOR loop):
    1. ballBounceHeight = ballBounceIndexNumber * ballCurrentHeight
    2. ballTotalDistanceTraveledValue += 2 * ballBounceHeight
    3. ballCurrentHeight = ballBounceHeight
    
4. The output is the ball's complete distanced traveled.

"""
#User input requests for the height where the ball was released and how long it can bounce for.
ballHeightValue = float(input("Please insert the original height the ball was released from: "))
ballBounceValue = int(input("Please insert the amount of bounces the ball can continue for: "))

#A ball's bounce index variable.
ballBounceIndexNumber = 0.6

#A ball's active height and traveled distance variables.
ballCurrentHeight = ballHeightValue
ballTotalDistanceTraveledValue = ballHeightValue

#Computing the ball's total distance inside a FOR loop based on its provided amount of bounces.
for bounces in range(ballBounceValue):
    ballBounceHeight = ballBounceIndexNumber * ballCurrentHeight
    ballTotalDistanceTraveledValue += 2 * ballBounceHeight
    ballCurrentHeight = ballBounceHeight

#Output the ball's traveled distance.
print("The ball's complete distance traveled is", ballTotalDistanceTraveledValue, "feet.")
