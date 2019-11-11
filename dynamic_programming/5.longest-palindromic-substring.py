class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s) 
        longestSubStr = ''
        longestStrLen = 0
        
        if l < 2 or s == s[::-1]:
            return s
        
        # i: len of subStr
        for i in range(1, l):
            # j: position form 0 to l-i
            for j in range(l - i + 1):
                subStr = s[j: j + i]
                if subStr == subStr[::-1] and longestStrLen < len(subStr):
                    longestStrLen = len(subStr)
                    longestSubStr = subStr

        return longestSubStr


class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s) 
        dp = [[0 for i in range(l)] for j in range(l)]
        longestSubStr = ''
        longestStrLen = 0
        
        # i: len of subStr
        for i in range(l):
            # j: position form 0 to i
            for j in range(i + 1):
                # init the dp when len = 1 or 2 
                if i - j <= 1:
                    if s[i] == s[j]:
                        dp[j][i] = 1
                        if longestStrLen < i - j + 1:
                            longestStrLen = i - j + 1
                            longestSubStr = s[j: i + 1]
                # start to calculate
                else:
                    if s[i] == s[j] and dp[j + 1][i - 1]:
                        dp[j][i] = 1
                        if longestStrLen < i - j + 1:
                            longestStrLen = i - j + 1
                            longestSubStr = s[j: i + 1]
        return longestSubStr


class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s) 
        dp_old = [0] * l
        dp_new = [0] * l
        longestSubStr = ''
        longestStrLen = 0
        
        # i: len of subStr
        for i in range(l):
            # j: position form 0 to i
            for j in range(i + 1):
                # init the dp when len = 1 or 2 
                if i - j <= 1:
                    if s[i] == s[j]:
                        dp_new[j] = 1
                        if longestStrLen < i - j + 1:
                            longestStrLen = i - j + 1
                            longestSubStr = s[j: i + 1]
                # start to calculate
                else:
                    if s[i] == s[j] and dp_old[j + 1]:
                        dp_new[j] = 1
                        if longestStrLen < i - j + 1:
                            longestStrLen = i - j + 1
                            longestSubStr = s[j: i + 1]
            dp_old = dp_new
            dp_new = [0] * l
        return longestSubStr
