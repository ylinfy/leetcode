class Solution:
    # 双指针，time: N**2
    def threeSum(self, nums):
        res = []
        if len(nums) < 3: return res
        nums.sort()
        nums_len = len(nums)
        # 排序后，遍历首个值nums[i]，再用双指针找第二三个值nums[l], nums[r]
        for i in range(nums_len - 2):
            # 首值大于0，对于排好序的数组，不可能存在三数之和为0, 直接返回
            if nums[i] > 0: return res
            # 遍历过程中，如果有相同的值，说明前面已经计算过该值的所有组合了，直接continue
            if i > 0 and nums[i] == nums[i-1]: continue

            # 双指针，找第二三个值
            l, r = i + 1, nums_len - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0: r -= 1
                elif s < 0: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 去除重复值，前面两个分支也可以加上
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
        return res


    # 哈希表，time: N**2
    def threeSum(self, nums):
        res = []
        if len(nums) < 3: return res
        dic = collections.defaultdict(int)
        
        # 记录所有数字出现的次数
        for n in nums:
            dic[n] += 1

        # 得到去重后的排序数组，遍历时用sorted_nums，查找时用dic
        sorted_nums = sorted(dic)
        for n in sorted_nums:
            # 如果存在数值0，则需要0出现的次数大于2，才能将[0,0,0]加入到结果中
            if n == 0 and dic[n] > 2:
                res.append([0,0,0])
            # 如果存在非零值，且出现的次数大于1，并且-2*n也在该字典中，可得到[n,n,-2*n]满足条件
            elif n != 0 and dic[n] > 1:
                if -2 * n in dic: res.append([n, n, -2 * n])
            # 假设n, n2, n3依次是按小到大，且满足条件的三个数，则n3在排序数组中存在最小索引值
            if n < 0:
                n2_n3 = -n
                n3_min_idx = bisect.bisect_right(sorted_nums, n2_n3 // 2)
                for n3 in sorted_nums[n3_min_idx:]:
                    n2 = -n - n3
                    if n < n2 and n2 in dic:
                        res.append([n, n2, n3])
        return res


    # 递归，剪枝，实现N数之和, time: N**2
    def threeSum(self, nums):
        # 定义set, 防止重复结果
        self.res = set()
        # 排序是后序剪枝的关键
        nums.sort()
        # params: nums, start index, N, target, mid data
        self._find_sum(nums, 0, 3, 0, [])
        return list(self.res)

    def _find_sum(self, nums, start, N, target, data):
        if len(nums) < N or N < 2: return 
        if N == 2:
            # 递归到N==2时，求出两数之和的情况
            t_res = set()
            for n in nums[start:len(nums)]:
                if target - n in t_res:
                    # 将两数之和的情况，加上中途的结果，组成一个完整的N数(nums中的N个索引，N数和为target)
                    self.res.add(tuple(data + [target - n, n]))
                t_res.add(n)
        else:
            for i in range(start, len(nums)):
                # 和双指针开始的遍历一样，对特殊情况进行剪枝
                # 最小的数 * N都大于target, 或者最大的数 * N都小于target，直接返回
                if nums[i] * N > target or nums[-1] * N < target: return
                # 从最小的数开始，后续有相同的数，前面已经处理过了，直接跳过
                if i > start and nums[i] == nums[i-1]: continue
                # 下探到下一层，索引i += 1, 另外N -= 1， target -= nums[i], data += [nums[i]]
                self._find_sum(nums, i + 1, N - 1, target - nums[i], data + [nums[i]])

