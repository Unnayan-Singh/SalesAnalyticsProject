# visualization_discount_profit.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_superstore_data.csv")

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category", palette="coolwarm", alpha=0.7)

plt.title("💸 Discount vs Profit by Category")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(True)
plt.legend(title="Category")
plt.tight_layout()

# Save the plot
plt.savefig("plots/visualization_discount_profit.png")
plt.show()
