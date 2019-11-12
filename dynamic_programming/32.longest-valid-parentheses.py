class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        
        dp = [0] * len(s)
        longest = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + (dp[i - 2] if i > 2 else 0)
                    longest = max(longest, dp[i])
                else:
                    if (i - 1 - dp[i - 1] >= 0) and s[i - 1 - dp[i - 1]] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[i - 2 - dp[i - 1]] if i - 1 - dp[i - 1] >= 1 else 0)
                        longest = max(longest, dp[i])
        #print(dp)
        return longest
