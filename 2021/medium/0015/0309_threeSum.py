class Solution:
    # 双指针，time: N**2
    def threeSum(self, nums):
        nums_len, res = len(nums), []
        if nums_len < 3: return res
        nums.sort()
        for i in range(nums_len - 2):
            if nums[i] > 0: return res
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, nums_len - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0: r -= 1
                elif s < 0: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
        return res


    # 哈希，time: N**2
    def threeSum(self, nums):
        nums_len, res = len(nums), []
        if nums_len < 3: return res
        
        # 统计各数值个数
        tmp_dic = collections.defaultdict(int)
        for n in nums: tmp_dic[n] += 1
        
        # nums去重后，排序
        sort_set_nums = sorted(tmp_dic) 
        for n in sort_set_nums:
            if n == 0 and tmp_dic[n] > 2: res.append([0, 0, 0])
            elif n != 0 and tmp_dic[n] > 1: 
                if -2 * n in tmp_dic: res.append([n, n, -2 * n])
            # n, n2, n3不相同，升序，所以n3有取值范围sort_set_nums[n3_min_idx:]
            if n < 0:
                n23 = -n
                n3_min_idx = bisect.bisect_right(sort_set_nums, n23//2)
                for n3 in sort_set_nums[n3_min_idx:]:
                    n2 = n23 - n3
                    if n2 > n and n2 in tmp_dic:
                        res.append([n, n2, n3])
        return res
                

    # 递归，用于多数之和, time: N**2
    def threeSum(self, nums):
        N, target = 3, 0
        if len(nums) < 2 or len(nums) < N: return []
        # 一定要记得排序
        nums.sort() 
        self.res = set()
        self._findSum(nums, 0, N, target, [])
        return list(self.res)

    def _findSum(self, nums, start, N, target, data):
        if N == 2:
            tmp_set = set()
            for i in range(start, len(nums)):
                if target - nums[i] in tmp_set:
                    self.res.add(tuple(data + [target - nums[i], nums[i]]))
                tmp_set.add(nums[i])
            return
        for j in range(start, len(nums)):
            # 剪枝1，最小数的N倍比target大，最大数的N倍比target小
            if nums[j] * N > target or nums[-1] * N < target: return
            # 剪枝2，从start开始，前面有遍历过的数值已经处理了所有情况
            if j > start and nums[j] == nums[j-1]: continue
            self._findSum(nums, j + 1, N - 1, target - nums[j], data + [nums[j]])


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(nums)
print(s.threeSum(nums))













                    

            
        

