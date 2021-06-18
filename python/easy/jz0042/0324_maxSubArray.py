class Solution:
    def maxSubArray(self, nums):
        pre = cur = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums))):
            cur = nums[i] if pre < 0 else pre + nums[i] 
            pre = cur
            max_sum = max(max_sum, cur)
        return max_sum
            
