import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005],
    "Customer": ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],
    "Product": ["Headphones", "Backpack", "Smartwatch", "Water Bottle", "Tablet"],
    "Quantity": [2, 1, 1, 5, 2],
    "Price": [2500, 1800, 6500, 400, 9000],
    "Discount": [200, 100, 500, 0, 1000],
}

df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:")
print(df)

print("\nOrders above Rs. 5,000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage order value:", df["Final_Amount"].mean())
