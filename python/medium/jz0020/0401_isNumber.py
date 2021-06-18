class Solution:
    def isNumber(self, s):
        s = s.strip()
        metN = metD = metE = False
        for i, ch in enumerate(s):
            if ch in ('+', '-'):
                if i > 0 and s[i-1] not in ('e', 'E'): return False
            elif ch in ('e', 'E'):
                if metE or not metN: return False
                metE, metN = True, False  # 将metN设置为False，防止末尾e
            elif ch == '.':
                if metD or metE: return False
                metD = True
            elif ch.isdigit(): metN = True
            else: return False
        return metN



    p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
    def isNumber(self, s: str) -> bool:
        return bool(self.p.match(s.strip()))
