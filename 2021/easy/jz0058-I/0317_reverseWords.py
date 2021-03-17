class Solution:
    # 分割，倒序，time: N (split:N, strip:N, join:N, reverse:N)
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])


    # 双指针，从后往前遍历，time: N
    def reverseWords(self, s):
        if not s: return ''
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            # 找到倒数第一个空格符
            while i >= 0 and s[i] != ' ': i -= 1
            # 找到后，[i+1:j+1]即为倒数第一个word
            res.append(s[i+1:j+1])
            # 跳过连续空格，找到下一个word的尾部
            while s[i] == ' ': i -= 1
            j = i  # 将i赋值给j, 循环操作
        return ' '.join(res)

            
