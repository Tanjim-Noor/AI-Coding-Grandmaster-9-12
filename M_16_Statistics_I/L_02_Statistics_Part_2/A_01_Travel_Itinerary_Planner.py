# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Upload dataset using Google Colab file loader
from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Weather Dataset.csv')
print(data.head(5))
print(data.info())

# Check null values
print(data.isnull().sum())

# Mean, variance and standard deviation of temperature
mean_temp = np.mean(data['Temperature (C)'])
var_temp = np.var(data['Temperature (C)'])
std_temp = np.std(data['Temperature (C)'])
print('Mean Temperature is :', mean_temp)
print('Variation of Temperature is :', var_temp)
print('Standard Deviation of Temperature is :', std_temp)

# Mean and standard deviation for each month
for i in range(1, 13):
    month = data.loc[data['month'] == i]['Temperature (C)']
    print('For month', i)
    print('Mean Temperature is', np.mean(month))
    print('Standard deviation is', np.std(month), "\n")

# Plot temperature histogram
plt.hist(data['Temperature (C)'], bins=20, edgecolor='black', color='g')
plt.xlabel('Temperature (C)')
.ylabel('Count of days')
plt.title('Temperature Distribution')
plt.show()