customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]

total_revenue = 0

for customer in customers:
    if customer["active"]:  # Only active customers
        for amount in customer["purchases"]:
            if amount >= 100:  # Ignore purchases less than 100
                total_revenue += amount * 1.10  # Add 10% tax

print("Total Revenue:",total_revenue)