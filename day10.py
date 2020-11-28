from art import logocal
print(logocal)

def add(a , b ):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def devide(a, b):
    return a/b
operations = {
    "+": add,
    "-": subtract,
    "/":devide,
    "*": multiply,
}

num1 =int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))
for char in operations:
    print(char)
operations_symbol= input("please enter the symbol below: ")
calculator_function = operations[operations_symbol]
firstAnswer = calculator_function(num1,num2)
print(f"{num1} {operations_symbol} {num2} = {firstAnswer}")

