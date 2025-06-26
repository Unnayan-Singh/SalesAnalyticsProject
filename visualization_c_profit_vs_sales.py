# visualization_c_profit_vs_sales.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category", palette="Set2", alpha=0.7)

plt.title("📈 Profit vs Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.legend(title="Category")
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig("plots/visualization_c_profit_vs_sales.png")
plt.show()
