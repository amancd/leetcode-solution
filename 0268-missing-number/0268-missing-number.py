class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            if i not in nums:
                return i

        if n not in nums:
            return n
            
        return n+1