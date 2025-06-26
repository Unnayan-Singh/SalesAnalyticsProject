# visual_profit_vs_sales.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_superstore_data.csv")

# Set up the plot
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# Scatter plot: Profit vs Sales
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category", palette="coolwarm", alpha=0.7)

plt.title("💹 Profit vs Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.legend(title="Category")
plt.tight_layout()

# Save the figure
plt.savefig("plots/visual_profit_vs_sales.png")
plt.show()
