# visualization_sales_trend.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Group by month and sum sales
monthly_sales = df.resample('MS', on='Order Date')['Sales'].sum()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='royalblue')
plt.title("📆 Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig("plots/visualization_sales_trend.png")
plt.show()
