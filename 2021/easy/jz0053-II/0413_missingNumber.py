class Solution:
    def missingNumber(self, nums):
        if not nums: return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == m: l = m + 1
            else: r = m - 1
        return l
