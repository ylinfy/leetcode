class Solution:
    # 双指针，哈希，time: N
    # i, j代表字符串中两个相同字符的最短间距, 即以s[j]为尾的最长子串长度为j-i
    def LengthOfLongestSubString(self, s):
        if not s: return 0
        i, res, dic = -1, 0, {}
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            res = max(res, j - i)
            dic[s[j]] = j
        return res
            

    # DP, 哈希, time: N
    # dp[j]: 以s[j]为尾的最长子串长度
    # if dp[j-1] < j - i, 说明与s[j]相同的字符s[i]在dp[j-1]对应子串左侧，即dp[j] = dp[j-1] + 1
    # else: 说明s[i]在dp[j-1]对应的子串，则dp[j] = j - i
    def LengthOfLongestSubString(self, s):
        if not s: return 0
        res, tmp, dic = 0, 0, {}
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(res, tmp)
        return res


    # DP, 线性迭代，time: N**2 (不推荐，省了点空间，但速度慢了太多)
    # i = j - 1, 往左迭代找到与s[j]相同字符来确定索引i
    def LengthOfLongestSubString(self, s):
        if not s: return 0
        res = tmp = 0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]: i -= 1
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(res, tmp)
        return res
        
