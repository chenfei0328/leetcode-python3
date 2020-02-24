class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        index = set()

        for i, c in enumerate(s):
            if c in table:
                # print(table)
                index.discard(table[c])
            else:
                index.add(i)
                table[c] = i
                
        return min(index) if index else -1



import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1