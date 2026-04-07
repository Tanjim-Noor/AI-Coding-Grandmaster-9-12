# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))

# Minimum and maximum values of Age
minimum_age = data['Age'].min()
maximum_age = data['Age'].max()
print('Minimum Age :', minimum_age)
print('Maximum Age :', maximum_age)

# Create binned age categories
bins = [0, 15, 30, 45, 60, 75]

age_labels = ['Young', 'Young - Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']
data['binned_age'] = pd.cut(data['Age'], bins, labels=age_labels)

print(data[['binned_age', 'Age']].head())

# Barplot for binned age
data['binned_age'].value_counts().plot(kind='bar')
plt.title('Age Distribution by Bin')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()
