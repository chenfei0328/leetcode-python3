import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table = collections.defaultdict(int)
        cmp = collections.defaultdict(int)
        len_p = len(p)
        for c in p:
            table[c] += 1
        
        ans = []
        for i, c in enumerate(s):
            cmp[c] += 1
            
            if i >= len_p:
                cmp[s[i-len_p]] -= 1
                if cmp[s[i-len_p]] == 0:
                    cmp.pop(s[i-len_p])
            
            if cmp == table:
                ans.append(i-len_p+1)
        
        return ans