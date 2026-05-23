class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_up_to = [prices[0]]
        prof = [0]

        for i in range(1,len(prices)):
            if min_up_to[i-1] > prices[i]:
                min_up_to.append(prices[i])
            else:
                min_up_to.append(min_up_to[i-1])
            if prices[i] - min_up_to[i] > prof[i-1]:
                prof.append(prices[i] - min_up_to[i])
            else:
                prof.append(prof[i-1])
            

        return prof[-1]


        