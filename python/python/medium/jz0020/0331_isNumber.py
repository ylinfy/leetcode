class Solution:
    # 逻辑判断法, time: N
    def isNumber(self, s):
        s = s.strip()
        # metD,metE,metN分别代表遇到dot,e/E,digit
        metD = metE = metN = False
        for i, ch in enumerate(s):
            if ch in ('+', '-'):  # 如果是sign, 要么在首位，要么紧跟e/E后
                if i > 0 and s[i-1] not in ('e', 'E'): return False
            elif ch == '.':  # 如果是dot, 前面不可存在dot或e/E
                if metD or metE: return False
                metD = True
            elif ch in ('e', 'E'):  # 如果是e/E, 前面不可无digit或有e/E
                if metE or not metN: return False
                metE, metN = True, False  # 防止e为最后ch，把metN置False
            elif ch.isdigit(): metN = True
            else: return False  # 是其他字符，直接返回False
        return metN


    # 正则表达式, time: N, 分三段匹配（首位符号位，e前部分，e及e后部分）
    def __init__(self):
        self.p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
    def isNumber(self, s):
        return bool(self.p.match(s.strip()))
            
        
