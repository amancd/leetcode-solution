class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        res = float('-inf')

        for i in range(1, len(nums)):
            diff = abs(nums[i-1] - nums[i])
            res = max(res, diff)
        
        if len(nums)>=2:
            diff = abs(nums[0] - nums[-1])
            res = max(res, diff)
        
        return res
