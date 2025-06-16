class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        maximum = float('-inf')
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i < j and nums[i] < nums[j]:
                    diff = nums[j] - nums[i]

                    maximum = max(maximum, diff)
            
        
        return maximum if maximum != float('-inf') else -1