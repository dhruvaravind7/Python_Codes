def whileLoop():
    i = 0
    while i < 3:
        print("Meow")
        i +=1

def forLoop():
    for _ in range(3):
        print("Meow")

def UserLoop():
    iter = 0
    while (iter <= 0 ):
        iter = int(input("Enter the number of meows here: "))
    for _ in range(iter):
        print("Meow")

UserLoop()
