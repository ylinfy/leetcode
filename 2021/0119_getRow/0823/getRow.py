class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        # 从第2行开始，第0，1行均是1
        for i in range(2, rowIndex + 1):
            # 首尾元素不用计算，均为1, 其中第i行有(i + 1)个元素
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
        return res
