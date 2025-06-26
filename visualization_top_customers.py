# visualization_top_customers.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Top 10 customers by sales
top_customers = df.groupby("Customer Name")["Sales"].sum().nlargest(10).sort_values()

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_customers.values, y=top_customers.index, palette='crest')
plt.title("👤 Top 10 Customers by Sales")
plt.xlabel("Sales")
plt.ylabel("Customer Name")
plt.tight_layout()

# Save the figure
plt.savefig("plots/visualization_top_customers.png")
plt.show()
