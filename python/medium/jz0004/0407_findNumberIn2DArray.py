class Solution:
    # 利用该数据的特性，快速遍历
    # time: M + N
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        i, j = 0, len(matrix[0]) - 1
        while i <= len(matrix) - 1 and j >= 0:
            if matrix[i][j] > target: j -= 1
            elif matrix[i][j] < target: i += 1
            else: return True
        return False


    # 二分查找
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        tmp = min(len(matrix), len(matrix[0]))
        for i in range(tmp):
            if self.bin_search(matrix, i, target, True) or \
            self.bin_search(matrix, i, target, False): return True
        return False

    def bin_search(self, matrix, start, target, isVetical):
        lo, hi = start, len(matrix) - 1 if isVetical else len(matrix[0]) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1) 
            if isVetical:
                if matrix[mid][start] == target: return True
                if matrix[mid][start] > target: hi = mid - 1
                else: lo = mid + 1
            else:
                if matrix[start][mid] == target: return True
                if matrix[start][mid] > target: hi = mid - 1
                else: lo = mid + 1
        return False
            

    # 递归
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        return self.recur(matrix, target, 0, 0, len(matrix[0]) - 1, len(matrix) - 1)

    def recur(self, matrix, target, l, t, r, b):
        if l > r or t > b: return False
        if target > matrix[b][r] or target < matrix[t][l]: return False
        m = l + ((r - l) >> 1)
        row = t
        while row <= b and matrix[row][mid] <= target:
            if matrix[row][mid] == target: return True
            row += 1
        return self.recur(matrix, target, l, row, mid, b) or self.recur(matrix, target, mid + 1, t, r, row - 1)
