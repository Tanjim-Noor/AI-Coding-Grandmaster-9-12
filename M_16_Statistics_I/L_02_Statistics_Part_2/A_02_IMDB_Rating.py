# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Upload dataset using Google Colab file loader
from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('IMDB Dataset.csv')
print(data.head(5))
print(data.info())
print(data.isnull().sum())

# Plot histogram for Runtime
plt.hist(data['Runtime'], bins=20, edgecolor='black')
plt.ylabel('Count of movies')
plt.xlabel('Runtime')
plt.title('Runtime Distribution')
plt.show()

# Plot histogram for IMDB Rating
plt.hist(data['IMDB_Rating'], bins=20, edgecolor='black')
plt.ylabel('Count of movies')
plt.xlabel('IMDB Rating')
plt.title('IMDB Rating Distribution')
plt.show()

# Define parameter bins_runtime and bins_rating
bins_time = np.arange(80, 230, 10)
plt.hist(data['Runtime'], edgecolor='black', bins=bins_time, color='g')
plt.ylabel('Count of movies')
plt.xlabel('Runtime')
plt.title('Binned Runtime Distribution')
plt.show()

bins_rating = np.arange(8, 10, 0.20)
plt.hist(data['IMDB_Rating'], edgecolor='black', bins=bins_rating, color='g')
plt.ylabel('Count of movies')
plt.xlabel('IMDB Rating')
plt.title('Binned IMDB Rating Distribution')
plt.xticks(bins_rating)
plt.show()