class Solution:
    # 回溯，time: N!
    def solveNQueens(self, n):
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.backtrack(n, 0, set(), set(), set())
        return self.res

    def backtrack(self, n, i, col, pie, na):
        if i == n:
            t_res = [''.join(x) for x in self.board]
            self.res.append(t_res)
            return 

        for j in range(n):
            if j not in col and (i + j) not in pie and (i - j) not in na:
                col.add(j)
                pie.add(i + j)
                na.add(i - j)
                self.board[i][j] = 'Q'
                self.backtrack(n, i + 1, col, pie, na)
                col.remove(j)
                pie.remove(i + j)
                na.remove(i - j)
                self.board[i][j] = '.'

    # 位运算 & DFS，time: N!
    def solveNQueens(self, n):
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.DFS(n, 0, 0, 0, 0)
        return self.res

    def DFS(self, n, i, col, pie, na):
        if i == n:
            t_res = [''.join(x) for x in self.board]
            self.res.append(t_res)
            return 

        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = dummy = bits & -bits
            bits &= bits - 1
            j = -1
            while dummy: dummy >>= 1; j += 1
            self.board[i][j] = 'Q'
            self.DFS(n, i + 1, col | p, (pie | p) << 1, (na | p) >> 1)
            self.board[i][j] = '.'
