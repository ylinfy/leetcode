class Solutions:
    # time: N**2, 超出时间限制
    def reversePairs(self, nums):
        if len(nums) < 2: return 0
        nums_len, count = len(nums), 0
        for i in range(nums_len - 1):
            for j in range(i + 1, nums_len):
                if nums[j] > nums[i]:
                    count += 1
        return count

    # 归并排序，time: N*logN
    def reversePairs(self, nums):
        if len(nums) < 2: return 0
        self.count = 0
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.count

    def mergeSort(self, nums, left, right):
        if left >= right: return
        mid = left + ((right - left) >> 1)
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
                self.count += (mid - i + 1)
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left:right+1] = temp

    # 离散化树状数组，time: N*logN
    def reversePairs(self, nums):
