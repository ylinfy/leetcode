class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, sum = 0, float("-INF")
        for i, n in enumerate(nums):
            pre = max(pre + n, n)
            sum = max(sum, pre)
        return sum

