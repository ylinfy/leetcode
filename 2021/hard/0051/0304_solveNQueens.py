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
