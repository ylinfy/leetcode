class Solution: 
    def maxProfit(self, prices):
        mi, res = float("inf"), 0
        for n in prices:
            mi = min(mi, n)
            res = max(res, n - mi)
        return res

