class Solution:
    # 集合判重，最大非零值与最小非零值差小于5即可，time: N
    def isStraight(self, nums):
        repeat = set()
        ma, mi = 0, 14
        for n in nums:
            if n == 0: continue
            ma = max(ma, n)
            mi = min(mi, n)
            if n in repeat: reutrn False
            repeat.add(n)
        return ma - mi < 5


    # 排序，找到最小非零值，同上，time: N*logN (sort: N*logN)
    def isStraight(self, nums):
        joker = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i+1]: return False
        return nums[-1] - nums[joker] < 5

