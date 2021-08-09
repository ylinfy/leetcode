class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # use lib method
        # bisect.bisect_left(nums, target)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l
