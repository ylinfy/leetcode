class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} 
        for i, n in enumerate(nums):
            if target - n in dic:
                return [dic[target - n], i]
            dic[n] = i
        return []
