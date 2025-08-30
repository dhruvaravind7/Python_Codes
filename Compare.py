def ifFunctiion():
    x= int(input("Enter a value for x: "))
    y= int(input("Enter a value for y: "))

    if (x>y):
        print(f"{x} is the greater value")
    elif(x<y):
        print(f"{y} is the greater value")
    else: 
        print("x and y are equal to each other")

def orFunctions():
    x= int(input("Enter a value for x: "))
    y= int(input("Enter a value for y: "))

    if (x>y) or (x<y):
        print("x and y are not equal to each other")
    else:
        print("x and y are equal to each other")

orFunctions()