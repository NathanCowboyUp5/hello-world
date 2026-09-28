"""
Project: population.py
Author: Nathan Stroup

This project focuses on predicting an organism's future population count through a while loop based on a user's
provided amount of organisms, growth rate, hours that is needed to accomplish that rate, and
the population growth hours. 

Program Steps:
1. The inputs are:
    1. organismNumberValue
    2. organismGrowthRateValue
    3. achievableGrowthHoursRateValue
    4. populationGrowthHoursValue
    
2. Significant constants include:
    1. completeOrganismPopulation= organismNumberValue
    2. currentHoursNumber = 0.0
    
3. Computations inside the while loop:
    1. completeOrganismPopulation times organismGrowthRateValue
    2. currentHoursNumber (0.0) plus achievableHoursRateValue

4. The output is the predicted organism population.
"""

#User input requests for an amount of organisms, growth rate value, hours to meet that rate, and final population growth hours.
organismNumberValue = float(input("Please insert an amount of organisms: "))
organismGrowthRateValue = float(input("Please insert the growth rate value (bigger than zero): "))
achievableGrowthHoursRateValue = float(input("Please insert the amount of hours required to accomplish this growth rate: "))
populationGrowthHoursValue = float(input("Please insert the complete population growth hours: "))

#Total organism population and current hours variables.
completeOrganismPopulation = organismNumberValue
currentHoursNumber = 0.0

#Computing the organism's future population inside a while loop.
while currentHoursNumber  + achievableGrowthHoursRateValue <= populationGrowthHoursValue:
    completeOrganismPopulation *= organismGrowthRateValue
    currentHoursNumber += achievableGrowthHoursRateValue

#Output the predicted organism population.
print("The total population is predicted to be", completeOrganismPopulation, "organisms.")

