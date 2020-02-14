class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        
        dp = [[0 for _ in range(l)] for _ in range(l)]
        
        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if j - i <= 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = 1
        
        return sum(map(sum, dp))