import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import os
import numpy as np

# Load your CSV file (raw string to avoid issues with backslashes)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv('C:\\Users\\Sean\\Desktop\\Healthy-Boys\\healthy-boys\\Datasets\\region_health_stats.csv')

# Extract the two variables
x = df['Health Facility Density']
y = df['Mortality Rate']

# Perform Pearson correlation
r, p_value = pearsonr(x, y)

# Print results
print(f"Pearson's r: {r:.3f}")
print(f"P-value: {p_value:.3g}")

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')

# Line of best fit (regression line)
slope, intercept = np.polyfit(x, y, 1)
plt.plot(x, slope * x + intercept, color='red', label=f'Best Fit Line (r = {r:.3f})')

# Add titles and labels
plt.title('Health Facility Density vs Mortality Rate', fontsize=16)
plt.xlabel('Health Facility Density', fontsize=14)
plt.ylabel('Mortality Rate', fontsize=14)
plt.text(0.05, 0.95, f"Pearson's r = {r:.3f}", transform=plt.gca().transAxes, fontsize=12, color='black')

plt.legend()
plt.show()