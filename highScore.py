# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
# Example input:
# 78 65 89 86 55 91 64 89
# Example Output:
# The highest score in the class is: 91
#Write your code below this row 👇

# scores_list = []
# for score in student_scores:
#     student_scores += score
#     if student_scores[0] < student_scores[1]:
#         scores_list.pop([0])
#     else:
#         scores_list.append([0])
#     print(f"{scores_list}")

high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score
print(f"# The highest score in the class is: {high_score}")