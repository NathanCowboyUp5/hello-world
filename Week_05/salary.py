"""
Program: salary.py
Author: Nathan Stroup

This program calculates the salary schedule inside a school district based on their
instructors' beginning payment, percentage rise, and scheduled years.

Program Steps
1. The inputs are:
    1. teacherStartingSalary
    2. salaryPercentageIncrease
    3. scheduledYearsValue
    
2. The salary rate is calculated by dividing the salary percentage rise by one hundred.
    1. salaryRate = salaryPercentageIncrease / 100.0        (Example: 2 / 100 = 0.02)
    
3. The salary table features the headers in tabular format:
    1. "Year"
    2. "Salary"
    
4. Computations:
    1. Inside a FOR loop, the teachers' beginning payment each year is calculated by multipling itself
        with the percentage rise value:
        1. teacherStartingSalary = teacherStartingSalary + (salaryRate * teacherStartingSalary)
"""

#User inputs for teachers' beginning payment, percentage rise, and scheduled years.
teacherStartingSalary = float(input("Please insert the teacher's beginning payment: "))
salaryPercentageIncrease = float(input("Please insert the salary percentage rise value: "))
scheduledYearsValue = int(input("Please insert the amount of scheduled years: "))

#Calculating salary percentage rise. (EX: 2 / 100 = 0.02)
salaryRate = salaryPercentageIncrease / 100.0

#Table year and salary headers.
print("%-10s%9s" % ("Year", "Salary"))

#Computing and outputting sthe schedule's complete teacher payments
for scheduledYearsValue in range(1, scheduledYearsValue + 1):
    print("%-7d $%11.2f" % (scheduledYearsValue, teacherStartingSalary))
    teacherStartingSalary = teacherStartingSalary + (salaryRate * teacherStartingSalary)

