class Solution:
    # 找特殊众数：数量大于列表长度的一半
    # 哈希统计法，time: N
    def majorityElement(self, nums):
        nums_len = len(nums)
        dic = collections.defaultdict(int)
        for n in nums: 
            dic[n] += 1
            if dic[n] > nums_len // 2:
                return n
                
    # 数组排序法, time: n ~ nlogn
    def majorityElement(self, nums):
        nums_len = len(nums)
        nums.sort()
        return nums[nums_len//2]

    # 摩尔投票法，time: n
    def majorityElement(self, nums):
        vote = count = 0
        for num in nums:
            if vote == 0: x = num
            vote += 1 if num == x else -1
        # 若考虑nums中不存在众数，刚需要验证
        for num in nums:
            if num == x: count += 1
        return x if count > len(nums)//2 else 0  # 当无众数时返回0
            
