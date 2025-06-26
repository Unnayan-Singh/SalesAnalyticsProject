# monthly_sales_trend.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Extract month-year and group sales
df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month-Year')["Sales"].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month-Year', y='Sales', marker='o', sort=False)
plt.xticks(rotation=45)
plt.title("📅 Monthly Sales Trend")
plt.xlabel("Month-Year")
plt.ylabel("Sales")
plt.tight_layout()

# Save the plot
plt.savefig("plots/monthly_sales_trend.png")
plt.show()
