# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))

# Analyze distribution and skewness of selected features
labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for label in labels:
    print('Distribution of', label)
    sns.histplot(data[label].dropna(), kde=True)
    plt.title(f'{label} Distribution')
    plt.show()
    print('Skewness -', data[label].dropna().skew())

# Log transform skewed features
for col in ['SibSp', 'Parch', 'Fare']:
    data[f'log_{col}'] = np.log(data[col].replace(0, np.nan).dropna())
    print(f'Created log_{col}')

print(data[['log_SibSp', 'log_Parch', 'log_Fare']].head())
