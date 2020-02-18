class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        profit = 0        
        buy, sell = 0, 0
        
        i = 1
        while i <= len(prices) - 1:
            if prices[i] > prices[buy]:
                sell = i
                i += 1
                
                while i <= len(prices) - 1 and prices[i] >= prices[sell]:
                    sell = i
                    i += 1
                    
                profit += prices[sell] - prices[buy]
                buy = i
            else:
                buy = i
                i += 1
                
        return profit
            