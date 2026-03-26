# P3LAB_SealJoseph
# Program Description:
# This program takes a monetary amount as input and calculates the most efficient
# number of dollars, quarters, dimes, nickels, and pennies needed to make that amount.

# Get user input
amount = float(input("Enter the amount of money: "))

# Convert to cents
cents = int(round(amount * 100))

# Calculate denominations
dollars = cents // 100
cents = cents - (dollars * 100)

quarters = cents // 25
cents = cents - (quarters * 25)

dimes = cents // 10
cents = cents - (dimes * 10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

# Output results (only if > 0, handle singular/plural)
if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(dollars, "Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(quarters, "Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(dimes, "Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(nickels, "Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(pennies, "Pennies")
