
# Your magic Python code here

import math

def cashToCoins():
    dollarAmount = 8.69
    piggyBank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }

    piggyBank["quarters"] = int(dollarAmount // .25)
    print(dollarAmount)
    dollarAmount -= piggyBank["quarters"] * .25
    print(piggyBank["quarters"] * .25)
    print(dollarAmount)

    piggyBank["dimes"] = int(dollarAmount // .10)
    dollarAmount -= piggyBank["dimes"] * .10

    piggyBank["nickels"] = int(dollarAmount // .05)
    dollarAmount -= piggyBank["nickels"] * .05

    piggyBank["pennies"] = int(dollarAmount / .01)
    

    print(piggyBank)


cashToCoins()
