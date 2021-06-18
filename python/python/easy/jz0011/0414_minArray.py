class Solution:
    # 二分查找，旋转数组(有序数组旋转一次形成)可直接用二分查找处理
    # time: logN
    def minArray(self, numbers):
        if not numbers: return 0 
        l, r = 0, len(numbers) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            # 此处只能和nums[r]进行比较，与nums[l]比较不能正确的划分左右区间
            # 如[1,2,3,4,5]和[4,5,1,2,3], nums[m]都是大于nums[l], 但数组的最小值分别在左，右区
            # 即没法确定半区间的选择
            if numbers[m] > numbers[r]: l = m + 1
            elif numbers[m] < numbers[r]: r = m 
            else: r -= 1
        return numbers[l]
