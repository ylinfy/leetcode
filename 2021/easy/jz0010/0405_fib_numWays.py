class Solution:
    def fib(self, n):
        a = b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b % 1000000007
