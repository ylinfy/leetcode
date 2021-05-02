class Solution:
    # 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
    def firstUniqChar(self, s: str):
        uniq = dict()
        # 判断是否有重复字符，如果重复，value就存储为False
        for c in s:
            uniq[c] = not c in uniq
        # Python3.6后，dict是按插入顺序，有序排列键值，因此第一个单字符会排在靠前
        for k, v in uniq.items():
            if v: return k
        return ' '
