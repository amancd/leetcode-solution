from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = {}
        count = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product in freq:
                    freq[product] += 1
                else:
                    freq[product] = 1


        for v in freq.values():
            if v > 1:
                count += (v * (v - 1) // 2) * 8

        return count
