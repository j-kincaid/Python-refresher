# score = 0
# height = 1.8
# isWinning = True
# # # f-String
# print(f"Your score is {score}, your height is {height}m, and you are winning is {isWinning}.")

age = input("What is your current age?")

# years = 90 - int(age)
# m = round(years/12, 2)
# age = int(age)

age_as_int = int(age)

a = 90 - age_as_int

days = round((a * 365), 5)

weeks = round((a * 52), 4)

months = round((a * 12), 3)
print(age)
message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)