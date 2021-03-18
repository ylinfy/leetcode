class Solution:
    # 层序遍历，层数即高度
    # time: N
    def maxDepth(self, root):
        if not root: return 0
        queue, count = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            count += 1
        return count

    
    # 递归，高度是max(high(左子树), high(右子树)) + 1
    def maxDepth(self, root):
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


    # 递归，动态内存，存储已经算过的高度
    def __init__(self):
        self.height = collections.defaultdict(int)

    def maxDepth(self, root):
        if root in self.height:
            return self.height[root]
        if not root: return 0
        depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        self.height[root] = depth
        return depth
