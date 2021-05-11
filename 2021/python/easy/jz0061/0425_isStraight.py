class Solution:
    def isStraight(self, nums):
        if len(nums) < 5: return False
        mi, ma, repeat = 14, 1, set()
        for n in nums:
            if n == 0: continue
            if n in repeat: return False
            repeat.add(n)
            mi, ma = min(mi, n), max(ma, n)
        return ma - mi < 5


    def isStraight(self, nums):
        if len(nums) < 5: return False
        joker = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i+1]:
                return False
        return nums[-1] - nums[joker] < 5
