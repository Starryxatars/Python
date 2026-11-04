import pandas as pd

sales_data = {
    "Product_ID": [1, 2, 3, 4, 5, 6],
    "Product_Name": ["Rice Bag", "Cooking Oil", "Sugar", "Tea Powder", "Detergent", "Biscuits"],
    "Category": ["Grocery", "Grocery", "Grocery", "Beverages", "Household", "Snacks"],
    "Price": [1200, 180, 45, 320, 250, 30],
    "Quantity": [15, 40, 120, 25, 30, 200],
}


df = pd.DataFrame(sales_data)
print("Sales DataFrame:")
print(df)


df["Total_Sales"] = df["Price"] * df["Quantity"]
print("\nDataFrame with Total_Sales:")
print(df)


print("\nProducts with sales greater than Rs. 10,000:")
print(df[df["Total_Sales"] > 10000])


print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])


print("\nAverage sales:", df["Total_Sales"].mean())
