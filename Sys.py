import sys
while True:
    try:
        print("Hello my name is", sys.argv[1])
    except:
        print("Enter your name: ")
    else:
        break