class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maximum = nums[0]
        minimum = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                maximum, minimum = minimum, maximum
            
            minimum = min(nums[i], minimum * nums[i])
            maximum = max(nums[i], maximum * nums[i])

            current = max(maximum, current)
        
        return current