class Solution:
    # 双指针，滑动窗口，以最小两个正整数i,j=1,2开始
    def findContinuousSequence(self, target):
        max_right_num = target // 2 + 1
        i, j, res = 1, 2, []
        while j <= max_right_num:
            s = (i + j) * (j - i + 1) // 2
            if s > target: i += 1
            elif s < target: j += 1
            else: 
                res.append(list(range(i, j + 1)))
                i += 1
        return res

    # 左右索引间距法, d = j - i (i, j分别是连续正整数的左，右数)
    # sum = (i + j) * (j - i + 1) // 2 --> sum = (2 * i + d) * (d + 1) // 2
    # 令target为t, 就会有 sum = t, 即(2 * i + d) * (d + 1) // 2 = t
    # 最终可得：i = (t - d * (d + 1) // 2) // (d + 1)
    # 条件1：i > 0 即分子要大于0, t - d * (d + 1) // 2 > 0 --> d * (d + 1) // 2 < t
    # 条件2：i是正整数，即 (t - d * (d + 1) // 2) % (d + 1) == 0
    def findContinuousSequence(self, target):
        # 从间隔1开始，即两个数组成target
        d, res = 1, []
        # 根据条件1，限定d的上限，即间隔的最大值
        while d * (d + 1) // 2 < target:
            # 根据条件2，如果x不为整数，就舍弃当前间隔情况，扩大间隔
            if not (target - d * (d + 1) // 2) % (d + 1):
                # 如果两个条件都满足，代入公式求出i, 并根据j = d + i求出j
                i = (target - d * (d + 1) // 2) // (d + 1)
                res.append(list(range(i, d + i + 1)))
            d += 1
        # 由于间隔是从小到大，意味着res里结果是从大到小的，所以反转一下
        return res[::-1]

        
        


            
