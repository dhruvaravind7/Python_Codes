def parity(num):
    return (True) if num % 2 ==0 else False


def main():
    num = int(input("Enter the number here: "))
    if (parity(num) == True):
        print(f"The nummer {num} is even")
    else:
        print(f"The number {num} is odd")



main()