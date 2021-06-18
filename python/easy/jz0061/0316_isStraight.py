class Solution:
    # 没有重复，并且最大值减非零最小值小于5，即可构成顺子
    # 集合判重，time: N
    def isStraight(self, nums):
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue
            ma = max(ma, num)
            mi = min(mi, num)
            if num in repeat: return False
            repeat.add(num)
        return ma - mi < 5

    
    # 排序，找最大值和非零最小值，time: N*logN (sort时间复杂度)
    def isStraight(self, nums):
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i+1]: return False
        return nums[4] - nums[joker] < 5
            
