class Solution:
    # 哈希，time: N, space: N
    def findRepeatNumber(self, nums):
        repeat = set()
        for n in nums:
            if n in repeat: return n
            repeat.add(n) 
    
    # n长的数组放0~n-1，指定位放指定数，不对的位置就交换
    # time: N, space: 1
    def findRepeatNumber(self, nums):
        for i in range(len(nums)):
            if nums[i] == i: continue
            if nums[nums[i]] == nums[i]: return nums[i] 
            # 此处交换nums[nums[i]]需要写在前面，否则先给nums[i]赋值，nums[nums[i]]对应的索引就变化了
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
