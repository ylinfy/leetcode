class Solution:
    def maxSubArray(self, nums):
        if not nums: return 0
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = cur_sum + nums[i] if cur_sum > 0 else nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
