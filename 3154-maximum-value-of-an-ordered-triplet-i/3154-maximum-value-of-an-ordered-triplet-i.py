from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        def fn(i, j, k):
            return max((i - j) * k, 0)  # Ensures non-negative result
        
        maximum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # j > i
                for k in range(j + 1, len(nums)):  # k > j
                    maximum = max(maximum, fn(nums[i], nums[j], nums[k]))  # Fix: Move this inside k loop

        return maximum
