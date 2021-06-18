class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for c in s: dic[c] = not c in dic
        for c in s: 
            if dic[c]: return c
        return " "

