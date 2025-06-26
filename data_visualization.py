import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv", parse_dates=['Order Date'])

# Set style
sns.set(style="whitegrid")

# 1. Sales Trend Over Time
plt.figure(figsize=(12, 6))
sales_trend = df.groupby("Order Date")["Sales"].sum()
sales_trend.plot()
plt.title("📈 Sales Trend Over Time")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("plots/sales_trend.png")
plt.show()

# 2. Total Sales by Category
plt.figure(figsize=(8, 6))
category_sales = df.groupby("Category")["Sales"].sum().sort_values()
category_sales.plot(kind='barh', color='skyblue')
plt.title("📊 Total Sales by Category")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig("plots/sales_by_category.png")
plt.show()

# 3. Pie Chart: Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(6, 6))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("🌍 Sales Distribution by Region")
plt.tight_layout()
plt.savefig("plots/sales_by_region.png")
plt.show()

# 4. Heatmap: Correlation
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Sales', 'Quantity', 'Discount', 'Profit']].corr(), annot=True, cmap='coolwarm')
plt.title("🧠 Correlation Matrix")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.show()

# 5. Top 10 Customers by Sales
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_customers.plot(kind='bar', color='orange')
plt.title("💼 Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("plots/top_customers_sales.png")
plt.show()
