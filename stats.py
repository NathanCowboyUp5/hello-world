"""
Project: stats.py
Author: Nathan Stroup

This program specializes in designing a function collection for a university's statisticians
group that determine a number set's median and mode. Moreover, the project determines
these values' average inside a "mean" module. Every function must possess an argument
of a digit list and output one number. However, if a value set is not present, they return
the value zero ("0"). This project also features a "main" group, where a provided catalog's three
statistical methods are reviewed.

Program Steps:
1. Critical Variables include:
    1. numberSetValues = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 9, 11]
    2. returnValueZero = 0
2. Computations:
    1. A number group's mode inside the "mode(numberSetValues)" function:
        1. If the college's number list is not made, zero is outputed as the mode.
        2. If a college value group is present, the mode is calculated by determining its
            highest digit. A dictionary about the number set's counts is created ("numberSetCounts"), which
            examines how many digits appear. In an if-else statement, when one repeatedly appears, it is added by one. However,
            if is viewed once, it remains one.
        3. The number list's maximum item is within its highest counted items, which are assigned to the ".values()" tool.
        4. For every digit inside this list, if its counts[numberKey] are equal to the highest value, its key is returned.
    2. A value set's  median through its "median(numberSetValues)" function:
        1. When the school's digit collection is not present, zero becomes the median.
        2. If a the campus' number list is present, its midpoint is determined by
            dividing its items (inside a "len()" tool) over 2.
            1. if the value group's items(within the "len()" feature) are formatted in an odd digit-based manner:
                1. Its midpoint is returned as the median.
            2. else:
                1. The list's even results are outputed, which is determined by adding its items'
                    midpoint value and numbers (through its middle value minus one) divided by 2.)
        
            3. A digit group's average (mean) within a "mean(numberSetValues)" function:
              1. If a university's number list is not designed, zero is labeled as the average.
               2. If a value list is created, the mean is computed by dividing its sum over
                                the complete amount of items through the len() tool.
5. The outputs are (The list outputs as "[]", while its median, average,
                    and mode as zero ("0"), if its numbers are not made):
    1. The college's tested number list.
    2. The number list's median.
    3. The number list's average (mean).
    4. The number list's mode.
"""

#Critical variables
numberSetValues = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 9, 11]     #An example of the college's digit list.
returnValueZero = 0

#Determining the number set's mode
def mode(numberSetValues):
    if not numberSetValues:
        return returnValueZero
    numberSetCounts = {}
    for number in numberSetValues:
        if number in numberSetCounts:
            numberSetCounts[number] += 1
        else:
            numberSetCounts[number] = 1

    maximumNumberValue = max(numberSetCounts.values())
    for numberKey in numberSetCounts:
        if numberSetCounts[numberKey] == maximumNumberValue:
            return numberKey

#Calculating the number set's median.
def median(numberSetValues):
    if not numberSetValues:
        return returnValueZero

    #Determining the list's median.
    numberMidPoint = len(numberSetValues) // 2
    if len(numberSetValues) % 2 == 1:
        return numberSetValues[numberMidPoint]
    else:
        numberSetEvenMedianResults = (numberSetValues[numberMidPoint] +
                                              numberSetValues[numberMidPoint - 1]) / 2
        return numberSetEvenMedianResults
    
#The mean() function, which calculates the number group's average
def mean(numberSetValues):
    if not numberSetValues:
        return returnValueZero
    return sum(numberSetValues) / len(numberSetValues)

#The main() function that runs the median, mode, and average through a provided list.
def main():
    print("The tested number set is: ", numberSetValues)
    print("The number set's median is: ", median(numberSetValues))
    print("The number set's average is: ", mean(numberSetValues))
    print("The number set's mode is: ", mode(numberSetValues))
    return
main()
