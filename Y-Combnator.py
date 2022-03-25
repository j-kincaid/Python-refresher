# count_ways([1, 5], 10)

# Counting ways to make change

# 1. 5 + 5 =  10
# 2. 1 + 1 + 1 + 1 + 1 + 1 +1 + 1 + 1 + 1
# 3. 5 + 1 +1 + 1 + 1 + 1

######################################################################
### Jumbled notes from Tom's lecture at PythonKC
######################################################################

from cgi import test
from itertools import count
import unittest



class TestCountWays(unittest.TestCase):

    def test_counts_ways_no_denominations(self):
        denominations = []
        amount = 100
        result = 0
        self.assertEqual(count_ways(denominations, amount), result)  

    def test_counts_ways_one_and_five_eq_ten(self):
        denominations = [1, 5]
        amount = 10
        result = 3
        self.assertEqual(count_ways(denominations, amount), result)

    def test_counts_ways_to_make_hundred(self):
            denominations = [1, 2, 5, 10, 20, 50, 100]
            amount = 100
            result = 424
            self.assertEqual(count_ways(denominations, amount), result)

    def count_ways(denominations, amount):
        # what is the base case?
        if amount < 0:
            return 0
        elif not denominations:
            return 0
        # recursive step
        # if first denomination matches amount, we found a way to make change
        # else we did not (int(...))
        return \
            int(denominations[0] == amount) \ 
            + count_ways(denominations, amount - denominations[0]) \ make progress toward first base case? 
            + count_ways(denominations[1:], amount) \ make progress toward second base case? 
