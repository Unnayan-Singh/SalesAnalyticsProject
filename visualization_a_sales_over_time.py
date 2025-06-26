import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Convert 'Order Date' to datetime (just in case)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Group data by Month-Year
df['Month-Year'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month-Year')['Sales'].sum().reset_index()
monthly_sales['Month-Year'] = monthly_sales['Month-Year'].astype(str)

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month-Year', y='Sales', marker='o')
plt.xticks(rotation=45)
plt.title('Sales Over Time')
plt.xlabel('Month-Year')
plt.ylabel('Sales')
plt.tight_layout()
plt.grid(True)
plt.savefig("plots/visualization_a_sales_over_time.png")
plt.show()
