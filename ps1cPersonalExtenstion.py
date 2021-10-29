# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:26:11 2021

@author: jessi
"""

# I want to make some modifications to ps1c, so that people can input their
# own max house cost, their salary, their semi-annual raise, their goal months
# and maybe even their max saving potential, and it will give them the results
# and outputs of their scenarios, ie tell them if it's possible or not.
# it assumes an annual raise of 3%
""" This is a personal extension of assignment ps1 """


house = float(input("What's the max you will spend on a house?"))
down_payment = house * (float(input("As a decimal, what percent of the sales price"
                                    " will you save as a down payment? ex: .25")))
goal = float(input("How many months do you want it to take to save for a down payment?"))
salary = float(input("What's your annual salary?"))
print("The down payment amount you're wanting to reach is", down_payment)
budget_min = float(input("What's the minimum amount of dollars you need each"
                         " month to pay for your essentials?"))
savings_rate = 0
payday = float(salary) / 12


def s(savings_rate, salary):
    savings = 0
    month = 0
    epsilon = .01
    r = 0.04 / 12
    semi_annual_raise = .07
    for i in range(36):
        month += 1
        payday = salary / 12
        if month % 6 == 0:
            payday = payday + (semi_annual_raise * payday)
        savings = (savings + (payday * (savings_rate * epsilon**2))) + ((savings + (payday * (savings_rate * epsilon**2))) * r)
    return savings


def p(salary):
    semi_annual_raise = .07
    month = 0
    for i in range(36):
        month += 1
        if month % 6 == 0:
            payday = (semi_annual_raise * salary) / 12
        print(payday, "is payday")


epsilon = .01
savings = 0
numGuesses = 0
low = 0
high = 10000
while abs(savings - down_payment) > 100 and numGuesses <= 1000:
    numGuesses += 1
    savings_rate = (high + low) / 2
    savings = s(savings_rate, salary)
    if savings - float(down_payment) >= 100:
        high = savings_rate
    else:
        low = savings_rate
    savings_rate = (high + low) / 2
if abs(savings - down_payment) < 100:
    if (savings_rate * epsilon**2 * payday) > (payday - budget_min):
        print("The savings rate required to save for a down payment of", down_payment,
              "in", goal, "months", "isn't possible with the cost of", 
              budget_min, "essentials")
    else: print("savings rate is", savings_rate * epsilon**2, "of your salary",
                "or", savings_rate * epsilon**2 * payday, "each month.")
else:
    print("On this salary, it's not possible to save for a 25% down_payment"
          " within", goal, "months")
print("Steps in bisection search:", numGuesses)
