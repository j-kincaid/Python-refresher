# BMI = weight / height ** 2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


h = float(height)
w = float(weight)
bmi = str(int(w / (h * h)))

print(bmi)