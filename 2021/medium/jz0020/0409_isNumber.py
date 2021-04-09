class Solution:
    # 正则式
    def __init__(self):
        self.p = re.compile(r"^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$")

    def isNumber(self, s):
        return bool(self.p.match(s.strip()))


    # 根据逻辑进行判断，time: N
    def isNumber(self, s):
        if not s: return False
        s = s.strip()
        metD = metE = metN = False
        for i, c in enumerate(s):
            if c in ('+', '-'):
                # +/-只能在第一位，或e/E的后一位，其余情况均直接返回False
                if i > 0 and s[i-1] not in ('e', 'E'): return False
            elif c in ('e', 'E'):
                # e/E前不能有e/E，e/E前不能没有数字
                if metE or not metN: return False
                metE, metN = True, False  # metN置为False, 防止以e/E结尾的情况
            elif c == '.':
                # 点的前面不能有e/E和点
                if metE or metD: return False
                metD = True
            elif c.isdigit(): metN = True
            else: return False
        # 最终将所有不符合的情况清除，如果s中有数字，即metN为True，那s一定是数值类s
        return metN

                
