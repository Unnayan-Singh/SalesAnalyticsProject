# sales_vs_quantity.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_superstore_data.csv")

# Plot settings
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Scatter plot of Sales vs Quantity
sns.scatterplot(data=df, x="Quantity", y="Sales", hue="Category", palette="Set2")

plt.title("📊 Sales vs Quantity Sold")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.legend(title="Category")
plt.tight_layout()

# Save plot
plt.savefig("plots/sales_vs_quantity.png")
plt.show()
