"""
Write a program that returns the most frequent integer in a given array.

[1, 3, 1, 3, 2, 1]

"""

listA = [1, 3, 1, 3, 2, 1];
# the output will look like:
## return 1

#We have to test the numbers as we go across
# add them to a new list when we get a new value
# then evaulate the longest list or greatest sum of items in the list

# if listA[0] = 0
# 0list += 1
# elif listA[0] = 1
# 1List +=1

# when there's a new integer, start a new list
# Which len(list) is greatest


# listA[1] = 3

# listA[2] = 1


# Welcome to a bigO of n problem. 
# It uses a dictionary / hash table

given_list = [1, 3, 1, 3, 2, 1];
def frequent(given_list) {
    max_count = -1
    max_item = None
    count = {} # empty dictionary to store key-value pairs
    for i in given_list:
        if i not in count:
            count[i] = 1 # key is 1 and value is 1, we have seen the number once so far.
        else:
            count[i] += 1 # else, if the value is already in the count dictionary, we increment the value by 1.
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item
}