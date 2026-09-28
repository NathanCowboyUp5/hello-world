"""
Program: employeepay.py
Author: Nathan Stroup

This project computes a worker's complete weekly pay based on their
hourly payment, work hours, and overtime hours.

Program Steps:
1. The inputs are comprised of an employee's hourly payment, regular job hours, and complete overtime hours.
2. Computations:
    1. An employee's total overtime wage = their normal work hours times their hourly salary times one and a half.
    2. An employee's complete weekly payment = their hourly wage times their regular job hours plus
                their overtime payment, which is all rounded by two.
3. The output is a worker's total weekly salary.

"""

#User input request messages for their hourly payment, work hours, and overtime wage.
employeeHourlyWage = float(input("Please insert the hourly wage: "))
employeeTotalRegularHours = float(input("Please insert the complete regular works: "))
employeeTotalOverTimeHours = float(input("Please insert the complete overtime hours: "))

#Employee overtime and weekly payment formulas
employeeTotalOverTimePay = employeeTotalOverTimeHours * (employeeHourlyWage * 1.5)
employeeTotalWeeklyPay = round(employeeHourlyWage * employeeTotalRegularHours + employeeTotalOverTimePay, 2)


#A worker's complete weekly payment results are displayed
print("The complete weekly payment is $", employeeTotalWeeklyPay)
