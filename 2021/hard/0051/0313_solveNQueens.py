class Solution:
    # 回溯，time: N**2
    # 将列(j)，撇(i+j)，捺(i-j), 用整型存储起来
    def solveNQueens(self, n):
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.backtrack(n, 0, set(), set(), set(), board)
        return self.res

    def backtrack(self, n, i, col, pie, na, board):
        if i == n:
            one_res = [''.join(x) for x in board]
            self.res.append(one_res)
            return

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

    # 位运算 & 回溯, time: N**2
    def solveNQueens(self, n):
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.DFS(n, 0, 0, 0, 0, board)
        return self.res

    def DFS(self, n, row, col, pie, na, board):
        if row == n:
            one_res = [''.join(x) for x in board]
            self.res.append(one_res)
            return

        # 将可以放置皇后的位置置为1, & ((1 << n) - 1)只保留低n位，高位全置0
        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  # 获取最低位的1
            bits &= bits - 1  # 打掉最低位的1，表示在该位置放置皇后
            dummy, col_pos = p, -1
            while dummy:
                dummy >>= 1
                col_pos += 1
            board[row][col_pos] = 'Q'
            self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1, board)
            board[row][col_pos] = '.'

