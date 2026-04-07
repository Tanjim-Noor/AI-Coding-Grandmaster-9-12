# Import Libraries
import pandas as pd
import numpy as np

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))
print(data.dtypes)

# Nominal and ordinal categorical features
nominal_cat = ['Name', 'Ticket', 'Cabin']
ordinal_cat = ['Embarked', 'Gender']

print('Nominal categorical columns:', nominal_cat)
print('Ordinal categorical columns:', ordinal_cat)

# Median value of Gender and Embarked using ordinal encoding
print('Gender value counts:')
print(data['Gender'].value_counts())

gender_categories = ['Female', 'Male']
data['Gender'] = pd.Categorical(data['Gender'], categories=gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes.dropna())
median_gender = gender_categories[int(median_index)]
print('Median Gender:', median_gender)

print('Embarked value counts:')
print(data['Embarked'].value_counts())

embarked_categories = ['S', 'C', 'Q']
data['Embarked'] = pd.Categorical(data['Embarked'], categories=embarked_categories, ordered=True)

median_index = np.median(data['Embarked'].cat.codes.dropna())
median_embarked = embarked_categories[int(median_index)]
print('Median Embarked:', median_embarked)
