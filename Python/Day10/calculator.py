import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def print_operations():
    print("+\n-\n*\n/")

def calc(n1, n2, operation):
    if operation == '+':
        return add(n1, n2)
    elif operation == '-':
        return subtract(n1, n2)
    elif operation == '*':
        return multiply(n1, n2)
    elif operation == '/':
        return divide(n1, n2)
    else:
        return
    
calculate = True

while calculate == True:

    current_calc = True
    num1 = float(input("What's the first number?: "))
    res = 0

    while current_calc == True:

        print_operations()
        op = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        res = calc(num1, num2, op)

        print(f"{num1} {op} {num2} = {res}")
        current_calc = not (input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ") == 'n')
        
        if current_calc:
            num1 = res

    os.system('cls')
    calculate = not current_calc
