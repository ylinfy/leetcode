class Solution:
    # time: M + N, 根据数组特性，快速迭代
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target: j -= 1
            elif matrix[i][j] < target: i += 1
            else: return True
        return False

