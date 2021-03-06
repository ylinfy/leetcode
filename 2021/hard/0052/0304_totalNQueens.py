class Solution:
    # 回溯 time: N!
    def totalNQueens(self, n):
        if n < 1: return 0
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

    # 位运算 & DFS, time: N!
    def totalNQueens(self, n):
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, col, pie, na):
        if row == n:
            self.count += 1
            return

        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits
            bits &= bits - 1
            self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
