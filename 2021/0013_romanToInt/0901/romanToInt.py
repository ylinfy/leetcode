class Solution:
    def romanToInt(self, s: str) -> int:
        VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = pre = 0
        for i in range(len(s) - 1, -1, -1):
            cur = VALUES[s[i]]
            ret += -cur if cur < pre else cur
            pre = cur
        return ret
