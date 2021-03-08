class Solution:
    # 双指钍， time: N**2
    def threeSum(self, nums):
        res, nums_len = [], len(nums)
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

    # 哈希表, N**2(第二层循环大大小于N, 因此此方法会比方法一快很多)  
    def threeSum(self, nums):
        res, nums_len = [], len(nums)
        if nums_len < 3: return res

        # 用字典记录数据的频次
        tmp_dic = collections.defaultdict(int)
        for n in nums:
            tmp_dic[n] += 1

        # 遍历tmp_dic.keys()
        # 以处注意，循环遍历用list, 查找用tmp_dic，字典中查找更快
        sort_list = sorted(tmp_dic) 
        for n in sort_list:
            if n == 0 and tmp_dic[n] > 2: res.append([0, 0, 0]) 
            elif n != 0 and tmp_dic[n] > 1:
                if -2 * n in tmp_dic: res.append([n, n, -2*n])
            if n < 0:
                n2_n3 = -n
                n3_min_idx = bisect.bisect_right(sort_list, n2_n3//2)
                for n3 in sort_list[n3_min_idx:]:
                    n2 = -n - n3
                    if n2 > n and n2 in tmp_dic: 
                        res.append([n, n2, n3])
        return res








