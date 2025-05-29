import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('region_health_stats.csv')
x = df['Health Facility Density']
y = df['Mortality Rate']

r, p_value = pearsonr(x, y)
print(f"Pearson's r: {r:.3f}")

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
slope, intercept = np.polyfit(x, y, 1)
plt.plot(x, slope * x + intercept, color='red', label=f'Best Fit Line (r = {r:.3f})')
plt.title('Correlation between Health Facility Density and Mortality Rate', fontsize=16)
plt.xlabel('Health Facility Density', fontsize=14)
plt.ylabel('Mortality Rate', fontsize=14)
plt.text(0.05, 0.95, f"Pearson's r = {r:.3f}", transform=plt.gca().transAxes, fontsize=12, color='black')
plt.legend()
plt.show()
