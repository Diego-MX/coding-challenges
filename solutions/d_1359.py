from functools import reduce

M_BASE = 10**9 + 7

class Solution: 
    def countOrders(self, n:int) -> int: 
        prod_mod = lambda p, j: (p*j*(2*j - 1)) % M_BASE
        return reduce(prod_mod, range(1, n+1))
