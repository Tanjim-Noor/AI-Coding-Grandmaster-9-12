# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Iris.csv')
print(data.head(5))

# Check null values
print(data.isnull().sum())

# Statistical information of features
print(data.describe())

# Boxplot of all features
labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print('Distribution of', label)
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=data[label])
    plt.title(f'Boxplot of {label}')
    plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Iris Features')
plt.show()

# Check skewness
for label in labels:
    print('Distribution of', label)
    plt.figure(figsize=(8, 4))
    sns.histplot(data[label].dropna(), kde=True)
    plt.title(f'Distribution of {label}')
    plt.show()
    print('Skewness of', label, data[label].skew())
