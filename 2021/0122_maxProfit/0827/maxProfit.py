class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            if delta > 0: maxValue += delta
        return maxValue
