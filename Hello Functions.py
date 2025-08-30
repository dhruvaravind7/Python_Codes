def main():
    hello()
    name = input("Enter your name here: ").strip().capitalize()
    hello(name)

def hello(name="world"):
    print(f"Hello, {name}")


main()