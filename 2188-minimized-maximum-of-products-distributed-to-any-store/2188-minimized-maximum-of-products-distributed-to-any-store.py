import math
from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        minimum = right

        while left <= right:
            mid = (left + right) // 2
            total = 0
            for quantity in quantities:
                total += math.ceil(quantity / mid)
            
            if total <= n:
                minimum = mid
                right = mid - 1
            else:
                left = mid + 1

        return minimum
