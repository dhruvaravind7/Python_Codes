def main():
    x= GetInt("What is x: ")
    print(f"x is {x}")

def GetInt(prompt):
    while True:
        try:
            x = int(input(prompt))
            break
        except ValueError:
            pass

    return x

main()