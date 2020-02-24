class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        path = 1
        m, n = len(matrix), len(matrix[0])
        visited = {}
        
        def dfs(i, j, visited):
            if (i, j) in visited:
                return visited[(i, j)]
            
            path_len = [0]   
            for x, y in ((i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)):
                if 0 <= x < m and 0 <= y < n:
                    if matrix[x][y] > matrix[i][j]:
                        path_len.append(dfs(x, y, visited))
            
            val = 1 + max(path_len)
            visited[(i, j)] = val
            return val
        
        for i in range(m):
            for j in range(n):
                path = max(path, dfs(i, j, visited))
                visited.clear()
        return path
            