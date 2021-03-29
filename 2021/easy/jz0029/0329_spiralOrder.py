class Solution:
    # python特性，使用zip，面试中忌用
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


    # 定义矩阵上下左右边界，按照逆时针方式逐步处理
    # time: N (matrix每个元素都遍历一次)
    def spiralOrder(self, matrix):
        if not matrix: return []
        # 初始化左上右下边界
        l, t, r, b, res = 0, 0, len(matrix[0]) - 1, len(matrix) -1, []
        while True:
            # 包含最后一个元素
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1  # 遍历完顶行，top边界t自加1, 如果超出bottom边界b，即遍历完
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1  # 遍历完右列，right边界r自减1, 如果超出left边界l，即遍历完
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1  # 遍历完底行，bottom边界b自减1, 如果超出top边界t，即遍历完
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1  # 遍历完左列，left边界l自加1, 如果超出right边界r，即遍历完
            if l > r: break
        return res


    # 一圈一圈处理，处理完一圈，l,r,t,b全部向里缩小
    # time: N
    def spiralOrder(self, matrix):
        if not matrix: return []
        l, t, r, b, res = 0, 0, len(matrix[0]) - 1, len(matrix) -1, []
        while r > l and b > t:
            i, j = t, l
            # 不带最后一个元素, 转向时该最后一个元素作为下一次的首元素
            for j in range(l, r): res.append(matrix[i][j])
            j += 1  # python不能像c++中使用++j,只能执行完for时，再自加1, 使j==r, 其他类似，最后for循环后的i -= 1可删除
            for i in range(t, b): res.append(matrix[i][j])
            i += 1
            for j in range(r, l, -1): res.append(matrix[i][j])
            j -= 1
            for i in range(b, t, -1): res.append(matrix[i][j])
            i -= 1  # 可删除
            l, t, r, b = l + 1, t + 1, r - 1, b - 1
        # 最后还剩下一行或者一列元素
        if r == l:
            for i in range(t, b + 1): res.append(matrix[i][r])
        elif t == b:
            for j in range(l, r + 1): res.append(matrix[t][j])
        return res        


    

            

        

        
