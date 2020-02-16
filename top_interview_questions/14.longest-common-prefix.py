class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        
        for i in range(1, len(strs)):
            l = len(strs[i])
            k = 0
            tmp = ''
            while k < l and k < len(prefix):
                if prefix[k] == strs[i][k]:
                    tmp += prefix[k]
                    k += 1
                else:
                    break
            
            if not tmp:
                return ""
            else:
                prefix = tmp
                
        return prefix
            
            
        