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


def missing_integer(A):
    n = len(A)

    # Step 1: Replace out-of-range numbers with a placeholder (e.g., n+1)
    for i in range(n):
        if A[i] <= 0 or A[i] > n:
            A[i] = n + 1

    # Step 2: Mark presence
    for x in A:
        if 1 <= x <= n:
            idx = abs(x) - 1
            if A[idx] > 0:
                A[idx] = -A[idx]  # mark as seen

    # Step 3: Find first missing
    for i in range(n):
        if A[i] > 0:
            return i + 1

    # Step 4: If none missing, return n+1
    return n + 1

print(missing_integer([1, 3, 6, 4, 1, 2]))  # → 5
print(missing_integer([1, 2, 3]))           # → 4
print(missing_integer([-1, -3]))            # → 1

