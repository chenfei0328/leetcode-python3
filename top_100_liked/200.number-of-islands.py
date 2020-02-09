class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    dfs(x, y)
        
        num = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num += 1
                    visited = dfs(i, j)
        return num