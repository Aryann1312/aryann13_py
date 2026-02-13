sales = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]

totals = {}
for product, qty in sales:
    if product in totals:
        totals[product] += qty
    else:
        totals[product] = qty

max_qty = 0
max_product = ""
for product, qty in totals.items():
    if qty > max_qty: 
        max_qty = qty
        max_product = product

print(max_product)