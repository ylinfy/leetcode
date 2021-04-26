class Solution:
    def findRepeatNumbers(self, nums):
        for i in range(len(nums)):
            if nums[i] == i: continue
            if nums[i] == nums[nums[i]]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

