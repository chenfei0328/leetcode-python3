class Solution:
    def romanToInt(self, s: str) -> int:
        t = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans = 0
        l = len(s)
        for i, c in enumerate(s):
            if i < l - 1:
                if t[c] < t[s[i + 1]]:
                    ans -= t[c]
                    continue
            ans += t[c]
            
        return ans