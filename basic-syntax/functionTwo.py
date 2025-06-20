def add(x, y):
    return x+y


while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = add(num1, num2)
    print("Sum is: ", result)

    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() == "n":
        print("Exiting program...")
        break
