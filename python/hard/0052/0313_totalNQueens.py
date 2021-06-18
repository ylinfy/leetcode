class Solution:
    # 回溯法，time: N**2
    # 将列(j)，撇(i+j)，捺(i-j), 用整型存储起来
    def totalNQueens(self, n):
        self.count = 0
        self.backtrack(n, 0, set(), set(), set())
        return self.count

    def backtrack(self, n, i, col, pie, na):
        if i == n:
            self.count += 1
            return
        for j in range(n):
            if j not in col and (i + j) not in pie and (i - j) not in na:
                col.add(j)
                pie.add(i + j)
                na.add(i - j)
                self.backtrack(n, i + 1, col, pie, na)
                col.remove(j)
                pie.remove(i + j)
                na.remove(i - j)

    # 位运算，回溯，time: N**2
    def totalNQueens(self, n):
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, col, pie, na):
        if row == n:
            self.count += 1
            return
        
        # 将可以放置皇后的位置置为1, & ((1 << n) - 1)只保留低n位，高位全置0
        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  # 获取最低位的1
            bits &= bits - 1  # 打掉最低位的1，表示在该位置放置皇后
            # row每增加一，即往下走一行，pie和na原有的所有位置再或上当前位置p,都要左，右移一
            self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)

