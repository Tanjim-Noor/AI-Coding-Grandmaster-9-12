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

# Countplot for gender survival
g = sns.countplot(x='Gender', hue='Survived', data=data)
plt.title('Survival by Gender')
plt.show()

# Countplot for passenger class survival
plt.figure(figsize=(8, 5))
sns.countplot(x='Pclass', hue='Survived', data=data)
plt.title('Survival by Passenger Class')
plt.show()

# Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['Age'].dropna(), kde=False, bins=40)
plt.title('Age Distribution of Passengers')
plt.show()

# Gender countplot
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.show()

# SibSp with survival
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', hue='SibSp', data=data, palette='mako')
plt.title('Survival by SibSp')
plt.show()

# Parch with survival
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', hue='Parch', data=data, palette='mako')
plt.title('Survival by Parch')
plt.show()

# Fare distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['Fare'].dropna(), kde=True)
plt.title('Fare Distribution')
plt.show()

# Age group by PClass
plt.figure(figsize=(8, 5))
sns.boxplot(x='Pclass', y='Age', data=data, palette='winter')
plt.title('Age by Pclass')
plt.show()

# Correlation heatmap
data_corr = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(data_corr, annot=True, cmap='viridis')
plt.title('Feature Correlation Heatmap')
plt.show()
