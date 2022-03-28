""" O(1) is the most efficient form of O.

"""

def add_items(n):
    return n + n
    # Here you just have one operation so it's O(1).
    # If you have return n + n + n it's two operations 
    # but you still call it O(1).
    # O(1) is also called Constant Time because even if the number
    # of operations will remain constant as n increases
