"""
Paste your docstring here
"""

def first_unique(A):
    from collections import Counter
    counts = Counter(A)          # Step 1: count occurrences
    for idx, char in enumerate(A):  # Step 2: find first unique
        if counts[char] == 1:
            return idx
    return -1                   # no unique character
        