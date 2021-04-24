class Solution:
    def levelOrder(self, root):
        if not root: return []
        deq, res = deque([root]), []
        while deq:
            node = deq.popleft()
            res.append(node.val)
            if node.left: deq.append(node.left)
            if node.right: deq.append(node.right)
        return res

    def levelOrder(self, root):
        dic, res = defaultdict(list), []
        self.dfs(root, 0, dic)
        for v in dic.values(): res += v
        return res

    def dfs(self, node, level, dic):
        if not node: return
        dic[level] += [node.val]
        if node.left: self.dfs(node.left, level + 1, dic)
        if node.right: self.dfs(node.right, level + 1, dic)
