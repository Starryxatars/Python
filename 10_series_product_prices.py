import pandas as pd

price_dict = {"Laptop": 55000, "Mouse": 500, "Keyboard": 1200, "Monitor": 9000, "Pen Drive": 800}
prices = pd.Series(price_dict)

print("Products and prices:")
print(prices)

increased = prices * 1.10
print("\nPrices after 10% increase:")
print(increased)

print("\nMost expensive product:", prices.idxmax(), "-", prices.max())

print("\nProducts costing more than Rs. 1,000:")
print(prices[prices > 1000])
