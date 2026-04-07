# Import Pandas and Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Upload File and Make a Copy of the File
countries_df = pd.read_csv('countries.csv')
countries = countries_df
print(countries.head(3))

# Extract the rows where the year is 1952
c_52 = countries.loc[countries['year'] == 1952]
print(c_52.head())

# Extract the rows where the year is 2007
c_07 = countries.loc[countries['year'] == 2007]
print(c_07.head())

# Merge the '52 and the '07 dataframes together
c_merge = c_52.merge(c_07, left_on='country', right_on='country')
print(c_merge.head())

# Drop both the year columns
c_merge = c_merge.drop(['year_x', 'year_y'], axis=1)
print(c_merge.head())

# Create a new column that takes the difference between the population_y and the population_x column
c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']
print(c_merge.head())

# Test the math
print(31889923 - 8425333)
print(c_merge.shape, type(c_merge))

# Sort the values so you get back the 10 countries with the biggest population growth
c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)
print(c_merge.head(10))

# Now let's plot our data!
names = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Philippines']
pop_grow = (c_merge['population_growth'] / 10**6)

plt.figure(figsize=(15, 9))
plt.bar(names, pop_grow, width=0.6)
plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title('Top 10 Countries w/the Biggest Population Growth from 1952 to 2007')
plt.xticks(rotation=45)

for x, y in zip(names, pop_grow):
    label = "({:.2f}".format(y)
    plt.annotate(label,
                 (x, y),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

plt.show()
