import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("D:\python_database_projects_2\python_database_projects\PD_final\monthly_IBM.csv", parse_dates=['timestamp'])
data = data.reset_index()

sns.regplot(x=data.index, y='close', data=data,color='red')
plt.xlabel('time')
plt.ylabel('final price')
plt.title('regression plot monthly')
plt.show()