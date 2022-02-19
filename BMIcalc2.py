# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# h = round(height, 2)
# w = round(weight, 2)
bmi = round(weight / (height * height))


# Example input

# height = 1.75
# weight = 85
# Example output 
# Your BMI is 28, you are slightly overweight.

# height = 1.8
# weight = 89
# Example output 
# Your BMI is 27, you are slightly overweight.



if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
