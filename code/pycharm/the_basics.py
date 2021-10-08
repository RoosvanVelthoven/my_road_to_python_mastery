# To run code use the short cut shift F10 (on Windows)
print("I am Roos van Velthoven")

# Note: we can use single quotes ' ' or double quotes " ".

# We have different types of code in Python.

# Expressions: expressions are code that produces a value.
# Variables: variables store data (temporarily) in a computers memory.

# String: a sting is code between quotations (a string is a series of characters).
# Integer: a integer is a number without a decimal point.
# Float (floating point number): a float is a number with a decimal point.
# Boolean: a boolean is a true of false statement.

# What happens if we run the below expression?
print("!" * 5)

# ! gets multiplied five times.

# What happens if we run the below variable?
age = 24

print(age)

# print(age) gives us the value 24 which we had coded in our memory.

# What happens if we run print("age")?

print("age")

# The terminal prints the string age.

# Exercise:
# We have a new student named Roos van Velthoven.
# She is 24 years old.
# Create three variables using the above information.

new_student = True
name = "Roos van Velthoven"
age = 24

# --- What does the function type() do?

# The function type() allows us to determine the class of a variable.

# For example:
print(type(age))

# You can change the type of your variable by adding int(), float(), bool() or str() at the beginning.

# For example:
age = str(age)

print(type(age))

# --- arithmetic operators

# + addition operator
# - subtraction operator
# * multiplication operator
# / division operator (float)
print(7 / 3 )
# 2.3333333333333335
# // division operator (integer)
print(7 // 3 )
# 2
# % modulis operator (returns the remainder of the division)
print(7 % 3 )
# 1
# ** exponent (to the power) operator
print(7 ** 2 )
# 49

# Augmented operators (e.g., += and -=)
x = 5
x = x + 3
print(x)
# 8

y = 5
y += 3
print(y)
# 8

# Order of operations (operator precedence).

# Parenthesis ()
# Exponentiation
# Multiplications or divisions
# Addition or subtraction

# --- Math functions
x = 15.5
print(round(x))
# 16

y = -22.3
print(abs(y)) # abs returns an absolute number (a positive number)
# 22.3

# To import the math model type import math:
import math

print(math.ceil(2.9))
# 3

print(math.floor(2.9))
# 2

# See the webpage https://docs.python.org/3/library/math.html for further information on the available functions.