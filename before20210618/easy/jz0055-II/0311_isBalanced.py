class Solution:
    # 后序遍历，剪枝，time: N
    # 从底至顶返回子树深度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回
    def isBalanced(self, root):
        return self._recur(root) != -1

    def _recur(self, root):
        if not root: return 0
        left = self._recur(root.left)
        if left == -1: return -1
        right = self._recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1

    # 先序遍历, 先判断根节点左，右子树深度
    # time: N*logN (每层执行复杂度 × 层数复杂度)
    def isBalanced(self, root):  # logN, 有多少层
        if not root: return True
        return abs(self._depth(root.left) - self._depth(root.right)) <= 1 \
        and self.isBalanced(root.left) and self.isBalanced(root.right)

    def _depth(self, node):  # N, 遍历所有节点
        if not node: return 0
        return max(self._depth(node.left), self._depth(node.right)) + 1

