# visualization_sales_by_state.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_superstore_data.csv")

# Group sales by state
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=True)

# Plot
plt.figure(figsize=(12, 10))
sns.barplot(x=state_sales.values, y=state_sales.index, palette='coolwarm')
plt.title("🗺️ Total Sales by State")
plt.xlabel("Sales")
plt.ylabel("State")
plt.tight_layout()

# Save figure
plt.savefig("plots/visualization_sales_by_state.png")
plt.show()
