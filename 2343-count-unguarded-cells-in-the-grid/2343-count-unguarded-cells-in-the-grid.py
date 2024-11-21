class Solution:
    """
    0: Unguarded cell
    1: Guarded
    2: Guard Present
    3: Wall
    """
    def dfs(self, x: int, y: int, direction: int, grid: List[List[int]], m: int, n: int):
        # Base conditions to stop DFS
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 2 or grid[x][y] == 3:
            return
        
        grid[x][y] = 1  # Mark as guarded
        # Continue in the same direction
        if direction == 0:       # Up
            self.dfs(x - 1, y, direction, grid, m, n)
        elif direction == 1:     # Right
            self.dfs(x, y + 1, direction, grid, m, n)
        elif direction == 2:     # Down
            self.dfs(x + 1, y, direction, grid, m, n)
        elif direction == 3:     # Left
            self.dfs(x, y - 1, direction, grid, m, n)

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize grid
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        # Mark guards and walls
        for guard in guards:
            grid[guard[0]][guard[1]] = 2
        for wall in walls:
            grid[wall[0]][wall[1]] = 3
        
        # Directions: Up, Right, Down, Left
        directions = [-1, 0, 1, 0, -1]
        
        # Propagate guarding influence
        for guard in guards:
            for i in range(4):
                x, y = guard[0] + directions[i], guard[1] + directions[i + 1]
                self.dfs(x, y, i, grid, m, n)
        
        # Count unguarded cells
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded += 1
        
        return unguarded
