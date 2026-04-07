# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))

# Check null values
print(data.isnull().sum())

# Quartiles of feature Age
age_q1 = np.quantile(data['Age'].dropna(), 0.25)
age_q2 = np.quantile(data['Age'].dropna(), 0.50)
age_q3 = np.quantile(data['Age'].dropna(), 0.75)

print('Age Quartiles -')
print('Q1 -', age_q1)
print('Q2 -', age_q2)
print('Q3 -', age_q3)

# Interquartile range of feature Age
IQR_age = age_q3 - age_q1
print('Interquartile Range :', IQR_age)

# Plot histogram for feature Age
plt.hist(data['Age'].dropna())
plt.ylabel('Count of Passengers')
plt.xlabel('Age')
plt.title('Age Histogram')
plt.show()

# Quartiles for feature Fare
fare_q1 = np.quantile(data['Fare'].dropna(), 0.25)
fare_q2 = np.quantile(data['Fare'].dropna(), 0.50)
fare_q3 = np.quantile(data['Fare'].dropna(), 0.75)

print('Fare Quartiles -')
print('Q1 -', fare_q1)
print('Q2 -', fare_q2)
print('Q3 -', fare_q3)

# Interquartile range of feature Fare
IQR_fare = fare_q3 - fare_q1
print('Interquartile Range :', IQR_fare)

# Plot histogram for feature Fare
bins = np.arange(0, 250, 20)
plt.hist(data['Fare'].dropna(), bins=bins)
plt.ylabel('Count of Passengers')
plt.xlabel('Fare')
plt.xticks(bins)
plt.title('Fare Histogram')
plt.show()
