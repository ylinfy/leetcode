class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # pre: 以当前下标i为结尾的连续子数组的最大和
        # res: nums[:i]中最大连续子数组和 
        res = pre = nums[0]
        for i in range(1, len(nums)):
            pre = max(nums[i], pre + nums[i])
            res = max(pre, res)
        return res

