class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:    
        dp = [i for i in range(amount + 1)]

        for i in range(1, amount + 1):
            minx = float('inf')
            for coin in coins:
                if coin <= i:
                    minx = min(dp[i - coin] + 1, minx)
# the coins might not be ordered
#		else:
#		    break
            dp[i] = minx

        return -1 if dp[-1] == float('inf') else dp[-1]
