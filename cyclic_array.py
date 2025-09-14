"""
Task:
Given an array of integers A and a number K, rotate the array K times to the right.

Example:

A = [3, 8, 9, 7, 6]
K = 3
# After rotation: [9, 7, 6, 3, 8]

Write a function in Python that returns the rotated array. Keep it O(n) time if possible.

⸻

Hints to think through first (no coding yet)
	1.	What happens if K > len(A)?
	2.	Can you use slicing instead of a loop?
	3.	How do you make sure the rotation is rightward?

    Rationale:
    # Using a set for A allows us to organize numbers efficiently through O(n) without sorting. 

"""

def rotate(A, K):
    N = len(A)
    if N == 0:
        return A
    K = K % N  # handles K > len(A) automatically
    return A[-K:] + A[:-K]

# Example test cases
test_cases = [
    ([3, 8, 9, 7, 6], 3),
    ([1, 2, 3, 4, 5], 2),
    ([10, 20, 30], 4),
    ([], 5),
    ([1, 2, 3], 0)
]

for A, K in test_cases:
    result = rotate(A, K)
    print(f"A={A}, K={K} → rotated={result}")