class Solution:
    # 正则表达式
    p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
    def isNumber(self, s):
        return bool(self.p.match(s.strip()))


    # 逻辑迭代
    def isNumber(self, s):
        s = s.strip()
        metN = metD = metE = False
        for i, c in enumerate(s):
            if c in ('+', '-'):
                if i > 0 and s[i-1] not in ('e', 'E'): return False
            elif c in ('e', 'E'):
                if metE or not metN: return False
                metE, metN = True, False
            elif c == '.':
                if metE or metD: return False
                metD = True
            elif c.isdigit(): metN = True
            else: return False
        return metN
        
