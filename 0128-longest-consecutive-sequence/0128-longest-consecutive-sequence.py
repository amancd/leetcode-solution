class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()

        maximum = 1
        count = 1

        if len(nums) == 1:
            return 1

        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue

            if abs(nums[i] - nums[i-1]) == 1:
                count +=1
                maximum = max(maximum, count)
            else:
                count = 1
        
        return maximum