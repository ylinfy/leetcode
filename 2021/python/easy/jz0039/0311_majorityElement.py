class Solution:
    # 哈希， time: N
    def majorityElement(self, nums):
        dic = collections.defaultdict(int)
        for n in nums:
            dic[n] += 1
            if dic[n] > len(nums)//2
                return n
    
    # 中位数，timsort time: N
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    # 摩尔投票，time: N
    def majorityElement(self, nums):
        vote = count = 0
        for n in nums:
            if vote == 0: x = n
            vote += 1 if n == x else -1
        return x
            
        
