class Solution:
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root):
        if not root: return 0
        level, queue = 0, deque([root])
        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
        return level

    def __init__(self):
        self.mem = defaultdict(int)

    def maxDepth(self, root):
        if not root: return 0
        if root in self.mem: return self.mem[root]
        depth = 1 + max(maxDepth(root.left), maxDepth(root.right))
        self.mem[root] = depth
        return depth

