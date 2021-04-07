class Solution:
    # BFS, 遍历上下左右四点，舍弃越界及无效的点，最终visited里面存放的都是可以到达的位置
    # time: MN
    # 数位相加结果： s(i+1) = si + 1 if (i+1) % 10 else si - 8
    # 虽每次有四步走，但只需要从[0,0]出发走右下两步，即可覆盖全部位置
    def movingCount(self, m, n, k):
        queue, visited = [(0,0,0,0)], set()
        while queue:
            i, j, si, sj = queue.pop()
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))  # (i+1, j) 往下走
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))  # (i, j+1) 往右走
        return len(visited)


    # DFS, time: MN
    def movingCount(self, m, n, k):
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            ri = dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)  # (i+1, j) 往下走
            rj = dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)  # (i, j+1) 往右走
            return 1 + ri + rj
        visited = set()
        return dfs(0,0,0,0)
        
