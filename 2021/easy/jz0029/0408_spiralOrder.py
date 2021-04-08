class Solution:
    # python zip
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


    # 逻辑迭代, 每次按顺时针方向迭代
    def spiralOrder(self, matrix):
        if not matrix: return []
        l, t, r, b, res = 0, 0, len(matrix[0]) - 1, len(matrix) - 1, []
        while True:  # 此处需要用True代替r >= l and b >= t, 因ltrb在每次循环中间有作自加自减
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1  # 第一行迭代完，更新top
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1  # 最右列迭代完，更新right
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1  # 最底行迭代完，更新bottom
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1  # 最左列迭代完，更新left
            if l > r: break
        return res


    # 逻辑迭代2，整个迭代完一次，才更新l,t,r,b, 相当于从外向里收缩
    def spiralOrder(self, matrix):
        if not matrix: return []
        l, t, r, b, res = 0, 0, len(matrix[0]) - 1, len(matrix) - 1, []
        while l < r and t < b:
            i, j = t, l  # 每次迭代前初始化i, j
            # (C++用此方法时，每行或每列迭代时，可不包含末尾元素, 使用++i/++j, 如第一行处理完后，不包含末尾，但j==r, 在处理右列时，将[t][r]右列起点加入)
            for j in range(l, r + 1): res.append(matrix[i][j])   # 已处理过[t][r], 此时j==r, 下次迭代右列时可从t+1开始
            for i in range(t + 1, b + 1): res.append(matrix[i][j])  # 已处理过[b][r], 此时i==b, 下次迭代底行时可从r-1开始 
            for j in range(r - 1, l - 1, -1): res.append(matrix[i][j])  # 已处理过[b][l], 此时j==l, 下次迭代左列时可从b-1开始
            for i in range(b - 1, t, -1): res.append(matrix[i][j])  # 完成一次迭代
            # 向中间内缩
            l, t, r, b = l + 1, t + 1, r - 1, b - 1
        # 最后可能还剩下一行或一列
        if l == r:  # 还剩下一列
            for i in range(t, b + 1): res.append(matrix[i][l])
        elif t == b: # 使用elif防止只剩下中间一点时，重复添加该点
            for j in range(l, r + 1): res.append(matrix[t][j])
        return res


