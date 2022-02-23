# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

your_names = name1 + name2
your_names_lower = your_names.lower()

t = your_names_lower.count("t")
r = your_names_lower.count("r")
u = your_names_lower.count("u")
e = your_names_lower.count("e")

true = t + r + u + e 

l = your_names_lower.count("l")
o = your_names_lower.count("o")
v = your_names_lower.count("v")
e = your_names_lower.count("e")

love  = l + o + v + e

str_love_score = str(true) + str(love)
love_score = int(str_love_score)
print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif (love_score >= 40 )and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else: 
    print(f"Your score is {love_score}.")


