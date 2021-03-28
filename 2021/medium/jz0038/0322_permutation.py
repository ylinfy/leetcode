class Solution:
    # 调库函数，time: N
    def permutation(self, s):
        mem, res = set(), []  
        for one in itertools.permutations(s):
            if one in mem: continue
            res.append(''.join(one))
            mem.add(one)
        return res

    # 递归，time: N
    def permutation(self, s):
        self.res = [] 
        self.dfs(0, list(s))
        return self.res

    def dfs(self, idx, clist):
        if idx == len(clist) - 1:
            self.res.append(''.join(clist))
            return 
        dic = set()
        for i in range(idx, len(clist)):
            if clist[i] in dic: continue
            dic.add(clist[i])
            clist[i], clist[idx] = clist[idx], clist[i]
            self.dfs(idx + 1, clist)
            clist[i], clist[idx] = clist[idx], clist[i]

            

