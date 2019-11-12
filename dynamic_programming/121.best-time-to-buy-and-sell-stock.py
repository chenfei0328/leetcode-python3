class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        value = 0
        min_v = max_v = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_v:
                min_v = max_v = prices[i]
            elif prices[i] > max_v:
                max_v = prices[i]
                value = max(value, max_v - min_v)
        return value
