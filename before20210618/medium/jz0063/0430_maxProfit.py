class Solution:
    # DP, 记录左侧最低买入值mi, dp[i]是以i为结束的当天最大利益值
    # dp[i] = max(dp[i-1], prices[i] - mi)
    def maxProfit(self, prices):
        mi, max_profit = float("inf"), 0
        for p in prices:
            mi = min(mi, p)
            max_profit = max(max_profit, p - mi)
        return max_profit
