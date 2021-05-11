class Solution:
    # DP, time: N
    # 遍历prices，用mi记录左侧最低价，用res来记录最大利益, 最终返回res
    def maxProfit(self, prices):
        if not prices: return 0
        mi, res = float("inf"), 0 
        for num in prices:
            if num < mi: mi = num
            # dp[i] = max(dp[i-1], num - mi), num当前值，mi左侧最小值 
            res = max(res, num - mi)  # dp[i] = max(dp[i-1], num - mi) 
        return res
                
            
            
