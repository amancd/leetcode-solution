class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        res = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in ans:
                    ans.append(grid[i][j])
                else:
                    res.append(grid[i][j])
        
        n = len(grid) * len(grid)
        for i in range(1, n+1):
            if i not in ans:
                res.append(i)


        return res
        
