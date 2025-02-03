class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        increasing, decreasing = 0, 0
        
        for i in range(len(nums)):
            inc = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    inc+=1
                else:
                    break
            
            increasing = max(inc, increasing)

        for i in range(len(nums)):
            dec = 1
            for j in range(i+1, len(nums)):
                if nums[j] < nums[j-1]:
                    dec+=1
                else:
                    break
            
            decreasing = max(dec, decreasing)
        
        return max(increasing, decreasing)