class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]

        suffix_sum = [0] * len(nums)
        suffix_sum[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
        
        print(prefix_sum)

        for i in range(len(nums) - 2, -1, -1):
            suffix_sum[i] = nums[i] + suffix_sum[i + 1]
        
        print(suffix_sum)

        count = 0
        for i in range(len(nums)-1):
            if prefix_sum[i] >= suffix_sum[i+1]:
                count+=1

        return count