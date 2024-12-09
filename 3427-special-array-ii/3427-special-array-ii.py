class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            if nums[i - 1] % 2 == nums[i] % 2:
                prefix[i] += 1

        res = []

        for l, r in queries:
            if l > 0:
                count = prefix[l] - prefix[r] 
            else:
                count = prefix[r]
        
            res.append(count == 0)

        return res