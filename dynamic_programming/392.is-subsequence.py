class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        i = j = 0
        s_len, t_len = len(s), len(t)
        
        while 1:
            if s_len - i > t_len - j or j >= t_len:
                return False

            if s[i] == t[j]:
                i += 1
                j += 1
                if i == s_len:
                    return True
            else:
                j += 1
