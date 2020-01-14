# Turn you cash into coins

def cashToCoins():

    dollarAmount = 8.69

    #Convert dollars to whole number cuz python ain't got time for decimals
    dollarAmount *= 100
    
    #Initialize dictionary
    piggyBank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }

    #Use integer division to get coin totals and subtract value as you 
    #decrease in denomination 
    piggyBank["quarters"] = int(dollarAmount // 25)
    dollarAmount -= piggyBank["quarters"] * 25
    
    piggyBank["dimes"] = int(dollarAmount // 10)
    dollarAmount -= piggyBank["dimes"] * 10

    piggyBank["nickels"] = int(dollarAmount // 5)
    dollarAmount -= piggyBank["nickels"] * 5

    piggyBank["pennies"] = int(dollarAmount / 1)
    
    print(piggyBank)

cashToCoins()
