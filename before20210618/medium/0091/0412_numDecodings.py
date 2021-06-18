class Solution:
    # DP, 只与dp[i-1]和dp[i-2]有关，使用pre, cur代替
    # DP状态: s中以i索引结尾的左子字符串有多少种解码方法
    def numDecodings(self, s):
        if s[0] == '0': return 0  # 无效0
        n = len(s)
        pre = cur = 1  # 必须初始化1
        for i in range(1, len(s)):
            tmp = cur  # 记录cur，用于最后赋值给pre
            if s[i] == '0':
                # 只有'10'和'20'的组合，因此直接cur = pre (dp[i] = dp[i-2])
                if s[i-1] in '12': cur = pre
                else: return 0  # 触发无效0, 存在无效0, 无法解码
            # 存在两种情况，当前cur = pre + cur (dp[i] = dp[i-1] + dp[i-2])
            # 相当于爬楼梯问题，最后剩一步还是两步（最后留一个字符还是两个字符）
            elif '11' <= s[i-1:i+1] <= '26':  
                cur += pre
            # 其他情况: pre, cur = cur, cur (dp[i], dp[i-1] = dp[i-1], dp[i-1])
            pre = tmp
        return cur


    # 其实就是相当于爬楼梯问题的变体，或者说是斐波拉契数列变体
    # 即f(n) = f(n-1) + f(n-2)是有条件的（存在f(n) = f(n-1) or f(n-2)的特殊情况)
    # 下面就是典型的斐波拉契数列DP解法
    def numDecodings(self, s):
        pre = cur = 1
        for i in range(1, len(s)):
            pre, cur = cur, pre + cur
        return cur
    # 本题使用斐波拉契变体解法
    def numDecodings(self, s):
        if s[0] == '0': return 0  # 无效0
        pre = cur = 1
        for i in range(1, len(s)):
            # s[i] == '0'时，dp[i] 就只与dp[i-2]有关
            # 当s[i-1:i+1]不在[10,26]范围时，dp[i]就只与dp[i-1]有关
            # 当两条件都不满足时，dp[i] = 0, 即最终pre = cur = 0
            pre, cur = cur, pre * (9 < int(s[i-1:i+1]) <= 26) + cur * (int(s[i]) > 0)
        return cur
                
                
                

