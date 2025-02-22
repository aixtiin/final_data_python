import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from ucimlrepo import fetch_ucirepo

heart_disease = fetch_ucirepo(id=45)
data = pd.DataFrame(heart_disease.data.features)
data.columns = ['age', 'sex'    , 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
print(data['cp'].value_counts())

data['sex'] = data['sex'].map({0: 'Female', 1: 'Male'})
data['cp'] = data['cp'].map({
    4: 'Typical Angina',  # Add this line
    1: 'Atypical Angina',
    2: 'Non-Anginal Pain',
    3: 'Asymptomatic'
})

sns.swarmplot(x='sex', y='age', data=data, hue='cp', palette='rocket', dodge=True) 
plt.xlabel('Gender')      
plt.ylabel('Age')
plt.title('age+gender+chest_pain')

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Chest Pain Type', loc='upper left')
plt.show()