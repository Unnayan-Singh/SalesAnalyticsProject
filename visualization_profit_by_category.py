# visualization_profit_by_category.py

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Aggregate profit by category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    category_profit, 
    labels=category_profit.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Set3.colors
)
plt.title("📊 Profit Contribution by Category")
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.
plt.tight_layout()

# Save plot
plt.savefig("plots/visualization_profit_by_category.png")
plt.show()
