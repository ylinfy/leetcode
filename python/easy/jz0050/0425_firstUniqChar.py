class Solution:
    def findUniqChar(self, s):
        uniq = dict()
        for c in s:
            uniq[c] = not c in uniq
        # python3.6后，字典是按插入顺序排序的，所以第二次可以直接遍历字典uniq
        for k, v in uniq.items():
            if v: return k 
        return " "
