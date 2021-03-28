class Solution:
    def maxSubArray(self, nums):
        pre, cur = 0, nums[0]
        max_sum = nums[0]
        for i in range(len(nums)):
            cur = nums[i] if pre <= 0 else pre + nums[i]
            pre = cur
            max_sum = max(max_sum, cur)
        return max_sum


    def maxSubArray(self, nums):
        if not nums: return 0
        cur_sum = max_sum = float('-inf')
        for i in range(len(nums)):
            cur_sum = nums[i] if cur_sum < 0 else cur_sum + nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
