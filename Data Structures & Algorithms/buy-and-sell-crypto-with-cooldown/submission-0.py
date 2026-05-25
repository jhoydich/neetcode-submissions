class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            # take either the previous val or the max of selling today and 
            prev = profit[i-1]
            mt = 0
            for j in range(i):
                tb = profit[j-2] if j > 1 else 0
                if tb + prices[i] - prices[j] > mt:
                    mt = tb + prices[i] - prices[j]
            profit[i] = max(mt, prev)
        return profit[-1]