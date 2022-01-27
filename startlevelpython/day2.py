print("Welcome to the tip calculator")
totalBill = input("What is the total Bill amount? ")
totalBill = int(totalBill)
numberPeople = input("How many people in the party? ")
numberPeople = int(numberPeople)
tipRate = input("What percent of tip that you want to tip ? 10, 15, 20? ")
tipRate = int(tipRate)
amountpaybyEachperson= ( totalBill*(1+tipRate/100))/numberPeople

print("Each person Should Pay: " + str(amountpaybyEachperson))
