class Solution:
    def permutation(self, s: str):
        res, sList = [], list(s)
        self.backtrack(sList, res, 0)
        return list(res)

    def backtrack(self, L: list[chr], res: list[str], idx: int):
        if idx == len(L) - 1:
            res.append(''.join(L))
            return
        repeat = set() 
        for i in range(idx, len(L)):
            # 当i和idx交换时，得到的组合情况已经处理过了，直接跳过
            if L[i] in repeat: continue 
            repeat.add(L[i])
            L[i], L[idx] = L[idx], L[i] 
            self.backtrack(L, res, idx + 1)
            L[i], L[idx] = L[idx], L[i] 


    def permutation(self, s: str):
        mem, res = set(), []
        for one in itertools.permutations(s):
            if one in mem: continue
            mem.add(one)
            res.append(''.join(one))
        return res
        
