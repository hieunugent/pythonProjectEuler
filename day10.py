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
def calculator():
    num1 = float(input("please enter the first number: "))
    for char in operations:
        print(char)
    exit = False
    while not exit:
        operations_symbol = input("Pick an Operation: ")
        num2 = float(input("what is your next number? "))
        calculator_function = operations[operations_symbol]
        result = calculator_function(num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {result} ")
        wantcontinue = input(f"Type 'y' if you want to continue with {result} type 'rs' to reset or 'exit' to exit ").lower()
        if(wantcontinue =="y" or wantcontinue=="yes"):
            num1 = result
        elif wantcontinue=='rs':
            exit = True
            calculator()
        elif wantcontinue=='exit':
            exit = True
        
calculator()