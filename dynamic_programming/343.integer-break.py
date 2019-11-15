class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        
        return dp[n]




class Solution:
    def integerBreak(self, n: int) -> int:
        d, m = divmod(n, 3)
        if m == 0:
            return 2 if n == 3 else 3**d
        elif m == 1:
            return 1 if n == 1 else 3**(d - 1) * 4
        elif m == 2:
            return 1 if n == 2 else 3**d * 2
