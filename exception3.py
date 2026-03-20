class nagatttiveNumberError(Exception):
    pass
try:
    num = int(input("Enter a positive number:"))
    if num < 0:
        raise nagatttiveNumberError("Negative numbers are not allowed.")
    print("You entered:", num)      
except nagatttiveNumberError as e:
    print("Error:", e)      