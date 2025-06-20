print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")

# choice = input("Enter your choice: ")
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if choice == "1":
#     print(num1+num2)
# if choice == "2":
#     print(num1-num2)
# if choice == "3":
#     print(num1*num2)
# if choice == "4":
#     print(num1/num2)

option = int(input("Enter your choice: "))
if (option in [1,  2, 3, 4]):

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if option == 1:
        result = num1+num2
    if option == 2:
        result = num1-num2
    if option == 3:
        result = num1*num2
    if option == 4:
        result = num1//num2

else:
    print("Invalid input is")
