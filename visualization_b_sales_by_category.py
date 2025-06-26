# visualization_b_sales_by_category.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_superstore_data.csv")

# Aggregate total sales by Category
category_sales = df.groupby("Category")["Sales"].sum().reset_index().sort_values("Sales", ascending=False)

# Plot
plt.figure(figsize=(8, 6))
sns.barplot(data=category_sales, x="Category", y="Sales", hue="Category", legend=False, palette="pastel")

plt.title("📊 Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the plot
plt.savefig("plots/visualization_b_sales_by_category.png")
plt.show()
