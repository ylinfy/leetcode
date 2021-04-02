class Solution:
    # 调用python库，time: N!*N
    def permutation(self, s):
        mem, res = set(), []
        # itertools.permutations(data, n): 将可迭代数据data的全排列
        # 以元组的方式存储在itertools.permutations可迭代object中，n是指选几个数
        for one in itertools.permutations(s):
            if one in mem: continue
            mem.add(one)
            res.append(''.join(one))
        return res


    # 回溯，time: N!*N
    def permutation(self, s: str) -> List[str]:
        self.res = []
        self.backtrack(list(s), 0)
        return self.res

    def backtrack(self, c: List[str], idx: int):
        if idx == len(c):
            self.res.append(''.join(c))
            return
        # 判重集合
        repeat = set()
        for i in range(idx, len(c)):
            # 判断当前数据，是否已经在当前层处理过了（组合过了）
            # 如['a', 'b', 'b', 'c'], 当'a'固定为首个字符时，遍历到第二个'b'时，直接continue
            if c[i] in repeat: continue
            repeat.add(c[i])
            # 固定当前idx索引的数据，遍历idx后的索引时，交换不同数据，得到不同组合
            c[i], c[idx] = c[idx], c[i] 
            self.backtrack(c, idx + 1)
            # 回溯时，还原当前层原排列
            c[i], c[idx] = c[idx], c[i] 

            
        
