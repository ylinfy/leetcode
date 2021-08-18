class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 前两行都是1，不用修改, 从第三行开始: range(2, numRows)
        # 每一行首尾元素为1，不用处理: range(1, len(dp[i]) - 1)
        dp = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp

