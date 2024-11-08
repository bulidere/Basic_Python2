 # Calculating and displaying central tendency measures
import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
path=kagglehub.dataset_download("henriqueyamahata/bank-marketing")
data=pd.read_csv(path+"/bank-additional-full.csv",sep=";")
df=pd.DataFrame(data)

 # Visualizing risk assessment with standard deviation
''''
plt.figure(figsize=(10, 5))
sns.histplot(df['duration'], bins=30, kde=True)
plt.axvline(x=df['duration'].mean(), color='red', linestyle='--',
label='Mean Duration')
plt.axvline(x=df['duration'].mean() + df['duration'].std(),

color='green', linestyle='--', label='1 Std Dev')
plt.axvline(x=df['duration'].mean() - df['duration'].std(),
color='green', linestyle='--')

plt.title("Duration Distribution with Mean and Standard Deviation")
plt.xlabel("Duration (seconds)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

 # Histogram for Age
plt.figure(figsize=(10, 5))
sns.histplot(df['age'], bins=30, kde=True)
plt.title("Age Distribution of Bank Clients")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# Box Plot for Call Duration
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['duration'])
plt.title("Distribution of Call Duration")
plt.xlabel("Call Duration (seconds)")
plt.show()

# Calculating correlations
pearson_corr = df[['duration', 'campaign']].corr(method='pearson')
spearman_corr = df[['duration', 'campaign']].corr(method='spearman')
print(f"Pearson Correlation: \n{pearson_corr}, \nSpearman Correlation:\n{spearman_corr}")
'''''

# Scatter plot for account balances vs. transaction frequency
 
plt.figure(figsize=(10, 6))
sns.scatterplot(x='campaign', y='duration', hue='y', data=df,
alpha=0.6)
plt.title("Campaign Contacts vs. Call Duration")
plt.xlabel("Number of Contacts in Campaign")
plt.ylabel("Call Duration (seconds)")
plt.legend(title="Subscription Outcome")
plt.show()

 # Sort by month order for better visual alignment
month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug',
'sep', 'oct', 'nov', 'dec']
df['month']= pd.Categorical(df['month'], categories=month_order, ordered=True)
df_sorted = df.sort_values('month')
# Plotting Ridge Plot
plt.figure(figsize=(10, 8))
for month in month_order:sns.kdeplot(df_sorted[df_sorted['month'] == month]['duration'],
label=month, fill=True, alpha=0.5)
plt.title("Ridge Plot of Call Duration by Month")
plt.xlabel("Call Duration (seconds)")
plt.ylabel("Density")
plt.legend(title='Month')
plt.show()