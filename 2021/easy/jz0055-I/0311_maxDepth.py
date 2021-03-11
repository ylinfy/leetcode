class Solution:
    # 层序遍历，直接使用列表实现, 也可使用deque实现
    # time: N
    def maxDepth(self, root):
        if not root: return 0
        queue, count = [root], 0
        while queue:
            count += 1
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
        return count

    # 后序遍历，左右根，得出左子树，右子树的深度，加取较大值+1
    # time: N
    def maxDepth(self, root):
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
