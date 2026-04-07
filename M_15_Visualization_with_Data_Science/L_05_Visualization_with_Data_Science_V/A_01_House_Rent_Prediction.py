# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
HouseDF = pd.read_csv('USA_Housing.csv')

# Display first few rows
print(HouseDF.head())

# Display dataset information
print(HouseDF.info())

# Display column names
print(HouseDF.columns)

# Create pairplot
sns.pairplot(HouseDF)

# Create heatmap of correlations
plt.figure(figsize=(12, 10))
sns.heatmap(HouseDF.corr(), annot=True)
plt.title('USA Housing Dataset Correlation Heatmap')
plt.show()
