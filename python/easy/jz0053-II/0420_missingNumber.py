class Solution:
    # 二分查找，time: logN
    # 左右子数以nums[i] != i为界，且该nums[i]为右子数的首位元素，i就是需要找到的值
    def missingNubmer(self, nums):
        if not nums: return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == m: l = m + 1
            else: r = m - 1
        return l
