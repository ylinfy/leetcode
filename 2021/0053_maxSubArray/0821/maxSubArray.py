class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, res = 0, float("-INF")
        for i, n in enumerate(nums):
            pre = max(pre + n, n)
            res = max(pre, res)
        return res
