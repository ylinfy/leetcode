class Solution:
    # 斐波那契数列，time: N
    # dp[i] = dp[i-1] + dp[i-2]
    def fib(self, n):
        dp = [1] * 3
        for _ in range(2, n+1):
            dp[2] = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], dp[2]
        return dp[2] % 1000000007

    def fib(self, n):
        a = b = 1
        """
        # b: dp[i-1], a: dp[i-2]
        # 每一次更新b，即得到dp[i-1] + dp[i-2]
        for _ in range(2, n+1):
            b, a = a + b, b
        return b % 1000000007
        """
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
