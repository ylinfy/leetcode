class Solution:
    # 二分查找，time: logk! + logA(n,k), k=min(M,N), n=max(M,N)
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        dia = min(m, n)
        for i in range(dia):
            if self.binSearch(matrix, target, i, m, True) or self.binSearch(matrix, target, i, n, False):
                return True
        return False

    def binSearch(self, matrix, target, start, end, isVetical):
        lo, hi = start, end - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            # 竖直方向
            if isVetical:
                if matrix[mid][start] == target: return True
                if matrix[mid][start] < target: lo = mid + 1
                else: hi = mid - 1
            # 水平方向
            else:
                if matrix[start][mid] == target: return True
                if matrix[start][mid] < target: lo = mid + 1
                else: hi = mid - 1
        return False
            
