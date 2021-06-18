class Solution:
    # i, j双索引哈希, j - i 是以s[j]为尾的最长子串长度，s[i] == s[j] 或者 i == -1
    def lengthOfLongestSubString(self, s):
        res, i, dic = 0, -1, {}
        for j, c in enumerate(s):
            if c in dic: i = max(i, dic[c])
            dic[c], res = j, max(res, j - i)
        return res


    # DP哈希, time: N
    def lengthOfLongestSubString(self, s):
        # cur用来存储以当前字符为尾的最长子串长度
        res, cur, i, dic = 0, 0, -1, {}
        for j, c in enumerate(s):
            if c in dic: i = max(i, dic[c])
            # 计算前，cur相当于dp[j-1], 计算后cur即dp[j]
            # dp[j-1]长度如果小于j-i，说明i落在dp[j-1]长度范围外，即dp[j-1]中字符没有和c相同的，直接dp[j-1] + 1
            # 否则i落在dp[j-1]区间，说明有相同字符在dp[j-1]区间里，dp[j]应该直接等于j-i
            cur = cur + 1 if cur < j - i else j - i
            dic[c], res = j, max(res, cur)
        return res


