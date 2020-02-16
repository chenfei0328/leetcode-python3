class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        l1, l2 = len(haystack), len(needle)
        if l1 < l2:
            return -1
        
        for i in range(0, l1 - l2 + 1):
            j = 0
            while j < l2 and haystack[i + j] == needle[j]:
                j += 1
            if j == l2:
                return i
            
        return -1
        