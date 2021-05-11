class Solution:
    # 回溯加集合判重, time: N!
    def solveNQueens(self, n):
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.backtrack(n, 0, set(), set(), set())
        return self.res

    def backtrack(self, n, i, col, pie, na):
        if i == n:
            one_res = [''.join(x) for x in self.board]
            self.res.append(one_res)
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

    
    # 回溯加位运算，time: N!
    def solveNQueens(self, n):
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.backtrack(n, 0, 0, 0, 0)
        return self.res

    def backtrack(self, n, row, col, pie, na):
        if row == n:
            one_res = [''.join(x) for x in self.board]
            self.res.append(one_res)
            return 

        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  # 获取最低位的1
            bits &= bits - 1  # 打掉最低位的1，表示在该位置放置皇后
            cid = bin(p - 1).count('1')
            self.board[row][cid] = 'Q'
            self.backtrack(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
            self.board[row][cid] = '.'
            
