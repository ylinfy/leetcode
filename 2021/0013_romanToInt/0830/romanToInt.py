class Solution:
    def romanToInt(self, s: str) -> int:
        VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = 0
        for i in range(len(s) - 1):
            value = VALUES[s[i]]
            if value < VALUES[s[i+1]]:
                ret -= value
            else:
                ret += value
        return ret + VALUES[s[-1]]
            
