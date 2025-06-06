import matplotlib.pyplot as plt
import pandas as pd
import os

# Read CSV for health facilities per region
os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv('../Datasets/Stat_HFProvincial.csv')

# Group by region name and sum the total for each region
region_totals = df.groupby('Region Name')['TOTAL'].sum().reset_index()

# Plot data
plt.figure(figsize=(12, 6))
bars = plt.bar(region_totals['Region Name'], region_totals['TOTAL'], color='red')

# Add labels and title
plt.xlabel('Region')
plt.ylabel('Total Health Facilities')
plt.title('Total Health Facilities per Region')
plt.xticks(rotation=45, ha='right')

# Add value on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1,
             str(height), ha='center', va='bottom', fontsize=8)

# Display plot
plt.tight_layout()
plt.show()
