class Solution:
    # 类似于0091题
    def translateNum(self, num):
        s = str(num)
        pre = cur = 1 
        for i in range(1, len(s)):
            tmp = cur
            if "10" <= s[i-1:i+1] <= "25": cur += pre
            pre = tmp
        return cur


    def translateNum(self, num):
        s = str(num)
        pre = cur = 1
        for i in range(1, len(s)):
            pre, cur = cur, pre * ("10" <= s[i-1:i+1] <= "25") + cur
        return cur

