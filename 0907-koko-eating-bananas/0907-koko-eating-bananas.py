import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        right = max(piles)
        left = 1

        while left <= right:
            mid = (left + right)//2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)

            if total <=h:
                minimum = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return minimum