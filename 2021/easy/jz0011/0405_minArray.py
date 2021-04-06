class Solution:
    def minArray(self, numbers):
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0] if numbers else None

    # 二分查找
    def minArray(self, numbers):
        if not numbers: return
        l, r = 0, len(numbers) - 1
        while l < r:
            m = l + ((r - l) >> 1)
            # 此处不能和numbers[l]比较，如[1,2,3,4,5]和[3,4,5,1,2], 都满足num[m] > num[l], 缩小到[m+1, r]对[1,2,3,4,5]就不对了
            if numbers[m] == numbers[r]: r -= 1
            elif numbers[m] > numbers[r]: l = m + 1
            else: r = m
        return numbers[l]
