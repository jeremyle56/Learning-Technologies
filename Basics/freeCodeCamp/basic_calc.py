
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Enter which operation you would like to use: ")

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("You must enter one of the following operations '+', '-', '*', '/'")