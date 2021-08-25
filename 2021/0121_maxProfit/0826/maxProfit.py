class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowPrice, maxValue = float("inf"), 0
        for p in prices:
            lowPrice = min(p, lowPrice)
            maxValue = max(p - lowPrice, maxValue)
        return maxValue
