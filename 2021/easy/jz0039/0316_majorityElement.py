class Solution:
    # 找大于数组长度一半的数
    # 哈希统计，找到即返回，time: N
    def majorityElement(self, nums):
        dic = collections.defaultdict(int) 
        for n in nums:
            dic[n] += 1
            if dic[n] > len(nums) // 2:
                return n
            

    # 排序取中，time: N*logN
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


    # 摩尔投票，time: N
    # 由于众数x数量大于数组长度的一半，最后投出的数一定会是众数
    def majorityElement(self, nums):
        vote = 0
        for n in nums:
            if vote == 0: x = n
            vote += 1 if n == x else -1
        return x

