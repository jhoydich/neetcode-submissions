class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_up_to = [prices[0]]
        prof = [0]
        curr_min = prices[0]
        prof = 0

        for i in range(1,len(prices)):
            if curr_min > prices[i]:
                
                curr_min = prices[i]
            
            if prices[i] - curr_min > prof:
            
                prof = prices[i] - curr_min
           
            

        return prof


        