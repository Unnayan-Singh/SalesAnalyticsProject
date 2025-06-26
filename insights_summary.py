import pandas as pd

df = pd.read_csv("cleaned_superstore_data.csv")

# Top 5 profitable states
top_states = df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(5)

# Most profitable segment
top_segment = df.groupby("Segment")["Profit"].sum().sort_values(ascending=False).idxmax()

# Most profitable category
top_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False).idxmax()

# Region with lowest sales
low_region = df.groupby("Region")["Sales"].sum().sort_values().idxmin()

# Sub-category with high sales but low profit
subcat_data = df.groupby("Sub-Category")[["Sales", "Profit"]].sum()
subcat_data["Profit_Margin"] = subcat_data["Profit"] / subcat_data["Sales"]
low_margin = subcat_data.sort_values(by=["Sales"], ascending=False).head(10).sort_values("Profit_Margin").head(1)

print("\n📌 BUSINESS INSIGHTS & RECOMMENDATIONS:\n")

print(f"✅ Top 5 most profitable states:\n{top_states.to_string()}\n")
print(f"✅ Most profitable customer segment: {top_segment}")
print(f"✅ Most profitable product category: {top_category}")
print(f"⚠️ Region with the lowest sales: {low_region}")
print(f"📉 Sub-category with high sales but low profit margin:\n{low_margin.to_string()}")
