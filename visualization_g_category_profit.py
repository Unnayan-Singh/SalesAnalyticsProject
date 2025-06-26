# visualization_g_category_profit.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Total profit by category
category_profit = df.groupby("Category")["Profit"].sum().sort_values()

# Plot
plt.figure(figsize=(8, 6))
sns.barplot(x=category_profit.values, y=category_profit.index, palette='flare')
plt.title("💰 Profit by Category")
plt.xlabel("Total Profit")
plt.ylabel("Category")
plt.tight_layout()

# Save plot
plt.savefig("plots/visualization_g_category_profit.png")
plt.show()
