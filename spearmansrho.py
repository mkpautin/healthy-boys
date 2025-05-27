import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

file_path = 'region_health_stats.csv'
df = pd.read_csv(file_path)
df_clean = df.dropna()

x_col = 'Health Facility Density'  
y_col = 'Mortality Rate'  
label_col = 'Region Name'

corr, p_values = spearmanr(df_clean)
corr_df = pd.DataFrame(corr, index=df_clean.columns, columns=df_clean.columns)
pval_df = pd.DataFrame(p_values, index=df_clean.columns, columns=df_clean.columns)

print("Spearman Correlation Matrix:")
print(corr_df)
print(pval_df)

plt.figure(figsize=(10, 8))
sns.regplot(data=df_clean, x=x_col, y=y_col, scatter=True, ci=None)
plt.title(f'Correlation between {x_col} and {y_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
texts = []
for i, row in df_clean.iterrows():
    texts.append(plt.text(row[x_col], row[y_col], str(row[label_col]), fontsize=9))
adjust_text(texts, arrowprops=dict(arrowstyle='-', color='gray', lw=0.5))
plt.grid(True)
plt.tight_layout()
plt.show()
