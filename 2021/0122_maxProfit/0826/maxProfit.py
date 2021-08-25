class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i-1]
            if delta > 0: max_value += delta
        return max_value
