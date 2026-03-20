class ZeroDivisionError(Exception):
    pass
try:
    e = int(input("Enter you first number:"))
    num2 = int(input("Enter you second number:"))

    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError as e:
    print("Error:",e)