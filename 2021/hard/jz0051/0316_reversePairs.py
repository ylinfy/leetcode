class Solution:
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
        i, j, temp = left, mid + 1, []
        while i <= mid and j <= right:
            if nums[i] > nums[j]:
                temp.append(nums[j])
                j += 1
                self.count += mid - i + 1
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
            
                

