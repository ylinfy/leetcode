class Solution:
    def isStraight(self, nums):
        repeat = set()
        ma, mi = 0, 14
        for n in nums:
            if n in repeat: return False
            if n == 0: continue
            ma = max(ma, n)
            mi = min(mi, n)
            repeat.add(n)
        return ma - mi < 5
    
    def isStraight(self, nums):
        joker = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i+1]: return False
        return nums[-1] - nums[joker] < 5
            
            
