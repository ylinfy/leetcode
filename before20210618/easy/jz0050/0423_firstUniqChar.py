class Solution:
    def firstUniqChar(self, s):
        uniq, removed = set(), set()
        for c in s:
            if c in removed: continue
            if c in uniq:
                uniq.remove(c)
                removed.add(c)
                continue
            uniq.add(c)
        for c in s:
            if c in s:
                return c
        return []


    def firstUniqChar(self, s):
        uniq = {}
        for c in s:
            uniq[c] = not c in uniq
        for c in s:
            if uniq[c]: return c
        return " "
            
