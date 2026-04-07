# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Upload dataset using Google Colab file loader
from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))
print(data.dtypes)

# Check null values
print(data.isnull().sum())

# Mean value of age
mean_age = np.mean(data['Age'])
print('Mean Age of Passengers is -', mean_age)

# Mean value of fare
mean_fare = np.mean(data['Fare'])
print('Mean Fare is -', mean_fare)

# Plot survival counts by passenger class
sns.countplot(x='Pclass', hue='Survived', data=data)
plt.title('Survival by Passenger Class')
plt.show()

# Plot age distribution
plt.figure(figsize=(10, 5))
sns.histplot(data['Age'].dropna(), bins=20, kde=True)
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.show()