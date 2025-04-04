class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [0] * len(grid)
        col_count = [0] * len(grid[0])
        total_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        total_count += 1
        
        return total_count
