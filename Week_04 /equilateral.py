"""
Program: equilateral.py
Author: Nathan Stroup

This project receives a triangle's three length values to identify
if they make an equilateral triangle.

Project Steps:
1. The user inputs include a triangle's three side lengths values.
2. Computations:
    A triangle's three values being compared inside an "if-else" statement on whether they equal each other.
            triangleLengthValueOne == triangleLengthValueTwo == triangleLengthValueThree
3. The output is a statement about whether a user's provided values form an equilateral triangle or not.
"""

#User input requests for triangle side lengths.
triangleLengthValueOne = float(input("Please insert the first triangle side length value: "))
triangleLengthValueTwo = float(input("Please insert the second triangle side length value: "))
triangleLengthValueThree = float(input("Please insert the third triangle side length value: "))
                             
#Computing whether the values are equal to each other and output statements.
if triangleLengthValueOne == triangleLengthValueTwo == triangleLengthValueThree:
    print("These values create an equilateral triangle.")
else:
    print("These values do not create an equilateral triangle.")


