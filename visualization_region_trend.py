# visualization_region_trend.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cleaned_superstore_data.csv")

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Add month-year column
df['Month'] = df['Order Date'].dt.to_period('M')

# Group by Region and Month
region_trend = df.groupby(['Month', 'Region'])['Profit'].sum().reset_index()
region_trend['Month'] = region_trend['Month'].astype(str)

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=region_trend, x='Month', y='Profit', hue='Region', marker='o')
plt.title("📈 Monthly Profit Trend by Region")
plt.xticks(rotation=45)
plt.tight_layout()

# Save figure
plt.savefig("plots/visualization_region_trend.png")
plt.show()
