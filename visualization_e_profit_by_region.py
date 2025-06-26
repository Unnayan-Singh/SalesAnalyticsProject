# visualization_e_profit_by_region.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Group by Region and sum profits
region_profit = df.groupby("Region")["Profit"].sum().reset_index().sort_values("Profit", ascending=False)

# Plot
plt.figure(figsize=(8, 6))
sns.barplot(data=region_profit, x="Profit", y="Region", palette="Set3")

plt.title("🌍 Profit by Region")
plt.xlabel("Total Profit")
plt.ylabel("Region")
plt.tight_layout()

# Save the plot
plt.savefig("plots/visualization_e_profit_by_region.png")
plt.show()
