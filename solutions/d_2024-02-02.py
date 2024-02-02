from functools import reduce
from typing import List


def digits_2_num(dd:List[int]) -> int:
    base_10 = lambda n, d: 10*n + d
    return reduce(base_10, dd)

def sequence_at(ff:int, kk:int) -> int:
    if ff+kk > 10: 
        return None
    digits = [ff + i for i in range(kk)]
    return digits_2_num(digits)

def next_sequential(nn:int) -> int: 
    k = len(str(nn))
    f = int(str(nn)[0])
    s0 = sequence_at(f, k)
    if s0 and (s0 >= nn): 
        return s0
    return sequence_at(f+1, k) or sequence_at(1, k+1)

class Solution:
    def sequentialDigits(self, low:int, high:int) -> List[int]: 
        s0 = next_sequential(low)
        ss = []
        while s0 and (s0 <= high): 
            ss.append(s0)
            s0 = next_sequential(s0+1)
        return ss
