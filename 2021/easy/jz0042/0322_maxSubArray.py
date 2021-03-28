class Solution:
    # dp, time: N, space: 1
    # dp[i]: 以nums[i]为结尾的连续子数组最大和，因为明确要以nums[i]结尾，只可能出现以下两种情况：
    # dp[i-1] > 0: dp[i-1] + nums[i] 
    # dp[i-1] <= 0: nums[i]
    # 因为只与dp[i-1]和nums[i]有关，将pre, cur设置为dp[i-1]和dp[i], 递归下去, 每一步中求出相应最大和
    def maxSubArray(self, nums):
        if not nums: return nums
        pre, max_sum = 0, nums[0]
        for n in nums:
            cur = (pre + n) if pre > 0 else n
            max_sum, pre = max(max_sum, cur), cur
        return max_sum

        
            
