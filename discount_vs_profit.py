# discount_vs_profit.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Plot: Discount vs Profit Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category", alpha=0.7)
plt.title("💸 Discount vs Profit by Category")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
plt.savefig("plots/discount_vs_profit.png")
plt.show()
