# You can use both double and single quotations:
project = "My road to Python mastery"
print(project)
project = "Roos's road to Python mastery"
print(project)
project = 'My road to Python "mastery"'
print(project)

# If you want to use a string that is multiple rows use triple quotes:
project = '''
Welcome, 

The current project is my Python progression diary.
If you wish to add to my Python progression journey (or my R progression journey) feel free to contact me.

I am always interested in learning more!

Kind regards,
Roos van Velthoven
'''

print(project)

# We can use square brackets to get a character at a certain index:
project = "My road to Python mastery"
#          012345
print(project[4])
# 0

# Note: The first character is 0, the second character is 1, et cetera.

# We can also use a negative index. For example to get the last character use the below code.
print(project[-1])
# y

# Furthermore, we can extract multiple characters at a time.
print(project[0:4])
# My r

# Note: the fourth character (o) is excluded!

# Please bear in mind that if you use a negative index the last character remains excluded
print(project[0:-1])
# My road to Python master

# --- Formatted strings

# Formatted strings help visualise our output. Formatted strings are prefixed with an f.
# Example:
colour = "colour"
red = "red"
colour_sentence = f"My favourite {colour} is {red}"
print(colour_sentence)

# --- Build in functions
name = "Roos van Velthoven"

# len() can be used to count the number of values/items of a string or list
print(len(name))
# 18

# Note: spaces are also included

# the dot operator (methods specific to strings)
print(name.upper())
# ROOS VAN VELTHOVEN

print(name.lower())
# roos van velthoven

print(name.find("s")) # returns the index of the first s
# 3

# Note the find method is case sensitive. A negative one is returned if the character does not exist.
print(name.find("S"))
# -1

print(name.find("van")) # returns the index of the first letter of the sequence of characters
# 5

print(name.replace("van", "de")) # code to replace characters
# Roos de Velthoven

print("van" in name) # code to check if characters are in a variable (in operator (boolean value))
# True

# Note: the in operator is case sensitive.
