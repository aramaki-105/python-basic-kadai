def get_tax(price, tax):
    return price + price * (tax / 100)

totale_price = get_tax(1200, 10)

print(f"(税込){totale_price}円")