class Solution:
    # 动态规划：time: N
    # 求连续子问题和或者长度，状态转移：以i索引结尾的连续最大和或长度为dp[i]
    # 求连续子数组和：dp[i] = nums[i] if dp[i-1] < 0 else dp[i-1] + nums[i]
    # 求无重复元素连续子数组长度：dp[j] = dp[j-1] + 1 if dp[j-1] < j - i else j - i (以j为结尾的连续子数组最大长度，i是左边第一个和j索引相同的值的索引)
    def maxSubArray(self, nums):
        if not nums: return 0
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = cur_sum + nums[i] if cur_sum > 0 else nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
