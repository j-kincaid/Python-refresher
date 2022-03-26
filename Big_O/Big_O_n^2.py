def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
print_items(10)

""" 
You would think that because this prints from 000 to 999 
we would call it O(n^3), but we drop it down to O(n^2). 
O(n^3) has a steeper curve on the graph so it is a heck of 
a lot less efficient from a time complexity standpoint. 
It doesn't matter if it's O(n^5), O(n^8), or whatever, we 
always simplify it to O(n^2).
"""