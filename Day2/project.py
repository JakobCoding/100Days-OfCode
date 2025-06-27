# Build a Tip Calculator 
# First Attempt 

print("Welcome to the tip caluculator!")
totalBill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
splitBetween = input("How many People to split the bill? ")

floatBill = float(totalBill)
floatTip = float(tip)
tipPercentage = floatTip / 100
actualTip = floatBill * tipPercentage
intSplitBetween = int(splitBetween)

splitTip = (floatBill + actualTip) / intSplitBetween
splitTipRound = round(splitTip, 2)

print(f"Each person should pay: ${splitTipRound}")