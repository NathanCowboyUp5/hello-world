"""
Program: sphere.py

This project records the input of a sphere's radius
to output its diameter, surface area, circumference, and volume.

"""

radius = int(input("Please insert the radius of the sphere:"))
diameter = 2 * radius
circumference = 2 * 3.14 * radius
surfaceArea = 4 * 3.14 * radius ** 2
volume =  4 / 3 * 3.14 * radius ** 3
print("The volume of the sphere is", volume)
print("The diameter of the sphere is", diameter)
print("The cirumference of the sphere is", circumference)
print("The surface area of the sphere is", surfaceArea)
