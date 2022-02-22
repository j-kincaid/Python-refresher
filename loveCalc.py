# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

your_name = "name1".lower()
their_name = "name2".lower()

true_count = 0
love_count = 0
if your_name.count("t"):
    true_count += 1
if their_name.count("t"):
    true_count += 1
if your_name.count("r"):
    true_count += 1
if their_name.count("r"):
    true_count += 1
if your_name.count("u"):
    true_count += 1
if their_name.count("u"):
    true_count += 1
if your_name.count("e"):
    true_count += 1
if their_name.count("e"):
    true_count += 1

print(true_count)

if your_name.count("l"):
    love_count += 1
if their_name.count("l"):
    love_count += 1
if your_name.count("o"):
    love_count += 1
if their_name.count("o"):
    love_count += 1
if your_name.count("v"):
    love_count += 1
if their_name.count("v"):
    love_count += 1
if your_name.count("e"):
    love_count += 1
if their_name.count("e"):
    love_count += 1

print(love_count)

love_score_concat = str(true_count) + str(love_count)
love_score = int(love_score_concat)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else: 
    print(f"Your score is {love_score}.")


