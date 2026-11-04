import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "weather.csv"))

print("Maximum temperature:", df["Temperature"].max())
print("Minimum temperature:", df["Temperature"].min())
print("Average temperature:", round(df["Temperature"].mean(), 2))

print("\nRecords where temperature is above 35 C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise average temperature:")
print(df.groupby("City")["Temperature"].mean().round(2))
