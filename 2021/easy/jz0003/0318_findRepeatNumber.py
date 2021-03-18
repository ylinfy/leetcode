class Solution:
    # 哈希，time: N
    def findRepeatNumber(self, nums):
        dic = collections.defaultdict(int)
        for n in nums:
            dic[n] += 1
            if dic[n] > 1: return n
        return -1


    # 组内交换，time: N
    def findRepeatNumber(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
        

        
