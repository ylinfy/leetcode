class Solution:
    def singleNumbers(self, nums):
        a = b = c = 0
        for x in nums: c ^= x
        bit = c & -c
        for x in nums:
            if x & bit == 0: a ^= x
            else: b ^= x
        return [a, b]
