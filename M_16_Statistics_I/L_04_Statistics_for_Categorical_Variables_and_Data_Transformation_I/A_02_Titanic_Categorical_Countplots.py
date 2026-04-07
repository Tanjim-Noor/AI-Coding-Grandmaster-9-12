# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))

sns.set_style('whitegrid')

# Countplot for feature Survived
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', data=data)
plt.title('Survived Countplot')
plt.show()

# Barchart for gender survival
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', hue='Survived', data=data)
plt.title('Survival by Gender')
plt.show()

# Customize plots
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', data=data, palette='winter')
plt.title('Survived Countplot - Winter')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')
plt.title('Survival by Gender - Winter')
plt.show()

# Countplot for Embarked
plt.figure(figsize=(8, 5))
sns.countplot(x='Embarked', data=data)
plt.title('Embarked Countplot')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=12)
plt.title('Embarked Countplot with rotated labels')
plt.show()
