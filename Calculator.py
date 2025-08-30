import Calculator_Art

print(Calculator_Art.logo)

def add(num1, num2):
    return (num1 + num2)

def multiply(num1, num2):
    return(num1 * num2)

def subtract(num1, num2):
    return(num1 - num2)

def divide(num1, num2):
    return(num1/num2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
while True:
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))
    while True:
        for symbol in operations:
            print(symbol)
        operationSymbol = input("Enter an operation from the line above: ")

        oper = operations[operationSymbol]
        sum = oper(num1, num2)
        print(f"{float(num1)} {operationSymbol} {float(num2)} = {float(sum)}")
        persist = input(f"Type 'y' to continue calculating with {sum}, or type 'n' to start a new calculation: ")
        if persist == "n":
            break
        else:
            num2 = int(input("What's the second number: "))
            num1 = sum
        

