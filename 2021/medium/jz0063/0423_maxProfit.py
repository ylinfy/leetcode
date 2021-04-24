class Solution:
    def maxProfit(self, prices):
        mi, max_pro = float("inf"), 0
        for p in prices:
            mi = min(mi, p)
            max_pro = max(max_pro, p - mi)
        return max_pro
