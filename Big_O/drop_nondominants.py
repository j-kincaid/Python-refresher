def list_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# That's O(n^2)

    for k in range(n):
        print(k)

# This one's just O(n)
list_items(10)

#The result is O(n^2 + n)
# When you get to large numbers, let's say 100, 
# O(n^2) is going to be 10,000 and that 
# little n by itself becomes insignificant/nondominant.
# You drop the nondominants and it becomes
# O(n^2) again.