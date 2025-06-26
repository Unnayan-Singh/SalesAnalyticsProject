# profit_by_segment.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_superstore_data.csv")

# Set plot style
sns.set(style="whitegrid")

# Plot average profit per segment
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Segment", y="Profit", estimator='mean', errorbar=None, palette="Set3")
plt.title("📊 Average Profit by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Profit")
plt.tight_layout()

# Save the plot
plt.savefig("plots/profit_by_segment.png")
plt.show()
