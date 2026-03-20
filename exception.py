try:
    num1 = int(input("Enter you first number:"))
    num2 = int(input("Enter you second number:"))

    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")