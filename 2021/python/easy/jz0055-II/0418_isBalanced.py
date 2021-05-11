class Solution:
    # 先序遍历， 遍历每一个节，判断左右子树高度差
    # time: N * logN
    def isBalanced(self, root):
        if not root: return True
        self.mem = defaultdict(int)
        return abs(self.depth_(root.left) - self.depth_(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth_(self, node):
        if not node: return 0
        if node in self.mem: return self.mem[node]
        depth = 1 + max(self.depth_(node.left), self.depth_(node.right))
        return depth


    # 后序遍历，把所有子树的平衡性判断一遍历, 均为平衡，则最后判断root是否是平衡树
    # time: N
    def isBalanced(self, root):
        if not root: return True
        return self.judge_(root) != -1

    def judge_(self, node):
        if not node: return 0
        left = self.judge_(node.left)
        if left == -1: return -1
        right = self.judge_(node.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

