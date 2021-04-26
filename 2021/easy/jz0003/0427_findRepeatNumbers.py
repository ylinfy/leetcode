class Solution:
    def findRepeatNumbers(self, nums):
        for i in range(len(nums)):
            j = nums[i]
            if j == i: continue
            if nums[i] == nums[j]: return nums[i]
            nums[i], nums[j] = nums[j], nums[j]

