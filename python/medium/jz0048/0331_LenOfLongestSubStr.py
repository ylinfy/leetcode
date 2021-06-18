class Solution:
    # 双指针，time: N
    def LengthOfLongestSubString(self, s):
        res, i, dic = 0, -1, {}
        for j in range(len(s)):
            if s[j] in dic: i = max(i, dic[s[j]])
            dic[s[j]] = j
            res = max(res, j - i)
        return res
            

    # DP, 哈希，time: N
    def LengthOfLongestSubString(self, s):
        res, i, cur, dic = 0, -1, 0, {}
        for j in range(len(s)):
            if s[j] in dic: i = max(i, dic[s[j]])
            dic[s[j]] = j
            cur = cur + 1 if cur < j - i else j - i
            res = max(res, cur)
        return res
            
