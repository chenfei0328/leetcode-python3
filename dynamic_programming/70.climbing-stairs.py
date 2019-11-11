class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        pre1, pre2 = 2, 1
        
        for k in range(2, n):
            now = pre1 + pre2
            pre2 = pre1
            pre1 = now
        return now
