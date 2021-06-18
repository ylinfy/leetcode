class Solution:
    # 位运算，DFS  time: N!
    def solveNQueens(self, n):
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.DFS(n, 0, 0, 0, 0)
        return self.res

    def DFS(self, n, row, col, pie, na):
        if row == n:
            t_res = [''.join(x) for x in self.board]
            self.res.append(t_res)
            return

        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = t_pos = bits & -bits  # 取出最低位的1
            bits &= bits - 1  # 清零最低位的1,相当于在该位置放入皇后
            
            # row为横坐标，此处用于得到对应的列坐标
            col_pos = -1
            while t_pos:
                t_pos >>= 1 
                col_pos += 1

            self.board[row][col_pos] = 'Q'
            self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
            self.board[row][col_pos] = '.'
            
    # 回溯, time: N!
    def solveNQueens(self, n):
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.backtrack(n, 0, set(), set(), set(), board)
        return self.res

    def backtrack(self, n, i, col, pie, na, board):
        if i == n: 
            t_res = [''.join(x) for x in board]
            self.res.append(t_res)

        for j in range(n):
            if j not in col and (i + j) not in pie and (i - j) not in na:
                col.add(j)
                pie.add(i + j)
                na.add(i - j)
                board[i][j] = 'Q'
                self.backtrack(n, i + 1, col, pie, na, board)
                col.remove(j)
                pie.remove(i + j)
                na.remove(i - j)
                board[i][j] = '.'
                

