"""
Program: minutes.py
Author: Nathan Stroup

This project receives an amounts of years from a user to determine how
many minutes pass in them.

Project Procedures:
1. Important constants
        1. Minutes in an hour
        2. Hours in a day
        3. Days in a year
2. The input is a set of years.
3. Computations:
        1. Annual Minutes = Minutes in an hour times hours in a day * the number of days in a year.
        2. Complete minutes in a specific range of years = a user's provided year(s)
                                times the annual amount of minutes.
                                            
4. The output is the amount of minutes in a set of years.
"""

#Crucial variables that identify how many minutes are in a year.
minutesPerHour = 60
hoursPerDay = 24
daysPerYear = 365

#User input request message for a specific year or time range.
yearsInputValue = int(input("Please provide a number of years: "))

#Calculate the complete minutes in a certain year or length of time.
yearlyMinutes = minutesPerHour * hoursPerDay * daysPerYear
totalMinutesInYears = yearsInputValue * yearlyMinutes

#Display how many minutes are in a particular year or time range.
print("The amount of minutes in", yearsInputValue, "year(s) is: ", totalMinutesInYears)
