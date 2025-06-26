# visualization_d_monthly_sales.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_superstore_data.csv")

# Ensure 'Order Date' is in datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Group sales by month
monthly_sales = df.resample('M', on='Order Date')["Sales"].sum()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, marker="o", color="royalblue")

plt.title("📆 Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig("plots/visualization_d_monthly_sales.png")
plt.show()
