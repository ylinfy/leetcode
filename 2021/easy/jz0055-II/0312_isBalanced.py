class Solution:
    def isBalanced(self, root):
        return self.recur(root) != -1

    def recur(self, node):
        if not node: return 0
        left = self.recur(node.left)
        if left == -1: return -1
        right = self.recur(node.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1


    def isBalanced(self, root):
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) < 2 \
        and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, node):
        if not node: return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1
        

