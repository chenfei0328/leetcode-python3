class Solution:
    def decodeString(self, s: str) -> str:

        def addStr(l=0, r=len(s)-1):
            ans = ''
            if l == r:
                return s[l]
            
            while l <= r:
                if s[l] >= '0' and s[l] <= '9':
                    k1 = l
                    l += 1 
                    while s[l] >= '0' and s[l] <= '9':
                        l += 1
                    num = int(s[k1:l])
                    # print(num)
                    l += 1
                    k2 = l
                    stack = 1
                    while stack > 0:
                        if s[l] == '[':
                            stack += 1
                        elif s[l] == ']':
                            stack -= 1
                        l += 1
                    ans += num * addStr(k2, l-2)
                else:
                    ans += s[l]
                    l += 1
            return ans
                
        return addStr()