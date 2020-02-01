class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        subStr = {}
        subStrHead = 0
        longest = 0
        
        for i, char in enumerate(s):
            if char in subStr:
                longest = max(longest, len(subStr))
                index = subStr[char]
                for j in range(subStrHead, index + 1):
                    del subStr[s[j]]
                subStrHead = index + 1
            subStr[char] = i
        longest = max(longest, len(subStr))
        return longest