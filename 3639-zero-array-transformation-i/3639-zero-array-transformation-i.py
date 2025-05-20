class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        # Brute Force
        # for query in queries:

        #     x, y = query

        #     while x<=y:
        #         if nums[x] != 0:
        #             nums[x] -= 1
        #         x+=1
        
        # print(nums)

        # if set(nums) == {0}:
        #     return True
        
        # return False

        # Optimal

        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        available = [0] * n
        available[0] = diff[0]
        
        for i in range(1, n):
            available[i] = available[i - 1] + diff[i]

        for i in range(n):
            if nums[i] > available[i]:
                return False

        return True