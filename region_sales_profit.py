# region_sales_profit.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Group by region
region_summary = df.groupby("Region")[["Sales", "Profit"]].sum().reset_index()

# Set seaborn style
sns.set(style="whitegrid")

# Plot
plt.figure(figsize=(10, 6))
bar_width = 0.4
x = range(len(region_summary))

plt.bar(x, region_summary["Sales"], width=bar_width, label="Sales", color="skyblue")
plt.bar([i + bar_width for i in x], region_summary["Profit"], width=bar_width, label="Profit", color="lightgreen")

plt.xticks([i + bar_width / 2 for i in x], region_summary["Region"])
plt.xlabel("Region")
plt.ylabel("Amount")
plt.title("💼 Total Sales and Profit by Region")
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig("plots/region_sales_profit.png")
plt.show()
