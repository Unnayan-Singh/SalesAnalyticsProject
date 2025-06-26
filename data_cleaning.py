import pandas as pd

try:
    # Read .xls file using xlrd engine
    df = pd.read_excel("Sample - Superstore.xls", engine='xlrd')
    print("✅ Excel file loaded successfully!")
except FileNotFoundError:
    print("❌ 'Sample - Superstore.xls' not found. Please place it in your project folder.")
    exit()
except Exception as e:
    print("❌ Error reading Excel file:", e)
    exit()

# Clean column names
df.columns = df.columns.str.strip()

# Drop columns with all NaNs and remove duplicates
df.dropna(axis=1, how='all', inplace=True)
df.drop_duplicates(inplace=True)

# Fill common nulls
df.fillna({
    "Customer Name": "Unknown",
    "Region": "Unknown",
    "Category": "Unknown",
    "Sales": 0,
    "Profit": 0
}, inplace=True)

# Convert date columns
for col in ['Order Date', 'Ship Date']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Save cleaned data
df.to_csv("cleaned_superstore_data.csv", index=False)
print("✅ Cleaned data saved as 'cleaned_superstore_data.csv'")
