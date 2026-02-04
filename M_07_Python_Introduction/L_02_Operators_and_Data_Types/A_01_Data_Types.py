"""
Activity 1
Title: Data Types
Short description:
Store your Name, Age, Weight, Whether you are a student or not (True for yes, False for no) in respective variables. What do you think is the data type of each variable? Print the data type of every variable. Change the datatype of Age to string and Weight to an integer.
"""

name = "Penguin"
age = 15
is_student = True
weight = 38.5

print("Name :", name)
print("Data Type of Name is", type(name))
print("Age :", age)
print("Data Type of Age is", type(age))
print("is_student :", is_student)
print("Data Type of is_student is", type(is_student))
print("Weight :", weight)
print("Data Type of weight is", type(weight))

print("\n After Type Casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))
