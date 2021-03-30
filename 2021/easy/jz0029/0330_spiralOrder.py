class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
            
    
    def spiralOrder(self, matrix):
        if not matrix: return []
        l, t, r, b, res = 0, 0, len(matrix[0]) - 1, len(matrix) - 1, []
        while True:
            # 遍历顶行
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1
            if t > b: break
            # 遍历右列
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1
            if l > r: break
            # 遍历底行
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1
            if t > b: break
            # 遍历左列
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res


    def spiralOrder(self, matrix):
        if not matrix: return []
        l, t, r, b, res = 0, 0, len(matrix[0]) - 1, len(matrix) - 1, []
        while r > l and b > t:
            i, j = t, l
            for j in range(l, r):
                res.append(matrix[i][j])
            j += 1
            for i in range(t, b):
                res.append(matrix[i][j])
            i += 1
            for j in range(r, l, -1):
                res.append(matrix[i][j])
            j -= 1
            for i in range(b, t, -1):
                res.append(matrix[i][j])
            i -= 1  # 此行可删除

            # 一圈跑完，向内缩1
            l, t, r, b = l + 1, t + 1, r - 1, b - 1
        if r == l:
            for i in range(t, b + 1): res.append(matrix[i][l])
        elif t == b:
            for i in range(l, r + 1): res.append(matrix[t][i])
        return res
            
                


