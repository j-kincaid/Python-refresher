def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)

# This prints n items twice. 
# It seems like we would write O(2n) but the rule is to drop the constant.
# We really write it O(n)