def convert_to_inr(product):
    name = product[0]
    price_usd = product[1]
    return (name, price_usd * 83)

def is_expensive(product):
    return product[1] > 3000

def convert_n_filter_products(products):
    converted = list(map(convert_to_inr, products))
    print("Converted prices:", converted)

    filtered = list(filter(is_expensive, converted))
    return filtered

def main():
    products = [
        ("Pen", 10),
        ("Bag", 50),
        ("Shoes", 60)
    ]

    result = convert_n_filter_products(products)
    print("Final Result:", result)

if __name__ == "__main__":
    main()