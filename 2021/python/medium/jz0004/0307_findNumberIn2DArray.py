class Solution:
    # 利用特殊数组性质，快速迭代 time: M + N
    def findNumberIn2DArray(self, matrix, target):
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False

    # 二分查找 time: logK! + logA(n, K), K=min(M,N), n=max(M,N)
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        diag = min(m, n) 
        for i in range(diag):
            if self.binSearch(matrix, target, i, m, True) or \
            self.binSearch(matrix, target, i, n, False):
                return True
        return False

    def binSearch(self, matrix, target, start, end, isVetical):
        lo, hi = start, end - 1
        while lo <= hi:
            mid = lo + ((hi - lo + 1) >> 1)
            if isVetical:
                if matrix[mid][start] == target: return True
                if matrix[mid][start] < target: lo = mid + 1
                else: hi = mid - 1
            else:
                if matrix[start][mid] == target: return True
                if matrix[start][mid] < target: lo = mid + 1
                else: hi = mid - 1
        return False
    
    # 递归，分治，二分查找，time: nlogn
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        return self._recur(matrix, target, 0, 0, len(matrix[0]) - 1, len(matrix) - 1)

    def _recur(self, matrix, target, left, top, right, bottom):
        if left > right or top > bottom: return False
        if matrix[top][left] > target or matrix[bottom][right] < target: return False
        mid = left + ((right - left + 1) >> 1)

        row = top
        while row <= bottom and matrix[row][mid] <= target:
            if matrix[row][mid] == target: return True
            row += 1
        return self._recur(matrix, target, left, row, mid - 1, bottom) or \
        self._recur(matrix, target, mid + 1, top, right, row - 1)







