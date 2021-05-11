class Solution:
    # 后序遍历，剪枝，time: N (每个节点都遍历一遍)
    def isBalanced(self, root):
        if not root: return True
        return self._recur(root) != -1

    def _recur(self, node):
        # 当前节点为空，高度为0
        if not node: return 0

        # DFS, 遍历左子树所有子树情况，找到最左边的最小子树，判断其左，右子树的高度(左子树高度0), 并返回该子树高度或者-1
        left = self._recur(node.left)
        # 左子树下，任何一子树返回结果为-1, 即子树的左右子树高度差大于1，就提前结束，直接返回-1, 一直返回给主函数
        if left == -1: return -1

        # DFS, 遍历右子树所有子树情况
        right = self._recur(node.right)
        # 右子树下，任何一子树返回结果为-1, 即子树的左右子树高度差大于1，就提前结束，直接返回-1, 一直返回给主函数
        if right == -1: return -1

        # max(left, right) + 1用于求该子树的高度，如果左右子树的高度差大于1，直接返回-1
        return max(left, right) + 1 if abs(left - right) < 2 else -1


    # 先序遍历，遍历每一个节点，判断左右子树高度差
    # time: N * lonN (节点数 * 每个节点高度复杂度)
    # 遍历每个节点：N
    # 计算高度：logN (root: N, root.left or right: n/2,., n/4....n/2**n) 相当于二分查找时间，即logN
    def isBalanced(self, root):
        if not root: return True
        return abs(self._depth(root.left) - self._depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def _depth(self, node):
        if not node: return 0
        return max(self._depth(node.left), self._depth(node.right)) + 1


    # 思考，有没有可能把计算过的高度存储起来
    # 先序遍历，存储所有高度的情况
    def __init__(self):
        self.mem = collections.default(int)

    def isBalanced(self, root):
        if not root: return True
        return abs(self._depth(root.left) - self._depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def _depth(self, node):
        if node in self.mem: return self.mem[node]
        if not node: return 0
        depth = max(self._depth(node.left), self._depth(node.right)) + 1
        self.mem[node] = depth
        return depth

