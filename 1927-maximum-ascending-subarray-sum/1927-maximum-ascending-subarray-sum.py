class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum = 0
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j-1] < nums[j]:
                    curr+=nums[j] 
                   
                else:
                    break

                maximum = max(maximum, curr)

        if max(nums) > maximum:
            return max(nums)
        
        return maximum