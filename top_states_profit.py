# top_states_profit.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_superstore_data.csv")

# Set plot style
sns.set(style="whitegrid")

# Group and sort by profit
top_states = df.groupby("State")["Profit"].sum().reset_index().sort_values(by="Profit", ascending=False).head(10)

# Create bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_states, x='Profit', y='State', hue='State', palette='viridis', legend=False)
plt.title("Top 10 States by Profit 💸")
plt.xlabel("Total Profit")
plt.ylabel("State")
plt.tight_layout()

# Save and show
plt.savefig("plots/top_states_profit.png")
plt.show()
