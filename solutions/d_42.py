from itertools import accumulate as accum
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = accum(height, max)
        rev_right = list(accum(reversed(height), max))
        top = map(min, zip(left, reversed(rev_right)))
        λ_fill = lambda t, h: max(t - h, 0)
        return sum(map(λ_fill, top, height))
    
    def trap2(self, height: List[int]) -> int:
        fill, left, right = 0, 0, max(height)
        for i, h in enumerate(height): 
            left = max(left, h)
            right = right if h < right else max(height[i:])
            fill += max(min(left, right)-h, 0)
        return fill
