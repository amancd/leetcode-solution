class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        def fn(i, j, k):
            return max((i - j) * k, 0)
        
        maximum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                for k in range(j + 1, len(nums)): 
                    maximum = max(maximum, fn(nums[i], nums[j], nums[k]))

        return maximum
