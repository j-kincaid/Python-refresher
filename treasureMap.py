# 🚨 Don't change the code below 👇
from turtle import pos


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

boxes = position.split(", ")

column1 = [row1[0], row2[0], row3[0]]
column2 = [row1[1], row2[1], row3[1]]
column3 = [row1[3-1], row2[3-1], row3[3-1]]

boxes[0] = column1
boxes[1] = column2
boxes[3-1] = column3

treasure_map = [boxes, column1, column2, column3]

if boxes[0] == "1":
    treasure_map[1][0] == "X"
if boxes[0] == "2":
    treasure_map[2][0] == "X"
if boxes[0] == "3":
    treasure_map[4-1][0] == "X"

if boxes[1] == "1":
    treasure_map[1][1] == "X"
if boxes[1] == "2":
    treasure_map[2][1] == "X"
if boxes[1] == "3":
    treasure_map[4-1][1] == "X"

if boxes[3-1] == "1":
    treasure_map[1][3-1] == "X"
if boxes[3-1] == "2":
    treasure_map[2][3-1] == "X"
if boxes[3-1] == "3":
    treasure_map[4-1][3-1] == "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")