class Solution:
    # 调用库函数，一行代码
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])

    # 双指针，均从后面开始
    def reverseWords(self, s):
        if not s: return ''
        s = s.strip()  # 去除前后多余空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1  # 找空格 
            res.append(s[i+1:j+1])  
            while s[i] == ' ': i -= 1  # 跳过连续空格
            j = i  # 定位到下一个单词尾部
        return ' '.join(res)
