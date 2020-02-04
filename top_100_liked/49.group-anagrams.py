class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for item in strs:
            tmp = ''.join(sorted(item))
            if tmp in s:
                s[tmp].append(item)
            else:
                s[tmp] = [item]

        ans = []
        for value in s.values():
            ans.append(value)
            
        return ans