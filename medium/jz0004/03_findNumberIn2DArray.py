class Solution:
    # recursion, time: n*logn ((2**logn)*logn = n*logn) --> ？不太确定
    def findNumberIn2DArray(self, matrix, target):
        if not matrix: return False
        return self._recursion(matrix, target, 0, 0, len(matrix[0]) - 1, len(matrix) - 1)

    def _recursion(self, matrix, target, left, top, right, bottom):
        if left > right or top > bottom: return False
        if matrix[top][left] > target or matrix[bottom][right] < target: return False
        mid = left + ((right - left) >> 1)

        # 1. 在竖直方向使用二分查找
        lo, hi = top, bottom
        while lo <= hi:
            r_mid = lo + ((hi - lo + 1) >> 1)
            if matrix[r_mid][mid] == target: return True
            if matrix[r_mid][mid] > target: hi = r_mid - 1
            else: lo = r_mid + 1
        # 用二分查找在竖直方向找到与target最接近但大于target的值, 所在的行
        row = r_mid if matrix[r_mid][mid] > target else r_mid + 1

        """
        # 2. 逐行查找，限制条件<=target
        row = top
        while row <= bottom and matrix[row][mid] <= target:
            if matrix[row][mid] == target: return True 
            row += 1
        """

        return self._recursion(matrix, target, left, row, mid - 1, bottom) or \
        self._recursion(matrix, target, mid + 1, top, right, row - 1)

s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(s.findNumberIn2DArray(matrix, 5))
        
            

