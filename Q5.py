sales = [("Pen", 10), ("Pencil", 5), ("Pen", 15)]

total_sales = {}

for product, quantity in sales:
    if product in total_sales:
        total_sales[product] = total_sales[product] + quantity
    else:
        total_sales[product] = quantity

print(total_sales)