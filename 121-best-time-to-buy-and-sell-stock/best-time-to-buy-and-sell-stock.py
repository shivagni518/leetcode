class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)):    
        #     for j in range(i+1,len(prices)):
        #         if i < j:
        #             max_profit = max(max_profit,prices[j]-prices[i])
        # return max_profit

        min_prices = prices[0]
        max_prices = 0
        for i in range(1,len(prices)):
            min_prices = min(min_prices,prices[i])
            max_prices = max(max_prices,prices[i]-min_prices)
        return max_prices    


        