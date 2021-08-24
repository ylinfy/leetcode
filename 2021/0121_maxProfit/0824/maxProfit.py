class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice, maxProfit = float("inf"), 0
        for p in prices:
            lowestPrice = min(p, lowestPrice) 
            maxProfit = max(maxProfit, p - lowestPrice)
        return maxProfit

