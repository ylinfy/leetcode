class Solution:
    def minNumber(self, nums):
        ss = [str(x) for x in nums]
        self.quick_sort(ss, 0, len(ss) - 1)
        return ''.join(ss)

    def quick_sort(self, ss, l, r):
        if l >= r: return
        i, j = l, r
        while i < j:
            # x + y < y + x, 则x排在y前, 排完一次序后, 哨兵的左边全少于哨兵，右边全大于哨兵 
            while i < j and ss[l] + ss[j] <= ss[j] + ss[l]: j -= 1  # l排在j前面
            while i < j and ss[i] + ss[l] <= ss[l] + ss[i]: i += 1  # i排在l前面
            ss[i], ss[j] = ss[j], ss[i]
        ss[i], ss[l] = ss[l], ss[i]
        self.quick_sort(ss, l, i - 1)
        self.quick_sort(ss, i + 1, r)

