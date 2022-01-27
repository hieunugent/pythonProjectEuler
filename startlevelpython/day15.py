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

def printreport(data, money):
    print("water: "+ str(data.get("water")))
    print("milk: "+ str(data.get("milk")))
    print("coffee: "+ str(data.get("coffee")))
    print("money: $"+ str(money))
# check if resource is ok
def set(a, b):
    a = b

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

def maintaince():
    return {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#  process coin

def canpurchase(total, price):
    if (total < price):
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True
def processcoin():
    print("please Insert your money")
    quaters = int(input("number of quaters: "))
    dimes = int(input("number of dimes: "))
    nickles= int(input("number of nickles: "))
    pennies = int(input("number of pennies: "))
    return quaters*.25 + dimes*0.1 + nickles*0.05 + pennies*0.01


# check transaction successfully
def updateresource(inventory, used):
    return {"water" : inventory.get("water") - used.get("water"),
             "milk" : inventory.get("milk") - used.get("milk"),
             "coffee" : inventory.get("coffee") - used.get("coffee")
             }
# make coffee
turnOn= True
earning = 0
while turnOn:
    choice = str(input("what would you like? (espresso/latte/cappuchino)"))
    if choice == "report":
        printreport(resources, money=earning)
        continue
    elif choice == "off":
        turnOn = False
        continue
    elif choice == "maintain":
        resources = maintaince()
        continue
    elif choice == "latte" or choice == "espresso" or choice =="cappuchino":
        cost = MENU.get(choice).get("cost")
        print("your " + choice + " cost $"+str(cost))
        

        totalmoney =processcoin() 
        cost = MENU.get(choice).get("cost")
        coffee = MENU.get(choice)
        materialcost =(coffee.get("ingredients"))
    if canpurchase(total=totalmoney, price=cost):
        if checkRecource(resource=resources, coffee=coffee):
            print("Here is your "+ choice + ", enjoy ")
            earning += cost
            resources = updateresource(resources, materialcost)
            if(cost < totalmoney):
                refund = round(totalmoney -cost,2)
                print("Here is your $"+ str(refund) + " change")

    
            


