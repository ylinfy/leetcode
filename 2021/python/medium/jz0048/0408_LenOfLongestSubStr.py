class Solution:
    # DP，dp[j]: 以j结尾的最长不含重复字符的子串
    # 设置j左边的索引i是和j一样的字符，存在两种情况：
    # dp[j-1]代表以j-1索引结尾的最长无重复字符子串，假设其在字符串上覆盖索引[t, j-1]
    # 情况1：当i在[t, j-1]区间时，dp[j] = j - i
    # 情况2：当i在[t, j-1]区间外，即i < t, 此时dp[j] = dp[j-1] + 1
    def lengthOfLongestSubString(self, s):
        if not s: return 0
        i, cur_sub_len = -1, 0
        max_sub_len, tmp = 0, set()
        for j, c in enumerate(s):
            if c in tmp:
                # 此处必须是max(i, tmp[c]), 若用i = tmp[c], 如"abcdbfa",以最后一个a为结尾的最长子串会出问题
                i = max(i, tmp[c])  
            tmp[c] = j
            cur_sub_len = cur_sub_len + 1 if cur_sub_len < j - i else j - i
            max_sub_len = max(max_sub_len, cur_sub_len)
        return max_sub_len


    def lengthOfLongestSubString(self, s):
        if not s: return 0
        i, res, tmp = -1, 0, {}
        for j, c in enumerate(s):
            if c in tmp:
                i = max(i, tmp[c])
            tmp[c] = j
            res = max(res, j - i)
        return res
