class Solution:
    # 归并排序，在回溯阶段，判断逆序对个数量
    # time: N * logN
    def reversePairs(self, nums):
        if len(nums) < 2: return 0
        self.count = 0
        self.mergeSort(nums, 0, len(nums)-1)
        return self.count

    def mergeSort(self, nums, left, right):
        if left >= right: return
        mid = left + ((right - left) >> 1)
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        # 用于记录排好序的数组片段，最后再赋值给nums对应的片段, 即nums对应片段已经排好序列
        temp = []  
        # 归并排序，并的时候，遍历左右两子数组，因此需要使用i,j来记录左，右子数组的开始索引并遍历
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] > nums[j]:  # 左右子数组均已排好序，nums[i] > nums[j]即逆序对为mid - i + 1
                self.count += mid -i + 1
                temp.append(nums[j])
                j += 1
            else:
                temp.append(nums[i])
                i += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left:right+1] = temp

