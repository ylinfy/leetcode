class Solution:
    def reversePairs(self, nums):
        if len(nums) < 2: return 0
        self.count = 0
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.count

    def merge_sort(self, nums, l, r):
        if l >= r: return
        m = l + ((r - l) >> 1)
        self.merge_sort(nums, l, m)
        self.merge_sort(nums, m + 1, r)
        self.merge(nums, l, m, r)

    def merge(self, nums, l, m, r):
        temp = []
        i, j = l, m + 1
        while i <= m and j <= r:
            if nums[i] > nums[j]:
                temp.append(nums[j])
                self.count += m - i + 1
                j += 1
            else:
                temp.append(nums[i])
                i += 1
        while i <= m: 
            temp.append(nums[i])
            i += 1
        while j <= r:
            temp.append(nums[j])
            j += 1
        nums[l:r+1] = temp
                

