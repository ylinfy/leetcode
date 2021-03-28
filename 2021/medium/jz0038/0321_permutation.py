class Solution:
    # 调用python库, time: N! * N , 比通用回溯用时稍少
    def permutations(self, s):
        mem, res = set(), []
        # itertools.permutations(data, n): 将可迭代数据data的全排列
        # 以元组的方式存储在itertools.permutations可迭代object中，n是指选几个数
        for one in itertools.permutations(s):
            if one in mem: continue
            res.append(''.join(one))
            mem.add(one)
        return res


    # 回溯, python切片特性，time: N!*N
    def permutation(self, s):
        def permute(s, data):
            if len(data) == s_len:
                res.append(''.join(data))
                return []
            for i in range(len(s)):
                # 当前层已经处理过的数据，直接跳过
                if s[i] in s[:i]: continue
                permute(s[:i] + s[i+1:], data + [s[i]])
        res = []
        s_len = len(s)
        permute(s, [])
        return res


    # 通用回溯，time: N! * N
    def permutation(self, s):
        res = []
        self.dfs(0, list(s), res)
        return res

    def dfs(self.idx, clist, res):
        if idx == len(clist) - 1:
            res.append(''.join(clist))
            return 
        # 判重集合
        dic = set()
        for i in range(idx, len(clist)):
            # 判断当前数据，是否已经在当前层处理过了（组合过了）
            # 如['a', 'b', 'b', 'c'], 当'a'固定为首个字符时，遍历到第二个'b'时，直接continue
            if clist[i] in dic: continue
            dic.add(clist[i])
            # 固定当前idx索引的数据，遍历idx后的索引时，交换不同数据，得到不同组合
            clist[i], clist[idx] = clist[idx], clist[i]
            self.dfs(idx + 1, clist, res)
            # 回溯时，还原clist
            clist[i], clist[idx] = clist[idx], clist[i]

        

        
            
            
            
