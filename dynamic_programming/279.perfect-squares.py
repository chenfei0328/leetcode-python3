# Time Limit Exceeded
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        curr = 2
        while curr*curr <= n:
            for j in range(curr*curr,n+1):
                dp[j] = min(dp[j],dp[j-curr*curr]+1)
            curr+=1
        return dp[-1]


class Solution:
    def numSquares(self, n):
        if n**(0.5)==int(n**0.5):
            return 1

        while (n&3==0):
            n>>=2
        if n&7==7:
            return 4

        for i in range(1,int(n**(0.5))+1):
            if (n-i*i)**(0.5) == int((n-i*i)**(0.5)):
                return 2
        return 3
