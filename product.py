products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Cloths", 50),
    ("Mobile", "Electronics", 500)
]

total_price = 0
for product in products:
    name, category, price = product
    
    if category == "Electronics": 
        discounted_price = price * 0.80  
        total_price += discounted_price

print("Total Price:",total_price) 