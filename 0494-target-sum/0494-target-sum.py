class Solution:
    def findTargetSumWays(self, a: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i, cur):
            if i == len(a): return cur == target
            return dp(i+1, cur+a[i]) + dp(i+1, cur-a[i])
        return dp(0, 0)