class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = obstacleGrid
        if dp[0][0]:
            return 0
        m, n = len(dp), len(dp[0])
        
        block = False
        for i in range(m):
            if dp[i][0]:
                block = True
            if block:
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        
        block = False
        for j in range(1, n):
            if dp[0][j]:
                block = True
            if block:
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
