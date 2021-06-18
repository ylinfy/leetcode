class Solution:
    def fib_numWays(self, n):
        a = b = 1  # n = 0 or 1的情况
        # 遍历从2到n, f(n) = f(n-1) + f(n-2), 因此最终返回b
        # 整个过程只与a,b初值和迭代次数有关，因此也可以是0遍历到n-1即for _ in range(n), 这样会多迭代一次，可通过返回a(上一次的)即可
        """
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
        """
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b % 1000000007
