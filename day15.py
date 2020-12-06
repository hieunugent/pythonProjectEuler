MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# print report
money = 102
def printreport(data):
    print("water: "+ str(data.get("water")))
    print("milk: "+ str(data.get("milk")))
    print("coffee: "+ str(data.get("coffee")))
    print("money: $"+ str(money))
# check if resource is ok
def checkRecource(resource, coffee):
    if resource.get("water") < coffee.get("ingredients").get("water"):
        print("Sorry, there is not enough water")
        return False
    elif resource.get("milk") < coffee.get("ingredients").get("milk"):
        print("Sorry, there is not enough milk")
        return False
    elif resource.get("coffee") < coffee.get("ingredients").get("coffee"):
        print("Sorry, there is not enough coffee")
        return False
    else:
        return True

#  process coin

def canpurchase(total, price):
    if (total < price):
        return False
    return True
def processcoin(quaters, dimes, nickles, pennies):
    return quaters*.25 + dimes*0.1 + nickles*0.05 + pennies*0.01


# check transaction successfully
# make coffee
turnOn= True

while turnOn:
    choice = str(input("what would you like? (espresso/latte/cappuchino)"))
    if choice == "report":
        printreport(resources)
        continue
    if choice == "off":
        turnOn = False
        continue

    print("please Insert your money")
    quaters = int(input("number of quaters"))
    dimes = int(input("number of dimes"))
    nickles= int(input("number of nickles"))
    pennies = int(input("number of pennies"))

    totalmoney =processcoin(quaters, dimes, nickles, pennies) 
    cost = MENU.get(choice).get("cost")
    coffee = MENU.get(choice)
    if canpurchase(total=totalmoney,price=cost):
        if checkRecource(resource=resources, coffee=coffee):
              print("Here is your "+ choice + ", enjoy ")
              if(cost < totalmoney):
                  refund = round(totalmoney -cost,2)
                  print("Here is your $"+ str(refund) + " change")
    else:
        print("Sorry that's not enough money. Money refunded.")
    


