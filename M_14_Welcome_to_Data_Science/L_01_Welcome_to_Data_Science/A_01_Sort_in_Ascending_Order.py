# Activity 1: Sort in Ascending Order

# In this question, you have to sort people in the ascending order of their height using NumPy arrays.

import numpy as np

# Define structured data for students
data_type = [('name', 'U15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

students = np.array(students_details, dtype=data_type)

print('Original array:')
print(students)

print('Sort by height:')
print(np.sort(students, order='height'))
