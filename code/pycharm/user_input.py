# To get input from a user we need the function input().

age = input("What is your age? ")

# How would you feed the input back to your user?

print("Your are " + age + " years old.")

# Note: remember to utilize spaces to separate strings from variables.

# Exercise:
# Ask two questions: what is your name?; what is your favourite animal?.
# Then print a message like "Roos's favourite animal is a chicken.".

name = input("What is your name? ")

animal = input("Hello " + name + ", what is your favourite animal? ")
print(name + "'s favourite animal is a " + animal + ".")

# ---

# Exercise:
# Ask the user to confirm their weight (in kilograms) and then convert it into pounds.

weight = input("What is your weight in kilograms? ")
convert = (int(weight) * 2.20)
print(convert)

print("You are " + str(convert) + " pounds.")