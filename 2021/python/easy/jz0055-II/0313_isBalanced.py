class Solution:
    # 先序遍历，判断每一个节点的左，右子树高度差
    # time: N*logN (每层复杂度 * 层数复杂度)
    # 每层复杂度：计算左右子树深度, N
    # 层数复杂度：一层一层遍历, logN
    def isBalanced(self, root):
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) < 2 and \
        self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, node):
        if not node: return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1


    # 后序遍历，剪枝，存在子树的左右高度差大于1,直接返回
    # time: N
    def isBalanced(self, root):
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return left
        right = self.depth(root.right)
        if right == -1: return right
        return max(left, right) + 1 if abs(left - right) < 2 else -1


