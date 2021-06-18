class Solution:
    def levelOrder(self, root):
        queue, res = deque([root]), []
        if not root: return res
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res

    def levelOrder(self, root):
        if not root: return []
        def dfs(node, level):
            if not node: return
            dic[level] += [node.val]
            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)
        dic, res = defaultdict(list), []
        dfs(root, 0)
        for v in dic.values(): res += v
        return res

