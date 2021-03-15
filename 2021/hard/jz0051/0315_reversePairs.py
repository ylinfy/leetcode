class Solution:
    # 归并排序，并的时候计算逆序对数，time: N*logN
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
        tmp = []
        i, j, k = left, mid + 1, 0
        while i <= mid and j <= right:
            if nums[j] < nums[i]:
                self.count += mid - i + 1
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        while i <= mid:
            tmp.append(nums[i])
            i += 1
        while j <= right:
            tmp.append(nums[j])
            j += 1
        nums[left:right+1] = tmp     

            
            

