class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice, maxProfit = float("inf"), 0
        for price in prices:
            lowestPrice = min(price, lowestPrice)
            maxProfit = max(price - lowestPrice, maxProfit)
        return maxProfit
