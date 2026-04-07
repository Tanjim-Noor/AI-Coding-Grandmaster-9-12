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

# Check null values
print(data.isnull().sum())

# Boxplot of feature Age
plt.figure(figsize=(8, 5))
plt.boxplot(data['Age'].dropna())
plt.title('Age distribution')
plt.ylabel('Age')
plt.show()

# Boxplot of feature Pclass
plt.figure(figsize=(8, 5))
plt.boxplot(data['Pclass'].dropna())
plt.title('Passenger Class distribution')
plt.ylabel('Passenger Class')
plt.show()
