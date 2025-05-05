import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from adjustText import adjust_text

os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv('../Datasets/FHSIS.csv', thousands=',')
df['Population'] = df['Population'].astype(int)

region_population = df.groupby('Region Name')['Population'].sum()
region_population_dict = region_population.to_dict()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv('../Datasets/Stat_HFProvincial.csv')

region_hf = df.groupby('Region Name')['TOTAL'].sum()
region_hf_dict = region_hf.to_dict()

region_hf_density = {}
for region in region_population_dict:
    population = region_population_dict.get(region)
    hf = region_hf_dict.get(region)
    if population and hf:
        region_hf_density[region] = (hf / population) * 10000
    else:
        region_hf_density[region] = None


os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv('../Datasets\VSR PUF 2023 Death.csv')

region_death = df['place_of_death_region_new'].value_counts()

region_id_to_name_map = {
    1: 'REGION I',
    2: 'REGION II',
    3: 'REGION III',
    4: 'REGION IV-A',
    5: 'REGION V',
    6: 'REGION VI',
    7: 'REGION VII',
    8: 'REGION VIII',
    9: 'REGION IX',
    10: 'REGION X',
    11: 'REGION XI',
    12: 'REGION XII',
    13: 'NCR',
    14: 'CAR',
    16: 'REGION XIII',
    17: 'MIMAROPA',
    18: 'NIR',
    19: 'BARMM'
}

region_death.index = region_death.index.map(region_id_to_name_map)
region_death_dict = region_death.to_dict()

death_counts_df = pd.DataFrame(list(region_death_dict.items()), columns=['Region Name', 'Deaths'])
population_df = pd.DataFrame(list(region_population_dict.items()), columns=['Region Name', 'Population'])

merged_df = pd.merge(death_counts_df, population_df, on='Region Name', how='left')

merged_df['Mortality Rate'] = (merged_df['Deaths'] / merged_df['Population']) * 10000


merged_df['Health Facility Density'] = merged_df['Region Name'].map(region_hf_density)

plt.figure(figsize=(12, 6))
regions = merged_df['Region Name'].unique()
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(regions)))
texts = []

for i, region in enumerate(regions):
    region_data = merged_df[merged_df['Region Name'] == region]
    x = region_data['Health Facility Density'].values[0]
    y = region_data['Mortality Rate'].values[0]

    plt.scatter(x, y, label=region, color=colors[i], s=100, alpha=0.7)

    texts.append(plt.text(x, y, region, fontsize=8))

adjust_text(texts, arrowprops=dict(arrowstyle='-', color='gray', lw=0.5))

slope, intercept = np.polyfit(merged_df['Health Facility Density'], merged_df['Mortality Rate'], 1)
best_fit_line = slope * merged_df['Health Facility Density'] + intercept
plt.plot(merged_df['Health Facility Density'], best_fit_line, color='red', linewidth=2, label='Best Fit Line')

plt.xlabel('Health Facility Density (per 10,000 people)')
plt.ylabel('Mortality Rate (per 10,000 people)')
plt.title('Mortality Rate vs Health Facility Density by Region')

plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()