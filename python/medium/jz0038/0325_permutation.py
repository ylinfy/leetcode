class Solution:
    # 调库函数，time: N
    def permutation(self, s):
        temp, res = set(), []
        for one in itertools.permutations(s):
            if one in temp: continue
            res.append(''.join(one))
            temp.add(one)
        return res


    # 通用回溯，time: N
    def permutation(self, s):
        self.res = []
        self.dfs(0, list(s))
        return self.res

    def dfs(self, idx, lis):
        if idx == len(lis) - 1:
            self.res.append(''.join(lis))
            return 
        
        # 判重集合
        t_set = set()
        for i in range(idx, len(lis)):
            if lis[i] in t_set: continue
            t_set.add(lis[i])
            lis[i], lis[idx] = lis[idx], lis[i]
            self.dfs(idx + 1, lis)
            lis[i], lis[idx] = lis[idx], lis[i]

