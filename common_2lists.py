"""
You are given two lists written in ascending order. Find the common elements between the two. 

"""

list_1 = [1, 3, 4, 6, 7, 9]

list_2 = [1, 2, 4 ,5, 9, 10]

# common_elements(list_1, list_2) -> [1, 4, 9]

def common_elements(list_1, list_2):
    result =[]
    for i in list_1:
        if (i in list_2):
            result.append(i)
    return result