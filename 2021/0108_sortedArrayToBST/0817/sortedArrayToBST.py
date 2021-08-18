class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        return self.makeTree(nums, 0, len(nums) - 1)

    def makeTree(self, nums, leftIndex, rightIndex):
        if leftIndex > rightIndex: return None
        midIndex = (leftIndex + rightIndex) // 2
        root = TreeNode(nums[midIndex])
        root.left = self.makeTree(nums, leftIndex, midIndex - 1)
        root.right = self.makeTree(nums, midIndex + 1, rightIndex)
        return root
