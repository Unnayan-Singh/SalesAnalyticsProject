# visualization_f_top_customers.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Calculate total sales by customer
top_customers = df.groupby("Customer Name")["Sales"].sum().reset_index()
top_customers = top_customers.sort_values(by="Sales", ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_customers, x="Sales", y="Customer Name", palette="cubehelix")

plt.title("🧑‍💼 Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")
plt.tight_layout()

# Save the plot
plt.savefig("plots/visualization_f_top_customers.png")
plt.show()
