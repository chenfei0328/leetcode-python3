from itertools import product
from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        AB = product(A, B)
        CD = product(C, D)
        
        sumAB = Counter(x + y for (x, y) in AB)
        sumCD = Counter(x + y for (x, y) in CD)
        
        for item in sumAB:
            if -item in sumCD:
                count += sumAB[item] * sumCD[-item]
                
        return count


import collections 
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = collections.Counter(C)
        d = collections.Counter(D)

        count = 0
        A = collections.defaultdict(int)
        B = collections.defaultdict(int)
        for i, ai in a.items():
            for j, bj in b.items():
                A[i + j] += (ai * bj)

        for i,ai in c.items():
            for j, bj in d.items():
                B[i + j] += (ai * bj)

        for i, a in A.items():
            num = -i
            if num in B:
                count += (a * B[num])
        return count