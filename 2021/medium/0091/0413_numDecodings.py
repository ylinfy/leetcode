class Solution:
    def numDecodings(self, s):
        if s.startswith('0'): return 0
        pre = cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] in '12': cur = pre
                else: return 0
            elif '11' <= s[i-1:i+1] <= '26':
                cur += pre
            pre = tmp
        return cur

    def numDecodings(self, s):
        if s.startswith('0'): return 0
        pre = cur = 1
        for i in range(1, len(s)):
            pre, cur = cur, pre * ('10' <= s[i-1:i+1] <= '26') + cur * (s[i] > '0')
        return cur
