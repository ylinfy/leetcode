class Solution:
    # 双指针，time: N**2
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        res, n = [], len(nums)
        for i in range(n - 2):
            if i == 0 and nums[i] > 0: return []
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0: k -= 1
                elif s < 0: j += 1
                else: 
                    res.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1
        return res


    # 计算，并根据逻辑判断，time: N**2
    def threeSum(self, nums):
        if len(nums) < 3: return []
        dic, res = defaultdict(int), []
        for n in nums: dic[n] += 1
        tmp_list = sorted(dic)
        for x in tmp_list:
            if x == 0 and dic[x] > 2: res.append([0, 0, 0])
            elif x != 0 and dic[x] > 1:
                if -2 * x in dic: res.append([x, x, -2*x])
            # 当元素数量为1时，且元素小于0(因排好序的，如果>=0, 即不存在三数和为0)
            if x < 0:
                y_z = -x
                z_min_idx = bisect.bisect_right(tmp_list, y_z // 2)
                for z in tmp_list[z_min_idx:]:
                    y = -x - z
                    if y > x and y in dic: res.append([x, y, z])
        return res
                
    
    # 通用，多数之和，time: N**2
    def threeSum(self, nums):
        self.res = set()
        N, target = 3, 0
        nums.sort()
        self.find_sum(nums, 0, N, target, [])
        return list(self.res)

    def find_sum(self, nums, start, N, target, data):
        if N < 2 or len(nums) < N: return
        if N == 2:
            tmp = set()
            for a in nums[start:]:
                if target - a in tmp:
                    self.res.add(tuple(data + [target - a, a]))
                tmp.add(a)
            return
        for i in range(start, len(nums)):
            if nums[i] * N > target or nums[-1] * N < target: return
            if i > start and nums[i] == nums[i-1]: continue
            self.find_sum(nums, i + 1, N - 1, target - nums[i], data + [nums[i]])

            
        
