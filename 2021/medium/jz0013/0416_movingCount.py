class Solution:
    # 只需要向下或向右，即可走遍所有格子，并判断哪些格子是能visited
    # 坐标数位之和计算公式：s(i+1) = si + 1 if (i + 1) % 10 else si - 8
    # 如i = 19, si = 1 + 9 = 10, s(i+1) = si - 8 = 2 (20, 2 + 0)
    # BFS, 将能访问到的不重复的全加入到visited中，最终求visited的长度
    # time: N
    def movingCount(self, m, n, k):
        visited, queue = set(), [(0,0,0,0)]
        while queue:
            i, j, si, sj = queue.pop()
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))  # 向下
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))  # 向右
        return len(visited)


    # DFS, 一直向下或者一直向右，直到撞到边界，再向右或者向左一步，每遍历一步，count加1，最终返回count
    def movingCount(self, m, n, k):
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            res_down = dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)  # 向下
            res_right = dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)  # 向右
            return 1 + res_down + res_right
        visited = set()
        return dfs(0,0,0,0)
