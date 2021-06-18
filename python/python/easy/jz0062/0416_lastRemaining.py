class Solution:
    def lastRemaining(self, n, m):
        idx = 0
        for i in range(2, n + 1):
            idx = (idx + m) % i
        return idx
