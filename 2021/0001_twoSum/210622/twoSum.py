class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        for i, n in enumerate(nums):
            if target - n in hashTable:
                return [hashTable[target - n], i]
            hashTable[n] = i
        return []
