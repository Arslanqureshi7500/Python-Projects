#Adding
from art import logo
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
    }


def calculator():
    print(logo)
    num1 = float(input("What's first number? : "))
    for symbol in operations:
        print(symbol)    
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's next number? : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer},or type 'n' start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            
calculator()