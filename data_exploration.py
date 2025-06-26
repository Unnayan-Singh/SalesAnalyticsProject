import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
try:
    df = pd.read_csv("cleaned_superstore_data.csv")
    print("✅ Data loaded successfully!")
except Exception as e:
    print("❌ Error loading CSV file:", e)
    exit()

# Dataset Overview
print("\n📊 Dataset Overview:")
print(df.info())

# Null Values
print("\n🧹 Null values in each column:")
print(df.isnull().sum())

# Sales Summary
if 'Sales' in df.columns:
    print("\n💰 Total Sales: ₹", round(df['Sales'].sum(), 2))
    print("📈 Average Sales: ₹", round(df['Sales'].mean(), 2))
    print("💹 Maximum Sale: ₹", df['Sales'].max())
    print("🔻 Minimum Sale: ₹", df['Sales'].min())

# Top 10 Products by Sales
if 'Product Name' in df.columns and 'Sales' in df.columns:
    top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
    print("\n🏆 Top 10 Products by Sales:\n", top_products)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
    plt.title('Top 10 Products by Sales')
    plt.xlabel('Total Sales')
    plt.ylabel('Product Name')
    plt.tight_layout()
    plt.show()

# Sales by Region
if 'Region' in df.columns and 'Sales' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Region', y='Sales', estimator=sum, ci=None, palette='Set2')
    plt.title('Sales by Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Monthly Sales Trend
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    monthly_sales = df.resample('M', on='Order Date')['Sales'].sum()

    plt.figure(figsize=(12, 5))
    monthly_sales.plot(marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
