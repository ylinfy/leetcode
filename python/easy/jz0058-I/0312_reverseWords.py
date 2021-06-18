class Solution:
    # time: N (stirp: N, join: N, split: N, reverse: N)
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])

    # time: N
    def reverseWords(self, s):
        if not s: return ''
        s = s.strip()
        i = j = len(s) - 1
        res = [] 
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ': i -= 1
            j = i
        return ' '.join(res)

