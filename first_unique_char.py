"""
Given a string s, return the index of the first non-repeating character. If none exists, return -1.
Example: "leetcode" → returns 0


Examples: 
A = "aabb" → -1
A = "loveleetcode" → 2 (the first unique character is 'v')

==========
Rationale:
# Thinking in terms of counts
# If i is identical to a previous index, it gets added to a count. There is a repeat so when the loop exits return 0.
# Else, (no unique characters), return -1

"""

def first_unique_char(A):
    s = list(A)
    s.sort()
    i = 0
    for i in s:
        # s += i
        if i == i:
            # return 0
            print('-1')
        else:
            # return - 1
            print('0')
        
A = "aabb"
first_unique_char(A)
        