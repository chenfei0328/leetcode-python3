class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [0 for _ in range(l + 1)]
        dp[0] = 1
        
        for i in range(l):
            if dp[i]:
                for j in range(i+1, l+1):
                    if s[i:j] in wordDict:
                        dp[j] = 1
        # print(dp)               
        return dp[-1]
        