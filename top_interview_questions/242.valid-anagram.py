import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = collections.Counter(s)
        for c in t:
            if c in counter:
                if counter[c] == 0:
                    return False
                counter[c] -= 1
            else:
                return False
        return True