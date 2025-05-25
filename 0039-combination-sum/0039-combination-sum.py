class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for candidate in candidates:
            for current_target in range(candidate, target + 1):
                for combination in dp[current_target - candidate]:
                    dp[current_target].append(combination + [candidate])
        
        return dp[target]