# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Example Input 
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"

# Example Output
# Your final bill is: $28.

#Write your code below this line 👇

S = 15
M = 20
L = 25
# add_pepperoni for S = + 2
# add_pepperoni for M or L = + 3
# extra_cheese for any = + 1

bill = 0
if size == S:
    bill = 15
    if add_pepperoni == "Y":
            bill += 2
elif size == M:
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
if 
    bill += 1
print(f"Your final bill is: ${bill}.")

if extra_cheese == "N":
    if size == S:
        bill = 15
        if add_pepperoni == "Y":
            bill += 2
            if size == M:
                bill = 20
            else:
                bill = 25
                if add_pepperoni == "Y":
                    bill += 3
else: 
    bill += 1