class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minval = prices[0]
        profitmax = 0
        
        for i in prices:
            minval = min(i, minval)
            profitmax = max(i-minval, profitmax)
        return profitmax
