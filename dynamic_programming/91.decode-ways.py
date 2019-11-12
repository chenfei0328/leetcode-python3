class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        l = len(s)
        dp = [1] * l
        
        for i in range(l):
            if s[i] == '0':
                if i - 1 >= 0:
                    if s[i - 1] == '1' or s[i - 1] == '2':
                        if i - 2 >= 0 and (s[i - 2] == '1' or s[i - 2] == '2'):
                            dp[i] = dp[i - 2]
                        else:
                            dp[i] = dp[i - 1]
                    else:
                        return 0
            elif s[i] > '0' and s[i] <= '6':
                if  i - 1 >= 0:
                    if s[i - 1] == '1' or s[i - 1] == '2':
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
            else:
                if i - 1 >= 0:
                    if s[i - 1] == '1':
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
                        
        return dp[-1]
