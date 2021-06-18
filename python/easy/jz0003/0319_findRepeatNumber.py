class Solution:
    def findRepeatNumber(self, nums):
        tmp = set()
        for n in nums:
            if n in tmp:
                return n
            tmp.add(n)
            
    def findRepeatNumber(self, nums):
        for i in range(len(nums)):
            if nums[i] == i: continue
            if nums[i] == nums[nums[i]]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
