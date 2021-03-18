class Solution:
    # time: N, space: 1
    def singleNumbers(self, nums):
        xor = functools.reduce(lambda x, y: x ^ y, nums)
        bit = xor & -xor
        a = b = 0
        for n in nums:
            if n & bit == 0: a ^= n
            else: b ^= n
        return [a, b]
