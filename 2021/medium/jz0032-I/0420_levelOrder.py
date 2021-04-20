class Solution:
    # 层序遍历，BFS, time: N
    def levelOrder(self, root):
        if not root: return []
        queue, res = deque([root]), []
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res


    # DFS, 记录level, time: N
    def levelOrder(self, root):
        def dfs(node, level):
            if not node: return
            dic[level] += [node.val]
            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)
        dic, res = defaultdict(list), []
        dfs(root, 0)
        for v in dic.values(): res += v
        return res
            



