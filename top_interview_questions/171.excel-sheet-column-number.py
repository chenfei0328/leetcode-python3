class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0
        
        l = len(s)
        k = 1
        ans = 0
        for i in range(l - 1, -1, -1):
            ans += k * (ord(s[i]) - 64)
            k *= 26
        
        return ans