class Solution:
    # 解码，将只包含数字的字符串s解码成大写字母字符串，规则'1' ~ '26' --> 'A' ~ 'Z', 问有多少种解码方法
    # DP, dp[i]: 以i为结尾的字符串s[:i]的解码种数
    # 字符串出现前导0直接返回0，无法解码
    # dp[i]: dp[i-1] + dp[i-2] if '11' <= s[i-1:i+1] <= '26'最后两个字符可以一个一个解码(种数：dp[i-1])也可以两个解码成一个字母(dp[i-2]), 类似于爬楼梯问题，最后两步可以分两步，也可以一步跨直接到达
    # dp[i]: 0 if s[i-1] not in '12' 相当于前导0了
    # dp[i]: dp[i-1] 其他情况,即s[i]只能单独解码的情况
    def numDecodings(self, s):
        if s.startswith('0'): return 0
        pre = cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] not in "12": return 0
                else: cur = pre
            elif '11' <= s[i-1:i+1] <= '26': cur += pre
            pre = tmp
        return cur


    # 可简化为有条件的爬楼梯问题，如下，cur = cur + pre是有条件的
    def numDecodings(self, s):
        if s.startswith('0'): return 0
        pre = cur = 1
        for i in range(1, len(s)):
            pre, cur = cur, pre * ("10" <= s[i-1:i+1] <= "26") + cur * (s[i] != "0")
        return cur

