class Solution:
    # BFS, time: MN
    def movingCount(self, m, n, k):
        queue, visited = [(0, 0, 0, 0)], set() 
        while queue:
            i, j, si, sj = queue.pop()
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))  # 向下
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))  # 向右
        return len(visited)

    # DFS
    def movingCount(self, m, n, k):
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            res_down = dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)
            res_right = dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
            return 1 + res_down + res_right
        visited = set()
        return dfs(0, 0, 0, 0)
