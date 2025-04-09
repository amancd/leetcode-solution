class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        Hash = {}
        res = 0
        for num in nums:
            if num < k: return -1
            if num not in Hash and num != k:
                Hash[num] = 1
                res += 1
        return res