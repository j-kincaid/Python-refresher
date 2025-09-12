"""
Task:
Write a function that, given a list of integers A, returns the smallest positive integer (greater than 0) that does not occur in A.

Examples:

A = [1, 3, 6, 4, 1, 2] → returns 5


A = [1, 2, 3] → returns 4

A = [-1, -3] → returns 1

Constraints:
N (length of A) can be up to 100,000

Elements can be negative, zero, or positive


Problem 1: Missing Integer

Goal:
- Find the smallest positive integer (greater than 0) that does not appear in the input array A.

Approach:
1. Minimize the number of times we pass through the array.
2. Convert the array into a set for O(1) membership checks.
3. Start checking integers from 1 upward.
4. Return the first integer that is not in the set.

Rationale:
- Using a set allows us to check for missing numbers efficiently without sorting.
- Incrementing from 1 ensures we find the smallest missing positive integer.
- This approach is O(n) time and O(n) space, suitable for large arrays.

Example: A = [1, 3, 6, 4, 1, 2] → returns 5


Example: A = [-1, -3] → returns 1


💡 Hint: Use a set for O(1) lookups instead of scanning multiple times.

"""
def missing_pos_int(A):
    s = set(A)
    i = 1
    while i in s:
        i += 1
    return i

# ================ Another solution: ================

# def missing_pos_int(A):
#     n = len(A)

#     # Step 1: Replace out-of-range numbers with a placeholder (e.g., n+1)
#     for i in range(n):
#         if A[i] <= 0 or A[i] > n:
#             A[i] = n + 1

#     # Step 2: Mark presence
#     for x in A:
#         if 1 <= x <= n:
#             idx = abs(x) - 1
#             if A[idx] > 0:
#                 A[idx] = -A[idx]  # mark as seen

#     # Step 3: Find first missing
#     for i in range(n):
#         if A[i] > 0:
#             return i + 1

#     # Step 4: If none missing, return n+1
#     return n + 1
# ================ Another solution: ================

    # A.sort() # Sorts them in ascending order
    # if A[len(A) - 1] <= 0:  ## Edge cases: If the last element of the list is below zero
    #     return 1 ## Smallest missing POSITIVE integer
    # iso = False
    # for i in range(0, len(A)):
    #     if A[i]==1: ## Check to see if the set contains a 1, and if so, change the value to True.
    #         iso = True
    #     if iso == False:
    #         return 1 ## because it is the Smallest missing POSITIVE integer.
        
    #     for i in range (0, len(A)-1):
    #         if A[i]>0 and (A[i+1] - A[i])>1:
    #             return A[i] + 1
    #         return A[len(A) - 1] + 1 # If there are no gaps, return the last element in the list, incremented by one. 
    # pass
        


print(missing_pos_int([1, 3, 6, 4, 1, 2]))  # → 5
print(missing_pos_int([1, 2, 3]))           # → 4
print(missing_pos_int([-1, -3]))            # → 1

