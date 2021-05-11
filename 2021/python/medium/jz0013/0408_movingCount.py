class Solution:
    # BFS, time: MN
    # 虽然可以走上下左右四个方向，但其实从起点出发，只需要向右和向下，即可覆盖所有格子
    # 坐标的数位相加时，满足公式：s(i+1) = si + 1 if (i+1) % 10 else si - 8, 对于j同理可得
    # 符合条件k >= si + sj, 并且没有越界的坐标均可以
    def movingCount(self, m, n, k):
        queue, visited = [(0,0,0,0)], set()  # queue中元素(i, j, si, si)
        while queue:
            # 不需要用双端队列，不需要按顺序弹出对象，只要把所有对象处理过就行
            i, j, si, sj = queue.pop()
            # 向右和向下，越界只考虑m,n; 把越界，不符合规则，已经访问过的情况均舍弃
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))  # 向下
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))  # 向右
        return len(visited)


    # DFS, time: MN
    def movingCount(self, m, n, k):
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            down = dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)
            right = dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
            return 1 + down + right
        visited = set()
        return dfs(0,0,0,0)

            
