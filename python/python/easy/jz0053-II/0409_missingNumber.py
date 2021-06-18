class Solution:
    # 二分查找, time: logN
    # 找到右子数组首位元素，左右子数组以nums[i] != i为界，且该nums[i]为右子数组首位元素
    def missingNumber(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == m: l = m + 1
            else: r = m - 1
        return l


    # time: N
    # 遍历，遍历完仍未发现目标，说明是少了最后一个数
    # 例如[0,1,2,3], 长度为n-1,说明n=5, 即应该是0,1,2,3,4，所以少了4
    def missingNumber(self, nums):
        for i, n in enumerate(nums):
            if n != i: return i
        return len(nums)
