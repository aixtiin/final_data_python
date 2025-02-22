import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('D:\python_database_projects_2\python_database_projects\PD_final\monthly_IBM.csv')

sns.lineplot(x='timestamp', y='close', data=data, color='blue')
sns.kdeplot(data['close'], color='red', linestyle='-') 
plt.xlabel('date')
plt.ylabel('close')
plt.title('IBM monthly')

mean_close = data['close'].mean()
median_close = data['close'].median()
mode_close = data['close'].mode()

plt.axvline(median_close, color='orange', linestyle='dashed')
plt.axhline(mean_close, color='red', linestyle='dashed')

print(f'mean: {mean_close}')
print(f'meadian_close: {median_close}')
print(f'mode: {mode_close}')
plt.show()