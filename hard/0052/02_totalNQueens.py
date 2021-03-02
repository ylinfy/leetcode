class Solution:
    # 位运算，time: N**2
    def totalNQueens(self, n):
        if n < 1: return 0
        self.count = 0
        self.DFS(n,0,0,0,0)
        return self.count

    def DFS(self, n, row, col, pie, na):
        if row == n:
            self.count += 1
            return

        # 将所有可以放置皇后的位置置为1，&((1 << n) - 1)只保留低位的n位
        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  # 取最低位的1，从最低位开始放置皇后
            bits &= (bits - 1)  # 清零最低位的1， 表示此处已放置皇后
            self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
