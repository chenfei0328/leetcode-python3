class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        l = len(s)
        ans = []
        
        def trackback(s, out=[]):
            if not s:
                ans.append(out[:])
            
            for i in range(len(s)):
                c = s[:i + 1]
                if c == c[::-1]:
                    out.append(c)
                    trackback(s[i + 1:])
                    out.pop()
                    
        trackback(s)
        return ans
                