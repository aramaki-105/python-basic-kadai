def get_tax(price, tax):
    totale = price + price * (tax / 100)
    return totale


totale_price = get_tax(1200, 10)

print(f"{price}円 (税込){totale_price}円")
