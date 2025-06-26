# regional_sales.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_superstore_data.csv")

# Set plot style
sns.set(style="whitegrid")

# Group sales by Region
region_sales = df.groupby("Region")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False)

# Create bar plot
plt.figure(figsize=(8, 6))
sns.barplot(data=region_sales, x="Region", y="Sales", hue="Region", palette="Set2", legend=False)
plt.title("Total Sales by Region 🗺️")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.tight_layout()

# Save and show plot
plt.savefig("plots/regional_sales.png")
plt.show()
