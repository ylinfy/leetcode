class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        def makeTree(left, right):
            if left > right: return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = makeTree(left, mid - 1)
            root.right = makeTree(mid + 1, right)
            return root
        return makeTree(0, len(nums) -1)
