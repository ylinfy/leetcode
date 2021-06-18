class Solution:
    # 双指针, 滑动窗口法, 取[i,j]连续正整数和与target比, 并移动指针, 相当于滑动窗口
    # time: N
    def findContinuousSequence(self, target):
        i, j, res = 1, 2, []
        # 当只有两个数时，j取得最大值，target // 2 + 1
        while j <= target // 2 + 1:
            # 求和，并与target比较, 比target小，则需要右移j, 否则，右移i
            # 等差数列求和：(i + j) * (j - i + 1) // 2
            s = (i + j) * (j - i + 1) // 2
            if s < target: j += 1
            elif s > target: i += 1
            else:
                res.append(list(range(i, j + 1)))
                i += 1
        return res


    # 间距法, 有连续正整数组[i, j], 令间距d=j-i, target=t, 将j = d + i代入连续正整数的等差公式
    # 可得连续正整数最左值(最小值): i = (t - d * (d + 1) // 2) // (d + 1) 
    # i > 0 且 i是正整数: 即 t > d(d+1)/2 且 (t -d(d+1)/2) % (d+1) == 0
    def findContinuousSequence(self, target):
        d, res = 1, []  # 从间距为1, 也就是只有两个数开始
        # 遍历间距d, 满足 i > 0
        while d * (d + 1) // 2 < target:
            # 满足 i 为正整数
            if not (target - d * (d + 1) // 2) % (d + 1): 
                i = (target - d * (d + 1) // 2) // (d + 1)
                res.append(list(range(i, d + i + 1)))
            d += 1
        # 从间距最小开始, 即正整数会是最大的, 需要反转一下res
        return res[::-1]
                
