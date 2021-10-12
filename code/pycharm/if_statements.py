# if statements allow us to create programs that can make decisions based on some condition.

is_raining = True # condition one
is_sunning = False # condition two

if is_raining: # if condition one is true print the below string
    print("It is raining!")
    print("Don't forget your umbrella")
elif is_sunning: # if condition two is true print the below string
    print("It is a sunny day")
    print("Remember your sunglasses")
else: # if neither condition is true print the below string
    print("Enjoy your day")

print("Talk to you later!")

loyal_customer = False
price_sausage = 5

if loyal_customer:
    print(f"Sausage Price: £{price_sausage*0.90}")
else:
    print(f"Sausage Price: £{price_sausage*1.10}")

# --- Logical operators (i.e., and, or and not)
hard_working = True
bad_grades = False

if hard_working and not bad_grades:
    print("Successful applicant")

# --- Comparison operators (>, >=, <, <=, == and !=)

age = 6
if age >= 18: # Boolean expression
    print("You are allowed to buy alcohol in the UK")
else:
    print("You are not allowed to buy alcohol in the UK")

# Exercise
password = input("New password: ")

if len(password) < 5:
    print("Password must be at least five characters.")
elif len(password) > 10:
    print("Password can be a maximum of 10 characters.")
else:
    print("New password accepted")

# Advanced exercise
bank_statement = input("How much money is in your bank account? ")
euro_pound = input("Is your bank statement in euros or pounds? ")

if euro_pound.lower() == "euros":
    print(f"You have {int(bank_statement) * 0.85} pounds.")
else:
    print(f"You have {int(bank_statement) * 1.18} euros.")



