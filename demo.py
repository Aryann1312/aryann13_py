def greet():    
    print("Hello World!!")

def decidePerson():    
    age_of_person = input("Enter person's AGE:")

    if age_of_person < 18:
        print("Teenager!")
    elif age_of_person >=18 and age_of_person <60:
        print("Adult!")
    else:
        print("Senior Citizen!")

def main():
    greet()
    decidePerson()
