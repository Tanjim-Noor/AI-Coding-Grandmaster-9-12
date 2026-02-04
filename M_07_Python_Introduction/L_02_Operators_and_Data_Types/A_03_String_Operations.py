"""
Activity 3
Title: String Operations
Short description:
Store the values of your first name and last name in respective variables. Now add these two strings and store them in the variable full_name. Create another variable with the first name multiplied by any number of your choice as its value. Print all the four variables. Now add another variable to your program with any string of your choice. Find its length, print its first and last character, and print a sub-string of this original string as well.
"""

first_name = "Codingal"
last_name = "Educations"
full_name = first_name + last_name
example = "Haa" * 5

print("First Name :", first_name)
print("Last Name :", last_name)
print("Full Name :", full_name)
print("String Multiplied 5 times gives this result :", example)

word = 'Coding'
print("Length of String :", len(word))
print("First letter of String :", word[0])
print("Last Letter of String :", word[5])
print("String Sliced :", word[0:3])
