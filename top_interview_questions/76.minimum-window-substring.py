import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        need = collections.Counter(t)
        # print(need)
        missing = len(t)
        
        i, j = 0, 0
        l = 0
        for r, rchar in enumerate(s):
            if need[rchar] > 0:
                missing -= 1
            need[rchar] -= 1
            
            while missing == 0:
                if j == 0 or r - l < j - i:
                    i, j = l, r + 1
                
                lchar = s[l]
                need[lchar] += 1
                if need[lchar] > 0:
                    missing += 1
                    
                l += 1
        
        return s[i:j]