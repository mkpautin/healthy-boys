import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import os

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