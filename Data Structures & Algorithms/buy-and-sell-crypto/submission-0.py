class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for day in range(len(prices)):
            buyPrice = prices[day]
            profits = [prices[sellDay] - buyPrice for sellDay in range(day+1, len(prices))]
            if profits:
                maxProfit = max(max(profits), maxProfit)
        return maxProfit
        