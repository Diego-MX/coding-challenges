from functools import reduce
from typing import List

def digits_2_num(dd): 
    base_10 = lambda n, d: 10*n + d
    return reduce(base_10, dd)


class Solution:
    def sequentialDigits(self, low:int, high:int) -> List[int]: 
        between = lambda ss: low <= ss <= high
        one_nine = '123456789'
        all_seqs = map(int, 
            (one_nine[i:(j+1)] for j in range(9) for i in range(j)))
        return list(filter(between, all_seqs))


def seqs_len_k(kk): 
    first = digits_2_num((i+1 for i in range(kk)))
    ones = digits_2_num((1 for i in range(kk)))
    return [first + ones*i for i in range(10-kk)]


class Solution2: 
    def sequentialDigits(self, low:int, high:int) -> List[int]: 
        k0 = len(str(low))
        k1 = len(str(high))

        ll = seqs_len_k(k0)
        if k1 > k0: 
            ll.extend(seqs_len_k(k1))

        between = lambda ss: low <= ss <= high
        return list(filter(between, ll))

