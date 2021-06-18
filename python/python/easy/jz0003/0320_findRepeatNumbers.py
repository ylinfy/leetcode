class Solution:
    # 集合判重，time: N, space: N
    def findRepeatNumbers(self, nums):
        num_set = set()
        for n in nums:
            if n in num_set: return n
            num_set.add(n)

    # 组内交换，time: N, space: 1
    def findRepeatNumbers(self, nums):
        for i in range(len(nums)):
            if nums[i] == i: continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

            
