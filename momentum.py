"""
Program: momentum.py

This project receives an item's velocity (based on meters per second)
and mass (through kilograms) to determine its momentum.

"""

itemMassValue = float(input("Please insert the item's mass in kilograms: "))
itemVelocityValue = float(input("Please insert the item's velocity in meters: "))
itemMomentum = itemMassValue * itemVelocityValue
print("The item's momentum is:", itemMomentum ,"kg*m/s ")
