def main():
    #CreateBarrier(4)
    #CreateRow(4)
    CreateSquare(3)

def CreateBarrier(height):
    for i in range(height):
        print("#")

def CreateRow(width):
    print("#" * width)

def CreateSquare(length):
    for i in range(length):
        CreateRow(length)

main()