"""
Program: tidbit.py
Author: Nathan Stroup

This program focuses on computing a loan's duration and salary timeline based on a user's
provided purchase price.

Project Steps
1. The input is a purchase price.

2. Crucial variables in this program are:
    1. currentMonth
    2. annualInterestRate
    3. monthlyInterestRate
    4. downPaymentValue
    5. monthlySalary
    6. beginningBalance
    7. currentBalance = beginningBalance

3. Compute loan lifetime (Inside a WHILE loop):
    1. monthlyInterest = round(currentBalance * (annualInterestRate / 12), 2)
    2. inside an IF-ELSE statement:
        1. if:
            1. Left over payment = 0.0
            2. Monthly salary equals monthly interst owed + current balance, which is rounded by two.
            3. Monthly principal equals current balance, which is rounded by two.
        2. else:
            1. Monthly principal owed equals monthly salary - monthly interest owed, which is rounded by two.
            2. Left over payment = current balance - monthly principal owed, which is rounded by two.
            
4. The top outputs are: purchaseValue, downPaymentValue, monthlySalary, and beginningBalance

5. The bottom outputs are: currentMonth, currentBalance, monthlyInterestOwed, monthlyPrincipalOwed, monthlySalary, and leftoverPayment
"""

#User input statement regarding purchase cost.
purchasePrice = float(input("Please insert the purchase price value: "))

#Crucial variables
currentMonth = 1                                                        #Current Month
annualInterestRate = 0.12                                               #Annual Interest Rate
monthlyInterestRate = round(annualInterestRate / 12, 2)                 #Monthly interest rate
downPaymentValue = round(0.10 * purchasePrice, 2)                       #Down Payment
monthlySalary = round(0.05 * (purchasePrice - downPaymentValue), 2)     #Monthly Payment
beginningBalance = round(purchasePrice - downPaymentValue, 2)           #Starting Salary
currentBalance = round(beginningBalance, 2)                             #Active Salary

#OUTPUT First Values
print("The purchase price is: $", purchasePrice)
print("The down payment is (10% Rate): $", downPaymentValue)
print("The monthly payment is (5% Rate): $", monthlySalary)
print("The beginning balance is: $", beginningBalance)

#Print Statement that Separates Outputted Values
print()

#Table Headers
print("%-10s%7s%27s%28s%20s%23s" % ("Month", "Salary", "Monthly Interest", "Monthly Owed Principal", "Monthly Salary", "Leftover Payment"))
print("-" * 115)
                                                        
#Calculating a loan's lifetime
currentBalance = beginningBalance
currentMonth = 1
while currentBalance > 0:
    monthlyInterestOwed = round(currentBalance * (annualInterestRate / 12), 2) #Monthly Interest Provided
    
    if monthlyInterestOwed + currentBalance < monthlySalary:
        leftOverPayment = 0.0                                                 #Leftover balance
        monthlySalary = round(monthlyInterestOwed + currentBalance, 2)        #Monthly Payment
        monthlyPrincipalOwed = round(currentBalance, 2)                       #Monthly Principal Owed
    else:
        monthlyPrincipalOwed = round(monthlySalary - monthlyInterestOwed, 2)  #Monthly Principal Owed
        leftOverPayment = round(currentBalance - monthlyPrincipalOwed, 2)     #Leftover balance

#Tabular Outputs and WHILE loop Repeat Statements
    print("%-10s%2s%7s%13s%7s%16s%7s%21s%6s%15s%5s" % (currentMonth, "$",currentBalance, "$", monthlyInterestOwed, "$",monthlyPrincipalOwed, "$", monthlySalary, "$", leftOverPayment))
    currentBalance = leftOverPayment
    currentMonth += 1

